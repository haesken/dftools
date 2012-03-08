#!/usr/bin/env python
# encoding: utf-8

""" Scrape the Bay12 site and forums for links to:
    Linux version of Dwarf Fortress, Phoebus tileset
    Then download them.
"""

import argparse
from lxml import etree
import sys
import subprocess


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Download & install Dwarf Fortress + Phoebus tileset.",
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-ddf", "--download_dwarf_fortress",
            action="store_true",
            help="Download Dwarf Fortress")

    parser.add_argument("-dph", "--download_phoebus",
            action="store_true",
            help="Download Phoebus")

    args = parser.parse_args()
    return args #}}}


def get_dwarf_fortress_link(): #{{{
    """ Scrape the Bay12 site for the linux Dwarf Fortress download link. """

    bay12_link = 'http://www.bay12games.com/dwarves/'
    tree = etree.parse(bay12_link, etree.HTMLParser())

    download_links_xpath = "/html/body/table[2]//table/tr/td/p/a"
    download_links = tree.xpath(download_links_xpath)

    links = [elem.items()[0][1] for elem in download_links]
    linux_base_link = [link for link in links if "linux" in link.lower()]
    linux_full_link = bay12_link + linux_base_link[0]

    return linux_full_link #}}}


def get_phoebus_host_link(): #{{{
    """ Scrape the Bay12 forums for the Phoebus tileset download link. """

    phoebus_post_link = ('http://www.bay12forums.com/' +
        'smf/index.php?topic=57557.0')
    tree = etree.parse(phoebus_post_link, etree.HTMLParser())

    download_links_xpath = ('/html/body/div/div[3]/div[4]/form/div/' +
        'div/div[2]/div[2]/div/a[4]')
    download_link = tree.xpath(download_links_xpath)[0].items()[0][1]

    return download_link #}}}


def get_phoebus_download_link(host_link): #{{{
    """ Scrape the given link for the actual download link. """

    tree = etree.parse(host_link, etree.HTMLParser())

    download_links_xpath = ('/html/body/div[4]/table/tr[2]/td/div/a')
    download_link_base = 'http://{domain}/'.format(
            domain=host_link.split('/')[2])
    download_link_suffix = tree.xpath(download_links_xpath)[0].items()[0][1]
    download_link = download_link_base + download_link_suffix
    # import ipdb; ipdb.set_trace()

    return download_link #}}}


def download_link(link, filename): #{{{
    """ Download a given url with wget. """

    subprocess.call('wget "{link}" -O "{filename}"'.format(
        link=link, filename=filename), shell=True) #}}}


def main(args): #{{{
    if args.download_dwarf_fortress == True:
        download_link(get_dwarf_fortress_link(), 'Dwarf_Fortress.tar.bz2')

    if args.download_phoebus == True:
        download_link(
                get_phoebus_download_link(get_phoebus_host_link()),
                'Phoebus.zip') #}}}


try:
    main(get_args())
except KeyboardInterrupt:
    sys.exit()
