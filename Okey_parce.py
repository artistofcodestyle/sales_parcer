import requests


cookies = {
    'PHPSESSID': 'bnuoq1urh0b6im8m22f3blqsj6',
    'amp_a0683b': 'tx95c43k_rnDirQg4gmKnF.dDBjZ3ppbzl4Ymlhdg==..1gnsu2o8t.1gnsuc20e.0.0.0',
    'age_proof': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.okmarket.ru/customers/new_actions/c8012_w34_regulyarnyy_katalog_food_sportivnoe_pitanie_2023_2/',
}

params = {
    'sort': 'ASC',
    'nav-products': 'page-2',
}

response = requests.get(
    'https://www.okmarket.ru/customers/new_actions/c8012_w34_regulyarnyy_katalog_food_sportivnoe_pitanie_2023_2/',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.text)