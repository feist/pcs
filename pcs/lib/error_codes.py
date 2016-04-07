from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

ACL_ROLE_ALREADY_EXISTS = 'ACL_ROLE_ALREADY_EXISTS'
ACL_ROLE_NOT_FOUND = 'ACL_ROLE_NOT_FOUND'
BAD_ACL_PERMISSION = 'BAD_ACL_PERMISSION'
BAD_ACL_SCOPE_TYPE = 'BAD_ACL_SCOPE_TYPE'
BAD_CLUSTER_STATE_FORMAT = 'BAD_CLUSTER_STATE_FORMAT'
CMAN_BROADCAST_ALL_RINGS = 'CMAN_BROADCAST_ALL_RINGS'
CMAN_UDPU_RESTART_REQUIRED = 'CMAN_UDPU_RESTART_REQUIRED'
CMAN_UNSUPPORTED_COMMAND = "CMAN_UNSUPPORTED_COMMAND"
CIB_CANNOT_FIND_CONFIGURATION = "CIB_CANNOT_FIND_CONFIGURATION"
CIB_LOAD_ERROR = "CIB_LOAD_ERROR"
CIB_LOAD_ERROR_SCOPE_MISSING = "CIB_LOAD_ERROR_SCOPE_MISSING"
CIB_LOAD_ERROR_BAD_FORMAT = "CIB_LOAD_ERROR_BAD_FORMAT"
CIB_PUSH_ERROR = "CIB_PUSH_ERROR"
COROSYNC_CONFIG_RELOAD_ERROR = "COROSYNC_CONFIG_RELOAD_ERROR"
CRM_MON_ERROR = "CRM_MON_ERROR"
COMMON_ERROR = 'COMMON_ERROR'
COMMON_INFO = 'COMMON_INFO'
ID_ALREADY_EXISTS = 'ID_ALREADY_EXISTS'
ID_NOT_FOUND = 'ID_NOT_FOUND'
IGNORED_CMAN_UNSUPPORTED_OPTION = 'IGNORED_CMAN_UNSUPPORTED_OPTION'
INVALID_ID = "INVALID_ID"
INVALID_METADATA_FORMAT = 'INVALID_METADATA_FORMAT'
INVALID_OPTION = "INVALID_OPTION"
INVALID_OPTION_VALUE = "INVALID_OPTION_VALUE"
INVALID_RESOURCE_NAME = 'INVALID_RESOURCE_NAME'
INVALID_TIMEOUT_VALUE = "INVALID_TIMEOUT_VALUE"
NODE_COMMUNICATION_ERROR = "NODE_COMMUNICATION_ERROR",
NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED = "NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED",
NODE_COMMUNICATION_ERROR_PERMISSION_DENIED = "NODE_COMMUNICATION_ERROR_PERMISSION_DENIED",
NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT = "NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT",
NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND = "NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND",
NODE_COROSYNC_CONF_SAVE_ERROR = "NODE_COROSYNC_CONF_SAVE_ERROR",
NODE_NOT_FOUND = "NODE_NOT_FOUND"
NON_UDP_TRANSPORT_ADDR_MISMATCH = 'NON_UDP_TRANSPORT_ADDR_MISMATCH'
PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND = "PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND"
PARSE_ERROR_COROSYNC_CONF = "PARSE_ERROR_COROSYNC_CONF",
PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE",
PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE",
RESOURCE_CLEANUP_ERROR = "RESOURCE_CLEANUP_ERROR"
RESOURCE_CLEANUP_TOO_TIME_CONSUMING = 'RESOURCE_CLEANUP_TOO_TIME_CONSUMING'
RESOURCE_WAIT_NOT_SUPPORTED = "RESOURCE_WAIT_NOT_SUPPORTED"
RESOURCE_WAIT_TIMED_OUT = "RESOURCE_WAIT_TIMED_OUT"
RESOURCE_WAIT_ERROR = "RESOURCE_WAIT_ERROR"
RRP_ACTIVE_NOT_SUPPORTED = 'RRP_ACTIVE_NOT_SUPPORTED'
RUN_EXTERNAL_PROCESS_ERROR = "RUN_EXTERNAL_PROCESS_ERROR"
UNABLE_TO_GET_AGENT_METADATA = 'UNABLE_TO_GET_AGENT_METADATA'
UNABLE_TO_READ_COROSYNC_CONFIG = "UNABLE_TO_READ_COROSYNC_CONFIG"
UNKNOWN_COMMAND = 'UNKNOWN_COMMAND'
UNKNOWN_RRP_MODE = 'UNKNOWN_RRP_MODE'
UNKNOWN_TRANSPORT = 'UNKNOWN_TRANSPORT'
UNSUPPORTED_RESOURCE_AGENT = 'UNSUPPORTED_RESOURCE_AGENT'
