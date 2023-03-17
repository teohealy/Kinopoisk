import requests
from bs4 import BeautifulSoup


def summary(path, lang, limit: int):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        rus_list = []
        en_list = []
        for i in soup.find_all("span", attrs={'data-tid': '4502216a'}):
            rus_list.append(i.text)
        for i in soup.find_all("span", class_='desktop-list-main-info_secondaryTitle__ighTt'):
            en_list.append(i.text)
        if lang == 'rus':
            return rus_list[:int(limit)]
        else:
            return en_list[:int(limit)]

