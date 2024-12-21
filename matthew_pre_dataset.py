import requests
from bs4 import BeautifulSoup
import re
import json


def spider_matthew_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    font_tags = soup.find_all("font")
    data_all = []
    data = {"input": "", "output": ""}
    for font_tag in font_tags:
        span_tags = font_tag.find_all("span")
        for span in span_tags:
            text = span.get_text(strip=True)
            if re.search(r'[a-zA-Z]', text):
                data['input'] = text
            else:
                data['output'] = text
            if data['input'] and data['output']:
                data_all.append(data.copy())
                data = {"input": "", "output": ""}
    data_all_json = json.dumps(data_all, ensure_ascii=False, indent=4)
    print(data_all_json)
    with open('./test_matthew_dataset.json', 'w', encoding='utf-8') as f:
        f.write(data_all_json)
    print('Spider Matthew Data Finished !!!')


def _test_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    font_tags = soup.find_all("font")
    data_all = []
    data = {"input": "", "output": ""}
    for font_tag in font_tags:
        span_tags = font_tag.find_all("span")
        em_tags = font_tag.find_all_next("em")
        print(f"em_tags : {em_tags}")
        for span in span_tags:
            text = span.get_text(strip=True)
            if re.search(r'[a-zA-Z]', text):
                data['input'] = text
            else:
                data['output'] = text
            if data['input'] and data['output']:
                data_all.append(data.copy())
                data = {"input": "", "output": ""}
    data_all_json = json.dumps(data_all, ensure_ascii=False, indent=4)
    print(data_all_json)
    with open('./test_matthew_dataset.json', 'w', encoding='utf-8') as f:
        f.write(data_all_json)
    print('Spider Matthew Data Finished !!!')


if __name__ == '__main__':
    # TheHolyAramaicScriptures.com MATTHEW'S WebPage Contents
    url = "https://theholyaramaicscriptures.weebly.com/mat-5.html"

    spider_matthew_data(url)

    # ************************* Test Data Start *************************** #
    # _test_data(url)
    # ************************* Test Data End *************************** #
