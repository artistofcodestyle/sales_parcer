# -*- coding: utf-8 -*-
import pprint
import requests
from bs4 import BeautifulSoup

base_url = 'https://vkusvill.ru'
product_list = []


def get_data_vv_price(current_page, b_url):
    cookies = {'PHPSESSID': 'LHhq30fRni7TWPFZeG1U7mFe0UPrC5Ks', 'BX_USER_ID': '181bb483cd1c796a8f2f25169c687eca'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    response = requests.get(f'{b_url}/goods/kosmetika-sredstva-gigieny/?PAGEN_1={int(current_page)}',
                            cookies=cookies, headers=headers)
    return response.text


# url_vprok = 'https://www.vprok.ru/catalog/4486/uhod-za-bolnymi'
# headers = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#             "Connection": "keep-alive",
#             "Cookie": "split_segment=5; region=1; deliveryTypeId=1; standardShopId=2527; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5IiwianRpIjoidXVpZDQ3MGU2MzU2LTQ3MTEtNDU0My1iYWM3LWU0NGVhZDcxZWY4OGQ4ZTlhMDhmNTIyZjUwMDdiNzQxZGQ5ZTZlNDc0YjYzY2E2Y2M2NjkiLCJpYXQiOjE2NzQ3NjAxNzIuMTIxNDkzLCJuYmYiOjE2NzQ3NjAxNzIuMTIxNDk2LCJleHAiOjE2NzQ4NDY1NzIuMTE3MDMsInN1YiI6IiIsInNjb3BlcyI6W10sInNwbGl0X3NlZ21lbnQiOjV9.qH547j_rB6IqYaYPcGVDEaq3ik8PYrLR7GWeNUWyA7oUKIPXPUz3lbU-sEKl232HhILnntfb6WA8TPVW5TWm7ruOLWyL6lm8XZmE89rqiFIqAdQF-buTFd5CRDR9Kb6rfpDk-vvwa4yvQu0TKbKKUnL6BDCUOa_0CcUXRrMpQVJH7CvCYDDz9M-hPDDDu7UGmKAP2i4RziNM3P8bt_Z84ezvUVIDJ0FdMDcVUyUBq8VEc8OsNFO9352qFKHyVTXhDgO_yngxO4Vjg2Ap6L8oUnSO9-UTCE4SeCBY-Skqs3Oc8tho2311yuiIBb5X-77TZzwPAO1bfci54cGrOY6d3fCIDIFI5w3nl0KEtgmaN_N2zgECWOgRF4Fnq1uGbyUaPLejtNBnBXdrBRBkTd_M3IgcdDtkLTbVn30YEmFGIA59SQXx-VTBLZ16n2sR65QhL9Pd67SVObMUqUuLEDupSxdgjq9K6j9ZUdGa023LSbZL1FBDQPQhug3HXL-KzcRSEaAW8yDa6eHsSqQbL1VUXULkQdJ7UsX35D9qPSX2s96o34PXfDIxWYe-IOKI4zDt-z4RpcybLtNv0C9DY576T0gXLAE7wUeEGZ7O0kkAyVFRzJzuH5WY7a2TObZJdUQLjjBL8duMFJ_1lxuOp3avVTauic9ZW0Ijwz2AER5Cfe0; split_segment_amount=11; shop=2527; noHouse=0; __zzatgib-w-vprok=MDA0dBA=Fz2+aQ==; __zzatgib-w-vprok=MDA0dBA=Fz2+aQ==; cfidsgib-w-vprok=PJUgAIJ470khd9KDPdU7PJhw50HAxVtKgeS+9INtj3gzakz9amy8UftI1v+JpkDzxyZzqv9TKVOZmOTeUp+I37BFdQa0OnB8TwngfZkW3hFhC/IobAkulunDxdh3+M5kVYhjK9LTnW1l4+KoKs31LwR33y0FMM4fhDlfZHY=; cfidsgib-w-vprok=bXcHU8r6eQDERAsBekyJ2MCM186uSu6X+E/vFNR8O1J7PkGk/5nmTnDzX+RuGzfuCekQzvyBRhqELSlUdzbxIr7JhvX0RVq+d/oPG7Qesq3zCZMc9jxuHJYBvjDmYyohaMwBnr1P9vWbEWUJbd58HrOPiSPWpya6EC3Xfvc=; cfidsgib-w-vprok=bXcHU8r6eQDERAsBekyJ2MCM186uSu6X+E/vFNR8O1J7PkGk/5nmTnDzX+RuGzfuCekQzvyBRhqELSlUdzbxIr7JhvX0RVq+d/oPG7Qesq3zCZMc9jxuHJYBvjDmYyohaMwBnr1P9vWbEWUJbd58HrOPiSPWpya6EC3Xfvc=; gsscgib-w-vprok=i+speXMvz1uYaKy8uv6Dq92ER7noBQ0JlBKfMHUwqVZvrjwY0Jn/u8JkYkInDqBHAeKOhPU6wE56/86IKI2dkbm3dRVP40Tj2PgF0kc/XC5ODc54SBz9Npt3uXTxlCzQB2iMJ1dyeH80mbP+2EL/hDYt0SgkgmYditzkLsY6FmINRtEqjebGKTnGUljRC8mf2ERyoDXhXemdpu9bnxa/Z9RA01EjTkx3BKGJ46xq0VBfpcTjB1jo9fg4L8rIIGeBEQ==; gsscgib-w-vprok=i+speXMvz1uYaKy8uv6Dq92ER7noBQ0JlBKfMHUwqVZvrjwY0Jn/u8JkYkInDqBHAeKOhPU6wE56/86IKI2dkbm3dRVP40Tj2PgF0kc/XC5ODc54SBz9Npt3uXTxlCzQB2iMJ1dyeH80mbP+2EL/hDYt0SgkgmYditzkLsY6FmINRtEqjebGKTnGUljRC8mf2ERyoDXhXemdpu9bnxa/Z9RA01EjTkx3BKGJ46xq0VBfpcTjB1jo9fg4L8rIIGeBEQ==; fgsscgib-w-vprok=yzWL8b4c8b5f04831fcefc70fa95c1ce7bba3aac; fgsscgib-w-vprok=yzWL8b4c8b5f04831fcefc70fa95c1ce7bba3aac; fcf=3; aid=eyJpdiI6IlZUWE9ZMms1UzBIVXFuelE2eVRqRGc9PSIsInZhbHVlIjoiR3h1NlE2TWcyRktvVmRJd3VwRGlzcXlyNWVSazdhaUM1U3c0SXpFSW5JczRXekZnTE1ac1wvaWs5WjVTVFVqZ2tjTFBaNW11VFwvT21Bcms4aXBmMmdwZz09IiwibWFjIjoiYjMxODg5ODVlZmUwMGNiNzQ2MWQ0OTE2OTMzMGVmNWRkM2NlOTIxNjEwNTA1YTRiYmU0NTA2ZjYyODQ0MDFiZCJ9; suuid=bf7ffd0e-ec00-432a-991f-5ce2dc0ccecd; isUserAgreeCookiesPolicy=true; x-next-route-destination=%2Fcatalog%2F4486%2Fuhod-za-bolnymi; luuid=470e6356-4711-4543-bac7-e44ead71ef88; XSRF-TOKEN=eyJpdiI6InRiQVB2WXBPYWpFMUNmYUhFN2pUZ1E9PSIsInZhbHVlIjoiUmd0TXF3MFcwYWRjMWhJR2ZqS0wrTGo0NFl6MGJkaU5Pa0htN0RHYXVaMyszc0dDVStCMWhzd1wvTWk1K3hKYzkrNDdDTmtXQ0oyWjVqV1ZGN0xoWnl3PT0iLCJtYWMiOiJjZTI4NTgzNTMyMDkxMDUyYWYxNTJlYjY5MTAwZGU5ODg0ZmQ4MzkxNmNjZWM3NzFlMWMxMmVhMWJmZDY4NmE0In0%3D; gssc777781=; ngenix_jscv_a68b51100641=cookie_signature=xWE7uIoCgO0ZNEQuVLwIdTOW0VQ%3D&cookie_expires=1674763914",
#             "Host": "www.vprok.ru",
#             "Sec-Fetch-Dest": "document",
#             "Sec-Fetch-Mode": "navigate",
#             "Sec-Fetch-Site": "cross-site",
#             "TE": "trailers",
#             "Upgrade-Insecure-Requests": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"}
#
# cookies = {
# 		"__zzatgib-w-vprok": "MDA0dBA=Fz2+aQ==",
# 		"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5IiwianRpIjoidXVpZDQ3MGU2MzU2LTQ3MTEtNDU0My1iYWM3LWU0NGVhZDcxZWY4OGQ4ZTlhMDhmNTIyZjUwMDdiNzQxZGQ5ZTZlNDc0YjYzY2E2Y2M2NjkiLCJpYXQiOjE2NzQ3NjAxNzIuMTIxNDkzLCJuYmYiOjE2NzQ3NjAxNzIuMTIxNDk2LCJleHAiOjE2NzQ4NDY1NzIuMTE3MDMsInN1YiI6IiIsInNjb3BlcyI6W10sInNwbGl0X3NlZ21lbnQiOjV9.qH547j_rB6IqYaYPcGVDEaq3ik8PYrLR7GWeNUWyA7oUKIPXPUz3lbU-sEKl232HhILnntfb6WA8TPVW5TWm7ruOLWyL6lm8XZmE89rqiFIqAdQF-buTFd5CRDR9Kb6rfpDk-vvwa4yvQu0TKbKKUnL6BDCUOa_0CcUXRrMpQVJH7CvCYDDz9M-hPDDDu7UGmKAP2i4RziNM3P8bt_Z84ezvUVIDJ0FdMDcVUyUBq8VEc8OsNFO9352qFKHyVTXhDgO_yngxO4Vjg2Ap6L8oUnSO9-UTCE4SeCBY-Skqs3Oc8tho2311yuiIBb5X-77TZzwPAO1bfci54cGrOY6d3fCIDIFI5w3nl0KEtgmaN_N2zgECWOgRF4Fnq1uGbyUaPLejtNBnBXdrBRBkTd_M3IgcdDtkLTbVn30YEmFGIA59SQXx-VTBLZ16n2sR65QhL9Pd67SVObMUqUuLEDupSxdgjq9K6j9ZUdGa023LSbZL1FBDQPQhug3HXL-KzcRSEaAW8yDa6eHsSqQbL1VUXULkQdJ7UsX35D9qPSX2s96o34PXfDIxWYe-IOKI4zDt-z4RpcybLtNv0C9DY576T0gXLAE7wUeEGZ7O0kkAyVFRzJzuH5WY7a2TObZJdUQLjjBL8duMFJ_1lxuOp3avVTauic9ZW0Ijwz2AER5Cfe0",
# 		"aid": "eyJpdiI6IlZUWE9ZMms1UzBIVXFuelE2eVRqRGc9PSIsInZhbHVlIjoiR3h1NlE2TWcyRktvVmRJd3VwRGlzcXlyNWVSazdhaUM1U3c0SXpFSW5JczRXekZnTE1ac1wvaWs5WjVTVFVqZ2tjTFBaNW11VFwvT21Bcms4aXBmMmdwZz09IiwibWFjIjoiYjMxODg5ODVlZmUwMGNiNzQ2MWQ0OTE2OTMzMGVmNWRkM2NlOTIxNjEwNTA1YTRiYmU0NTA2ZjYyODQ0MDFiZCJ9",
# 		"cfidsgib-w-vprok": "bXcHU8r6eQDERAsBekyJ2MCM186uSu6X+E/vFNR8O1J7PkGk/5nmTnDzX+RuGzfuCekQzvyBRhqELSlUdzbxIr7JhvX0RVq+d/oPG7Qesq3zCZMc9jxuHJYBvjDmYyohaMwBnr1P9vWbEWUJbd58HrOPiSPWpya6EC3Xfvc=",
# 		"deliveryTypeId": "1",
# 		"fcf": "3",
# 		"fgsscgib-w-vprok": "yzWL8b4c8b5f04831fcefc70fa95c1ce7bba3aac",
# 		"gssc777781": "",
# 		"gsscgib-w-vprok": "i+speXMvz1uYaKy8uv6Dq92ER7noBQ0JlBKfMHUwqVZvrjwY0Jn/u8JkYkInDqBHAeKOhPU6wE56/86IKI2dkbm3dRVP40Tj2PgF0kc/XC5ODc54SBz9Npt3uXTxlCzQB2iMJ1dyeH80mbP+2EL/hDYt0SgkgmYditzkLsY6FmINRtEqjebGKTnGUljRC8mf2ERyoDXhXemdpu9bnxa/Z9RA01EjTkx3BKGJ46xq0VBfpcTjB1jo9fg4L8rIIGeBEQ==",
# 		"isUserAgreeCookiesPolicy": "true",
# 		"luuid": "470e6356-4711-4543-bac7-e44ead71ef88",
# 		"ngenix_jscv_a68b51100641": "cookie_signature=xWE7uIoCgO0ZNEQuVLwIdTOW0VQ=&cookie_expires=1674763914",
# 		"noHouse": "0",
# 		"region": "1",
# 		"shop": "2527",
# 		"split_segment": "5",
# 		"split_segment_amount": "11",
# 		"standardShopId": "2527",
# 		"suuid": "bf7ffd0e-ec00-432a-991f-5ce2dc0ccecd",
# 		"x-next-route-destination": "/catalog/4486/uhod-za-bolnymi",
# 		"XSRF-TOKEN": "eyJpdiI6InRiQVB2WXBPYWpFMUNmYUhFN2pUZ1E9PSIsInZhbHVlIjoiUmd0TXF3MFcwYWRjMWhJR2ZqS0wrTGo0NFl6MGJkaU5Pa0htN0RHYXVaMyszc0dDVStCMWhzd1wvTWk1K3hKYzkrNDdDTmtXQ0oyWjVqV1ZGN0xoWnl3PT0iLCJtYWMiOiJjZTI4NTgzNTMyMDkxMDUyYWYxNTJlYjY5MTAwZGU5ODg0ZmQ4MzkxNmNjZWM3NzFlMWMxMmVhMWJmZDY4NmE0In0="
# 	}
#
# response = requests.get(url_vprok, cookies=cookies, headers=headers)


def parce_squ_on_page(goods_on_page, b_url):
    for good in goods_on_page:
        squ_regular_price = float(good.find('span', class_='js-datalayer-catalog-list-price-old hidden').text.strip())
        squ_current_price = float(good.find('span', class_='js-datalayer-catalog-list-price hidden').text.strip())
        if squ_regular_price != squ_current_price:
            squ_id = None #good.find('div', class_='ProductCard js-product-cart js-datalayer-catalog-list-item _woDeliv')\
                # .get('data-id')
            good_data = good.find('a', class_='ProductCard__link rtext _desktop-md _mobile-sm gray900 js-datalayer-'
                                              'catalog-list-name')
            squ_name = good_data.attrs['title']
            print(squ_name)
            squ_href = b_url + good_data.get('href')
            product_list.append(add_dict(squ_id, squ_name, squ_regular_price, squ_current_price, squ_href))
        else:
            continue
    return product_list


def add_dict(id_prod, name, reg_price, sale_price, url):
    sale = round(((reg_price - sale_price) / reg_price * 100), 2)
    dict_prod = ({'id': id_prod, 'squ': name, 'regular price': reg_price, 'sales price': sale_price, 'sale': sale,
                  'URL': url})
    return dict_prod


# vv_file = 'vv_data_parce.html'

# with open(vv_file, 'r', encoding='utf-8') as f:
    # f.write(data_f)
    # data = f.read()

# soup = BeautifulSoup(data, 'lxml')
# goods = soup.find_all("div", class_="ProductCard js-product-cart js-datalayer-catalog-list-item _woDeliv")


# squ_on_page = soup.find_all('span', class_='js-datalayer-catalog-list-position hidden')




def main():
    count_page = 1
    base_squ_on_page = 0
    while True:     # проверка количества товаров на странице (если меньше лимита, то выход)
        data_file = get_data_vv_price(count_page, base_url)
        soup = BeautifulSoup(data_file, 'lxml')
        squ_on_page = len(soup.find_all('div', class_='ProductCards__item ProductCards__item--col-lg-1-3'))
        goods = soup.find_all("div", class_="ProductCards__item ProductCards__item--col-lg-1-3")
        parce_squ_on_page(goods, base_url)
        if count_page == 1:
            base_squ_on_page = squ_on_page
        if base_squ_on_page == squ_on_page:
            count_page += 1
        else:
            # with open('sales_vv.txt', 'w', encoding='utf8') as total_f:
            #     total_f.write(product_list)
            break
    return pprint.pprint(product_list)

if __name__ == "__main__":
    main()
