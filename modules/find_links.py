# encoding: utf-8

""" Scrape the Bay12 site and forums for links to:
    Linux version of Dwarf Fortress, Phoebus tileset
    Then download them.
"""

"""
Copyright (c) 2012, haesken
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of haesken nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL haesken BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from lxml import html
import requests


def download_page(url): #{{{
    """ Download a page with Requests. Will handle https. """
    try:
        page = requests.get(url)
    except requests.ConnectionError:
        pass

    if page.status_code == 200:
        return page.content #}}}


def extract_links_from_xpath(url, link_xpath): #{{{
    """ Parse the html of a given url and extract the links of an xpath. """

    page = download_page(url)
    tree = html.fromstring(page)
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


def get_dfhack_download_link(): #{{{
    """ Get the download link for the current version of DFHack. """

    dfhack_downloads_link = 'http://github.com/peterix/dfhack/downloads/'
    links = extract_links_from_xpath(dfhack_downloads_link, "//a[@href]"),

    current_linux_link = [link[1] for link in links[0]
            if "linux.tar.gz" in link[1].lower()][0]

    current_linux_link_absolute = 'http://www.github.com' + current_linux_link

    return current_linux_link_absolute #}}}
