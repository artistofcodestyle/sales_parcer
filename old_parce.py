import pprint
import re
import requests

product_list = []
base_url = "https://fix-price.com/catalog/"
param_cat = {"pad": r"[Пп]роклад\w+", "cotton": r"[Вв]ат\w+", "tampon": r"[Тт]ампон\w*", "diaper": r"[Пп]ел[её]нк\w+",
             "nappy": r"[Пп]амперс\w+|[Пп]одгузник\w+",
             "urologic_pad": r"[Пп]роклад\w+\sуролог\w+|[Уу]ролог\w+\sпрокладк\w|[Пп]рокладк\w+\sдля\sуролог\w+",
             "beauty": r"[Гг]игиен\w+", "wet_tissue": r"[Вв]лажн\w+\sсалфет\w+|[Сс]алфет\w+\sвлажн\w+", "empty": ""
             }


def get_data_fix_price(page):       # Создает запрос на сайте. На вход подается страница
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }

    params = {'page': str(page), 'limit': '28', 'sort': 'sold'}

    json_data = {'category': 'kosmetika-i-gigiena'}

    response = requests.post('https://api.fix-price.com/buyer/v1/product/in/kosmetika-i-gigiena', params=params,
                             headers=headers, json=json_data).json()
    return response, int(params.get('limit'))   # Возвращает словарь с товарами со страницы и лимит на этой стр.


def parce_products(data_file):  # Проверяет товар на наличие скидки и выбранной категории -> выдает словарь товаров со %
    for product in data_file:
        if (product.get('specialPrice') and re.search(param_cat.get('empty'), product.get('title'))) is not None:
            # проверка категории в re.search(param_cat.get('######')
            sales_price_product = int(product.get('specialPrice').get('price'))
            id_product = product.get('id')
            squ_product = product.get('title')
            reg_price_product = float(product.get('price'))
            url_product = base_url + product.get('url')
            product_list.append(add_dict(id_product, squ_product, reg_price_product, sales_price_product, url_product))
        else:
            continue
    return product_list


def add_dict(id_prod, name, reg_price, sale_price, url):
    sale = round(((reg_price - sale_price) / reg_price * 100), 2)
    dict_prod = ({'id': id_prod, 'squ': name, 'regular price': reg_price, 'sales price': sale_price, 'sale': sale,
                  'URL': url})
    return dict_prod

def main():
    count_page = 1
    while True:     # проверка количества товаров на странице (если меньше лимита, то выход)
        data_file, limit = get_data_fix_price(count_page)
        total_product_list = parce_products(data_file)
        if len(data_file) == limit:
            count_page += 1
        else:
            break
    pprint.pprint(total_product_list)


# def main(url):
#     r = requests.get(url)
#     with open('test.html', 'w') as output_file:
#         output_file.write(str(r.text.encode('utf-8')))

if __name__ == "__main__":
    main()
