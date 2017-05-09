from bs4 import BeautifulSoup
import urllib

import argparse
from wikitools import wiki
from wikitools import page

def getLocations(soup):
    """
    requires a base BeatifulSoup object(with url)
    quick and dirty function to find get the locations of all the table rows and their labels
    """
    results = []
    trows = soup('table')[1].find_all('tr')
    if len(trows) < 2:
        return {'error': 'RSID not found.'}
    for header in trows:
        cleanText = header.get_text().split('\n')[0].replace(u'\xa0', ' ')
        results.append(cleanText)
    return results


def getSnpData(trows):
    results = dict()

    if len(trows) < 2:
        return {'error': 'RSID not found.'}
    for header in trows:
        d = header.find_all('td')
        key = d[0].text
        results[key] = d[1].text
    return results


def getData(locations, soup):
    """
    requires the locations array from getLocations and a base BeatifulSoup object(with url)
    pull genotype info based on
    """
    chromeIndex = locations.index('On chromosome')
    positionIndex = locations.index('Chromosome position')

    tvalues = soup('table')[1].find_all('td')
    trait = ''
    if 'Summary' in locations:
        trait = tvalues[locations.index('Summary')].find_all('span')[0].get_text().split(u"\u00A0")[0]
    elif 'Trait' in locations:
        trait = tvalues[locations.index('Trait')].find_all('span')[0].get_text().split(u"\u00A0")[0]

    chromosome = tvalues[chromeIndex].find_all('span')[0].get_text().split()[0]
    position = ''.join(tvalues[positionIndex].find_all('span')[0].get_text().split()[0].split(','))

    result = {
        'chromosome': chromosome,
        'position': position,
        'trait': trait
    }
    return result


def genotype(rsid):
    """
    requires an rsid string
    grabs information on an rsid, including location on the chromosome and general traits
    """
    if rsid[0] == 'I' or rsid[0] == 'i':
        return {'error': 'Cannot find indicators, must use rs #s'}
    soup = BeautifulSoup(urllib.urlopen('http://www.snpedia.com/index.php/Special:Browse/' + rsid, "").read(),
                         "html.parser")
    trows = soup('table')[1].find_all('tr')
    if len(trows) < 2:
        return {'error': 'That rsid does not have any data/does not exist.'}
    locations = getLocations(soup)
    genotypeData = getData(locations, soup)
    genotypeData['rsid'] = rsid
    return genotypeData


def snp(rsid, pair):
    """
    requires rsid and pair string
    grabs specific information for an snp with the supplied base pair
    """
    if rsid[0] == 'I' or rsid[0] == 'i':
        return {'error': 'Cannot find indicators, must use rs #s'}
    formatPair = '(' + pair[0].upper() + ';' + pair[1].upper() + ')'
    soup = BeautifulSoup(
        urllib.request.urlopen('http://snpedia.com/index.php/' + rsid + formatPair).read(),
        "html.parser")
    trows = soup('table')[1].find_all('tr')
    if len(trows) < 2:
        return {'error': 'That base pair does not have a trait associated with it.'}
    #locations = getLocations(soup)
    genotypeData = getSnpData(trows)
    genotypeData['rsid'] = rsid
    genotypeData['genotype'] = pair
    return genotypeData

def parse_snpedia_data(rsid, pair):
    if rsid[0] == 'I' or rsid[0] == 'i':
        return {'error': 'Cannot find indicators, must use rs #s'}
    formatPair = '(' + pair[0].upper() + ';' + pair[1].upper() + ')'
    soup = BeautifulSoup(
        urllib.request.urlopen('http://snpedia.com/index.php/' + rsid + formatPair).read(),
        "html.parser")
    trows = soup('table')[1]
    genotypeData = dict()
    genotypeData['trait'] = soup('table')[0].text
    genotypeData.update(snp(rsid, pair))
    return genotypeData

def search_snpedia(snp):
    """
    http://snpedia.com/index.php/Bulk
    """
    site = wiki.Wiki("http://bots.snpedia.com/api.php")
    pagehandle = page.Page(site, snp)
    snp_page = pagehandle.getWikiText()
    return snp_page