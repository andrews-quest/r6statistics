import urllib.request
import bs4 as bs
import re


def retrieve():
    url = 'https://r6.tracker.network/profile/pc/AndrewSQuest'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = urllib.request.Request(url=url, headers=headers)
    raw_data = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(raw_data, features="html.parser")

    winrate = ''
    time_played = ''

    #for instance in soup.find_all('div', [{'data-stat' : 'PVPWLRatio'}, {'data-stat' : 'PVPTimePlayed'}]):
    for instance in soup.find_all('div', {'data-stat': ['PVPTimePlayed', 'PVPWLRatio']}):
        if re.findall('(.*?)%' , str(instance)) != []:
            winrate = re.findall('(.*?)%' , str(instance))
        if re.findall('(.*?)h', str(instance)) != []:
            time_played = re.findall('(.*?)h', str(instance))

    return winrate, time_played




