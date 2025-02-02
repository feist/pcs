from typing import (
    Any,
    Optional,
    Union,
)
from urllib.parse import urlparse

from pcs import (
    settings,
    utils,
)
from pcs.cli.common.errors import CmdLineInputError
from pcs.cli.common.parse_args import (
    Argv,
    InputModifiers,
    KeyValueParser,
    split_list_by_any_keywords,
)
from pcs.common.str_tools import format_list


def _parse_host_options(
    host: str, options: Argv
) -> dict[str, Union[str, list[dict[str, Union[None, str, int]]]]]:
    ADDR_OPT_KEYWORD = "addr"  # pylint: disable=invalid-name
    supported_options = {ADDR_OPT_KEYWORD}
    parsed_options = KeyValueParser(options).get_unique()
    unknown_options = set(parsed_options.keys()) - supported_options
    if unknown_options:
        raise CmdLineInputError(
            f"Unknown options {format_list(unknown_options)} for host '{host}'"
        )
    addr, port = _parse_addr(parsed_options.get(ADDR_OPT_KEYWORD, host))
    return {"dest_list": [dict(addr=addr, port=port)]}


def _parse_addr(addr: str) -> tuple[Optional[str], int]:
    if addr.count(":") > 1 and not addr.startswith("["):
        # if IPv6 without port put it in parentheses
        addr = f"[{addr}]"
    # adding protocol so urlparse will parse hostname/ip and port correctly
    url = urlparse(f"http://{addr}")

    common_exception = CmdLineInputError(
        f"Invalid port number in address '{addr}', use 1..65535"
    )
    # Reading the port attribute will raise a ValueError if an invalid port is
    # specified in the URL.
    try:
        port = url.port
    except ValueError:
        raise common_exception from None
    # urlparse allow 0 as valid port number, pcs does not
    if port == 0:
        raise common_exception
    return url.hostname, (port if port else settings.pcsd_default_port)


def auth_cmd(lib: Any, argv: Argv, modifiers: InputModifiers) -> None:
    """
    Options:
      * -u - username
      * -p - password
      * --token - auth token
      * --request-timeout - timeout for HTTP requests
    """
    del lib
    modifiers.ensure_only_supported("-u", "-p", "--request-timeout", "--token")
    if not argv:
        raise CmdLineInputError("No host specified")
    host_dict = {
        host: _parse_host_options(host, opts)
        for host, opts in split_list_by_any_keywords(argv, "host name").items()
    }
    token = modifiers.get("--token")
    if token:
        token_value = utils.get_token_from_file(str(token))
        for host_info in host_dict.values():
            host_info.update(dict(token=token_value))
        utils.auth_hosts_token(host_dict)
        return
    username, password = utils.get_user_and_pass()
    for host_info in host_dict.values():
        host_info.update(dict(username=username, password=password))
    utils.auth_hosts(host_dict)


def deauth_cmd(lib: Any, argv: Argv, modifiers: InputModifiers) -> None:
    """
    Options:
      * --request-timeout - timeout for HTTP requests
    """
    del lib
    modifiers.ensure_only_supported("--request-timeout")
    if not argv:
        # Object of type 'dict_keys' is not JSON serializable, make it a list
        remove_hosts = list(utils.read_known_hosts_file().keys())
    else:
        remove_hosts = argv
    output, retval = utils.run_pcsdcli(
        "remove_known_hosts", {"host_names": remove_hosts}
    )
    if retval == 0 and output["status"] == "access_denied":
        utils.err("Access denied")
    if retval == 0 and output["status"] == "ok" and output["data"]:
        try:
            if output["data"]["hosts_not_found"]:
                hosts = format_list(output["data"]["hosts_not_found"])
                utils.err(f"Following hosts were not found: '{hosts}'")
            if not output["data"]["sync_successful"]:
                utils.err(
                    "Some nodes had a newer known-hosts than the local node. "
                    + "Local node's known-hosts were updated. "
                    + "Please repeat the action if needed."
                )
            if output["data"]["sync_nodes_err"]:
                utils.err(
                    (
                        "Unable to synchronize and save known-hosts on nodes: "
                        + "{0}. Run 'pcs host auth {1}' to make sure the nodes "
                        + "are authorized."
                    ).format(
                        ", ".join(output["data"]["sync_nodes_err"]),
                        " ".join(output["data"]["sync_nodes_err"]),
                    )
                )
        except (ValueError, KeyError):
            utils.err("Unable to communicate with pcsd")
        return
    utils.err("Unable to communicate with pcsd")
