import os.path
from dataclasses import dataclass
from textwrap import dedent

from lxml import etree

from pcs import settings
from pcs.cli.reports.output import error
from pcs.common.tools import xml_fromstring


@dataclass
class Capability:
    code: str
    description: str
    in_pcs: bool
    in_pcsd: bool


def get_capabilities_definition() -> list[Capability]:
    """
    Read and parse capabilities file

    The point is to return all data in python structures for further processing.
    """
    filename = os.path.join(settings.pcsd_exec_location, "capabilities.xml")
    try:
        with open(filename, mode="r") as xml_file:
            capabilities_xml = xml_fromstring(xml_file.read())
    except (OSError, etree.XMLSyntaxError, etree.DocumentInvalid) as e:
        raise error(
            f"Cannot read capabilities definition file '{filename}': '{e}'"
        ) from e
    capabilities = []
    for feat_xml in capabilities_xml.findall(".//capability"):
        desc_elem = feat_xml.find("./description")
        # dedent and strip remove indentation in the XML file
        desc = "" if desc_elem is None else dedent(desc_elem.text or "").strip()
        capabilities.append(
            Capability(
                code=str(feat_xml.attrib["id"]),
                description=desc,
                in_pcs=feat_xml.attrib["in-pcs"] == "1",
                in_pcsd=feat_xml.attrib["in-pcsd"] == "1",
            )
        )
    return capabilities


def get_pcs_capabilities() -> list[Capability]:
    """
    Get pcs capabilities from the capabilities file
    """
    return [feat for feat in get_capabilities_definition() if feat.in_pcs]


def get_pcsd_capabilities() -> list[Capability]:
    """
    Get pcsd capabilities from the capabilities file
    """
    return [feat for feat in get_capabilities_definition() if feat.in_pcsd]
