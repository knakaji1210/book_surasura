import requests
from bs4 import BeautifulSoup

result = requests.get('https://pycon.jp/2016/ja/schedule/talks/list/')
soup = BeautifulSoup(result.text, 'html.parser')
presentation_html_list = soup.find_all('div', class_='presentation')

with open('pyconjp-2016-talks.csv', 'w') as f:
    f.write('"{0}", "{1}"\n'.format('Language', 'Title'))
    
    for presentation_html in presentation_html_list:
        presentation_title_text = presentation_html.h3.get_text()

        if '(en)' in presentation_title_text:
            language = 'English'
            title = presentation_title_text.replace(' (en)', '')
        elif '(ja)' in presentation_title_text:
            language = 'Japanese'
            title = presentation_title_text.replace(' (ja)', '')

        f.write('"{0}", "{1}"\n'.format(language, title))
