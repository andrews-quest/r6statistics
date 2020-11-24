import bs4 as bs
import urllib.request
import re


# https://habr.com/ru/post/488720/
def retrieve_data():
    url = 'https://r6.tracker.network/profile/pc/AndrewSQuest/operators'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = urllib.request.Request(url=url, headers=headers)
    raw_data = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(raw_data, features="html.parser")

    all_data = open('all_data.txt', 'w')
    all_data.write(str(raw_data, encoding='utf-8'))

    attackers_list = list()
    defenders_list = list()
    operators_list = list()

    att_or_def_counter = 0
    att_or_def_index = 0

    for string in soup.find_all('tr'):
        operator = re.findall('<span>(.*?)</span>', str(string))
        time_played = re.findall('>(.*?)h (.*?)m<', str(string))
        if len(time_played) > 0:
            time_played_raw = (int(time_played[0][0]) * 60) + int(time_played[0][1])

        #!!! forming of attackers and defenders list separately, using blank spaces in 'operators' line
        if len(operator) != 0:
            if operator[0] not in ('SAS', 'FBI SWAT', 'SPETSNAZ', 'GIGN', 'GSG 9'):
                operators_list.append((operator[0], time_played_raw, int(time_played[0][0]) + int(time_played[0][1]) / 60))
                #print(operator[0] + ' ' + str(time_played_raw) + ' m')
        else:
            att_or_def_counter = att_or_def_counter + 1
            if att_or_def_counter == 2:
                att_or_def_index = len(attackers_list)

        attackers_list = operators_list[0:att_or_def_index-1]
        defenders_list = operators_list[att_or_def_index:]

    operators = open('operators.txt', 'w')
    for operator_info in operators_list:
        for column in operator_info:
            operators.write(str(column) + ' ')
        operators.write('\n')
    return attackers_list, defenders_list
