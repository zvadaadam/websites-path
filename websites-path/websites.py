import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_all_links(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as err:
        print(f'{err}')
        return []

    html_text = response.text

    soup = BeautifulSoup(html_text, 'lxml')

    links = soup.find_all('a')

    links = list(map(lambda x: x.get('href'), links))

    links = list(filter(lambda x: is_url_valid(x), links))

    links = list(map(lambda x: normalize_url(x), links))

    return links


def is_url_valid(url):
    try:
        result = urlparse(url)

        # result = result._replace(netloc=result.netloc.replace('www.', ''))
        # print(result.netloc.replace('www.', ''))

        return all([result.scheme, result.netloc, result.path])
    except:
        return False


def normalize_url(url):

    result = urlparse(url)

    # delete www.
    result = result._replace(netloc=result.netloc.replace('www.', ''))

    url = result.geturl()

    return url




