#!/usr/bin/env python
# Copyright 2011 Ankur Goyal
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import BeautifulSoup
from termcolor import cprint
import md5
import re
import time
import urllib2

from config import settings

PRICE_REGEX = re.compile('\$([\d]+)')
BR_REGEX = re.compile('\dbr')
all_entries = {}

def parse_entry(entry):
    ret = {}

    ret['id'] = md5.md5(str(entry)).hexdigest()

    link = entry.find('a')
    ret['link'] = link['href']

    hook = link.contents[0]
    ret['hook'] = hook

    br = BR_REGEX.search(hook)
    br_match = False
    if br:
        ret['br'] = br[0]
        if ret['br'] <= settings.max_br and ret['br'] >= settings.min_br:
            br_match = True

    price_g = PRICE_REGEX.search(hook)
    price_match = False
    if price_g:
        ret['price'] = int(price_g.group(1))
        rent_per_person = ret['price'] / ret['br']
        if rent_per_person <= settings.max_rent_person and rent_per_person >= settings.min_rent_person:
            price_match = True
            

    neighborhood = entry.find('font').contents[0]
    ret['neighborhood'] = neighborhood

    neighborhood_match = False
    for n in settings.neighborhoods:
        if n.lower() in neighborhood.lower():
            neighborhood_match = True

    for n in settings.badhoods:
        if n.lower() in neighborhood.lower():
            neighborhood_match = False

    ret['match'] = price_match and neighborhood_match and br_match

    return ret


def scrape():
    html = urllib2.urlopen(settings.url).read()
    soup = BeautifulSoup.BeautifulSoup(html)

    bq = soup.findAll('blockquote')[1]
    entries = bq.findAll('p')
    for entry in entries:
        try:
            parsed = parse_entry(entry)
        except:
            #cprint("failure. " + str(entry), 'red')
            continue

        if parsed['id'] in all_entries:
            continue
        all_entries[parsed['id']] = parsed
        if parsed['match']:
            cprint(str(parsed), 'green')

if __name__ == '__main__':
    while True:
        scrape()
        time.sleep(settings.period)
