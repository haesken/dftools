# encoding: utf-8

""" Scrape the Bay12 site and forums for links to:
    Linux version of Dwarf Fortress, Phoebus tileset
    Then download them.
"""

from lxml import etree


def extract_links_from_xpath(url, link_xpath): #{{{
    """ Parse the html of a given url and extract the links of an xpath. """

    tree = etree.parse(url, etree.HTMLParser())
    elems = tree.xpath(link_xpath)

    links = [(elem.text, str(elem.values()[0])) for elem in elems]
    return links #}}}


def get_dwarf_fortress_link(): #{{{
    """ Get the download link to the linux version of Dwarf Fortress. """

    bay12_link = 'http://www.bay12games.com/dwarves/'
    links = extract_links_from_xpath(bay12_link, "//p/a[@href]"),

    linux_link = [link[1] for link in links[0]
            if "linux.tar" in link[1].lower()]

    linux_link_absolute = bay12_link + linux_link[0]

    return linux_link_absolute #}}}


def get_phoebus_host_link(): #{{{
    """ Scrape the Bay12 forums for the Phoebus tileset download link. """

    phoebus_post_link = ('http://www.bay12forums.com/' +
            'smf/index.php?topic=57557.0')
    links_xpath = '//a[@href]'
    links = extract_links_from_xpath(phoebus_post_link, links_xpath)

    phoebus_host_link = [link[1] for link in links
            if "Graphic Set Package @DFFD" == link[0]][0]

    return phoebus_host_link #}}}


def get_phoebus_download_link(host_link): #{{{
    """ Scrape the given link for the actual download link. """

    links_xpath = '//a[@href]'
    links = extract_links_from_xpath(host_link, links_xpath)

    host = 'http://{host}/'.format(host=host_link.split("/")[2])
    download_suffix = [link[1] for link in links
            if "download.php?id=" in link[1]][0]

    phoebus_download_link = host + download_suffix

    return phoebus_download_link #}}}
