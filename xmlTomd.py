import xml.etree.ElementTree as ET
from tabulate import tabulate
import argparse


def parse_nmap_xml(xmlfile):
    # Parse XML
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    tableData = []
    for link in root.findall('urldata'):
        # we need
        # * broken link
        # * the URL of where the broken link appears
        # * where in the above it appears
        # * the "result"
        fullURL = link.find('realurl').text
        parentLink = link.find("parent")
        parentURL = parentLink.text
        parentLoc = parentLink.attrib.get('line')
        result = link.find('valid').attrib.get('result')

        brokenRow = [fullURL, parentURL, parentLoc, result]
        tableData.append(brokenRow)

    # Create and print table
    table = tabulate(tableData, headers=['Broken Link', 'Parent', 'Line in Parent', 'Reason'], tablefmt="github")
    print(table)
    print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse an Nmap XML file.')
    parser.add_argument('xmlfile', type=str, help='Path to the XML file')
    args = parser.parse_args()

    parse_nmap_xml(args.xmlfile)
