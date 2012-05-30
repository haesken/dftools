# encoding: utf-8

""" Scrape various sites for df/tileset download links. """

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
        if page.status_code == 200:
            return page.content
    except requests.ConnectionError:
        print 'Requests ConnectionError!' #}}}


def extract_links_from_xpath(url, link_xpath): #{{{
    """ Parse the html of a given url and extract the links of an xpath. """

    page = download_page(url)
    if page != None:
        tree = html.fromstring(page)
        elems = tree.xpath(link_xpath)

        return [(elem.text, str(elem.values()[0])) for elem in elems] #}}}


def get_dwarf_fortress_links(): #{{{
    """ Get the download link to the linux version of Dwarf Fortress. """

    bay12_link = 'http://www.bay12games.com/dwarves/'
    raw_links = extract_links_from_xpath(bay12_link, "//p/a[@href]"),

    platform_links = raw_links[0][:6]
    windows_link = bay12_link + platform_links[0][1]
    linux_link = bay12_link + platform_links[4][1]
    osx_link = bay12_link + platform_links[5][1]

    return (windows_link, linux_link, osx_link) #}}}


def get_dfhack_download_link(): #{{{
    """ Get the download link for the current version of DFHack. """

    dfhack_downloads_link = 'http://github.com/peterix/dfhack/downloads/'
    links = extract_links_from_xpath(dfhack_downloads_link, "//a[@href]"),

    current_linux_link = [link[1] for link in links[0]
            if "linux.tar.gz" in link[1].lower()][0]

    return  'http://www.github.com' + current_linux_link #}}}
