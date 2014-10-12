#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import requests
import json
from urlparse import urlparse
from datetime import datetime

base_url = 'http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen'

def get_details(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text)

    result = dict()

    for dl in html.findAll('dl'):
        column_number = 0

        for dd in dl.findAll('dd'):
            #print column_number, "-", dd.text
            
            if column_number == 1:
                result['direction'] = dd.text

            if column_number == 5:
                result['description'] = dd.text
            
            if column_number == 6:
                result['barrierfree'] = dd.text
            
            if dd.a:
                result['url'] = base_url + dd.a['href']

            column_number += 1

    return result

def get_issues(details=False):
    page = requests.get(base_url)
    html = BeautifulSoup(page.text)

    issues = []

    # parse the page's table containing all relevant information
    for table_row in html.findAll('tr'):
        # we use a counter to distinguish the four different columns
        column_number = 0

        # create a prototype entry
        entry = {
            "id": {},
            "what": {},
            "when": {},
            "where": {},
            "why": {} 
        }

        for table_column in table_row.findAll('td'):
            # collect the content of the nested tags
            content = [x for x in [BeautifulSoup(str(x)).text.strip() for x in table_column.contents] if x]

            # check if there is a link; if so, prefix it with the base url
            if table_column.a:
                link = base_url + table_column.a['href']

            # column 0 contains the type of transportation and the line
            if column_number == 0:
                # the first entry is the medium (subway, bus, ...)
                entry['what']['medium'] = content[0]

                if len(content) > 1:
                    # if there is a second entry, it is the line (works for anything but subways)
                    entry['what']['line'] = content[1]
                else:
                    # if not, we can use a part of the span to get the line (for subways)
                    spans = table_column.span['class']
                    entry['what']['line'] = spans.split("--")[1].upper()

            # column 1 contains information about the dates
            if column_number == 1:
                # process begin date
                begin = datetime.strptime(content[0], "von %d.%m.%Y %H:%M")
                entry['when']['begin'] = begin.isoformat()

                # process end date (can be 'until further notice', for which we use None)
                if content[1] == 'bis auf Weiteres':
                    entry['when']['end'] = None
                else:
                    end = datetime.strptime(content[1], "bis %d.%m.%Y %H:%M")
                    entry['when']['end'] = end.isoformat()

            # column 2 contains information about the reasons - note we shall later add a link to the 'why' section
            if column_number == 2:
                entry['why']['reason'] = content[0]

            # column 3 contains information about where the issue is
            if column_number == 3:
                # the stations are separated with "⇄"
                stations = content[0].split("&#x21c4;")
                entry['where']['start'] = stations[0].strip()
                entry['where']['end'] = stations[1].strip()
                # add the link
                entry['why']['url'] = link
                # use the id in the url as id
                entry['id'] = int(urlparse(link)[4].replace("id=", ""))
                
                if details:
                    entry['details'] = get_details(link)

            column_number += 1

        issues.append(entry)

    # remove first entry (table headers)
    issues = issues[1:]

    results = {
        "source_root_url": base_url,
        "issue_count": len(issues),
        "issues": issues
    }

    return results

if __name__ == "__main__":
    print json.dumps(get_issues(True), indent=4)
