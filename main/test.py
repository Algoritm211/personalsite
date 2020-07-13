# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.keys import Keys
# import time
# from bs4 import BeautifulSoup
# import requests
# import re
#
# import openpyxl
#
# # options = webdriver.ChromeOptions()
# # options.add_argument('headless')
# # options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# # chrome_driver_binary = "/usr/local/bin/chromedriver"
# # driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
# #
# #
# # def kenex_parser():
# #     kenex_results = []
# #     i = 1
# #     while i <= 35:
# #         url = 'https://www.kenex.cz/kamery/strana-{number}'+'/'
# #         url = url.format(number=i)
# #         req = requests.get(url)
# #         html = req.content
# #         soup = BeautifulSoup(html, 'lxml')
# #         cams = soup.find_all('li', class_='product')
# #
# #         for x in cams:
# #             name = x.find('a', class_='p-name').find('span').get_text(strip=True).lower()
# #             availability = x.find('span', class_='p-cat-availability').get_text(strip=True).lower()
# #             if 'obj' in availability:
# #                 availability = 'Не на складе'
# #             else:
# #                 availability = 'На складе'
# #             href = x.find('a', class_='p-name').get('href').lower()
# #             kenex_results.append({'name': name, 'availability': availability, 'href': 'https://www.kenex.cz'+href})
# #
# #         i += 1
# #
# #     for i in kenex_results:
# #         i['name'] = i['name'].replace(',', '.')
# #     return kenex_results
# #
# #
# # def viakom_parser(url, number):
# #     viakom_results = []
# #     driver.get(url)
# #     elem = driver.find_element_by_tag_name('body')
# #     number_of_scrolls = number
# #
# #     while number_of_scrolls:
# #         elem.send_keys(Keys.PAGE_DOWN)
# #         time.sleep(0.85)
# #         number_of_scrolls -= 1
# #
# #     html = driver.page_source
# #     soup = BeautifulSoup(html, 'lxml')
# #     cams = soup.find_all('article', class_='product-item')
# #
# #     for x in cams:
# #         try:
# #             name = x.find('h2', class_='product-name').find('a').get_text(strip=True).lower()
# #
# #             try:
# #                 try:
# #                     availability = x.find('span', class_='stock').get_text(strip=True).lower()
# #                 except:
# #                     availability = x.find('span', class_='nostock').get_text(strip=True).lower()
# #             except:
# #                 availability = x.find('div', class_='product-stock').get_text(strip=True).lower()
# #
# #             if 'skladem' in availability:
# #                 availability = 'На складе'
# #             # elif 'objedn' in availability:
# #             #     availability = 'На заказ'
# #             # elif 'ext' in availability:
# #             #     availability = 'На дальнем складе'
# #             else:
# #                 availability = 'Не на складе'
# #
# #             href = x.find('h2', class_='product-name').find('a').get('href').lower()
# #             viakom_results.append({'name': name, 'availability': availability, 'href': 'https://www.viakom.cz'+href})
# #         except:
# #             pass
# #
# #     for i in viakom_results:
# #         i['name'] = i['name'].replace(',', '.')
# #     return viakom_results
# #
# #
# # def eurosat_parser():
# #     eurosat_results = []
# #     url = 'https://eshop.eurosat.cz/kategorie/3697/cctv_kamery/'
# #     driver.get(url)
# #     time.sleep(1)
# #     button_hikvision = driver.find_element_by_xpath('//*[@id="supplier_26900"]')
# #     button_hikvision.click()
# #     time.sleep(1)
# #     button_select = driver.find_element_by_xpath('//*[@id="pavg_grid_id_toppager_center"]/table/tbody/tr/td[1]/select')
# #     button_select.click()
# #     time.sleep(1.5)
# #     button_100 = driver.find_element_by_xpath('//*[@id="pavg_grid_id_toppager_center"]/table/tbody/tr/td[1]/select/option[5]')
# #     button_100.click()
# #     time.sleep(1)
# #
# #
# #     button_next = driver.find_element_by_class_name('ui-icon-seek-next')
# #     i = 1
# #     while i <= 3:
# #         time.sleep(2.5)
# #         button_next.click()
# #
# #         html = driver.page_source
# #         soup = BeautifulSoup(html, 'lxml')
# #         cams = soup.find_all('div', class_='grid-tile-main')
# #         for x in cams:
# #             try:
# #                 try:
# #                     try:
# #                         availability = x.find('div', class_='on-stock').get_text(strip=True).lower()
# #                     except:
# #                         availability = x.find('div', class_='no-on-stock').get_text(strip=True).lower()
# #                     if 'není' in availability:
# #                         availability = 'Не на складе'
# #                     else:
# #                         availability = 'На складе'
# #                 except:
# #                     availability = None
# #
# #                 if availability != None:
# #                     name = x.find('h3').find('a').get_text(strip=True).lower()
# #                     href = x.find('h3').find('a').get('href').lower()
# #                     eurosat_results.append({'name': name, 'availability': availability, 'href': 'https://eshop.eurosat.cz'+href})
# #             except:
# #                 pass
# #         i += 1
# #
# #     for i in eurosat_results:
# #         i['name'] = i['name'].replace(',', '.')
# #     return eurosat_results
# #
# #
# #
# # def viakom_comparison(kenex_parser_results):
# #     url_1 = 'https://www.viakom.cz/kategorie/kamery-ip/#vendors=43,93&page=1&onstock=0&tabselect=0&navdatafilter=1,1,0&sortpar=16&sortdir=asc&ajx=true&navdata=1,1&view=table&rows=12'
# #     number_1 = 165
# #     url_2 = 'https://www.viakom.cz/kamery/turbo-hd-a-4v1-kamery/n-1,2,0#view=table&rows=12&page=1&onstock=0&tabselect=0&navdatafilter=1,2,0&sortpar=16&sortdir=asc&ajx=true&navdata=1,2,0&vendors=43,93,38'
# #     number_2 = 100
# #     viakom_parser_results = viakom_parser(url_1, number_1) + viakom_parser(url_2, number_2)
# #     viakom_comparison_list = []
# #
# #     for k in kenex_parser_results:
# #         for v in viakom_parser_results:
# #
# #             kenex_replaced = k['name'].replace(' ', '').replace('.', '')
# #             viakom_replaced = v['name'].replace(' ', '').replace('.', '')
# #
# #             if viakom_replaced in kenex_replaced:
# #                 viakom_comparison_list.append({'name': k['name'], 'availability_kenex': k['availability'],\
# #                 'availability_viakom': v['availability'],'href_kenex': k['href'], 'href_viakom': v['href']})
# #     return viakom_comparison_list
#
#
# # def eurosat_comparison(kenex_parser_results):
# #     eurosat_parser_results = eurosat_parser()
# #     eurosat_comparison_list = []
# #
# #     for k in kenex_parser_results:
# #         for e in eurosat_parser_results:
# #
# #             if e['name'] == 'ds-2cc12d9t-a' or e['name'] == 'ds-2ce16h1t-it5' or e['name'] == 'ds-2ce16h5t-it3z' or e['name'] == 'ds-2ce56h5t-vpit3z':
# #                 eurosat_parser_results.remove(e)
# #             if e['name'] == 'ds-2ce56d8t-it3ze':
# #                 e['name'] = 'ds-2ce56d8t-it3ze 2.8'
# #
# #             kenex_replaced = k['name'].replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '')
# #             eurosat_replaced = e['name'].replace(' ', '').replace('(outdoor)', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '').replace('/', '').replace('_', '')
# #
# #             if eurosat_replaced in kenex_replaced:
# #                 eurosat_comparison_list.append(({'name': k['name'], 'availability_kenex': k['availability'],\
# #                 'availability_eurosat': e['availability'],'href_kenex': k['href'], 'href_eurosat': e['href']}))
# #     return eurosat_comparison_list
#
# import json
# def cam():
#     with open('data1.json', 'r') as file:
#         viakom = json.load(file)
#
#     with open('data2.json', 'r') as file:
#         eurosat = json.load(file)
#
#     with open('data0.json', 'r') as file:
#         kenex_parser_results = json.load(file)
#
#     results = []
#
#     for v in viakom:
#         for e in eurosat:
#
#             if v['name'] == e['name']:
#                 if v['availability_kenex'] == 'На складе' and v['availability_viakom'] == 'Не на складе' and e['availability_eurosat'] == 'Не на складе':
#                     results.append(({'name': v['name'], 'availability_kenex': 'На складе',\
#                     'availability_viakom': 'Не на складе', 'availability_eurosat': 'Не на складе',\
#                     'href_kenex': v['href_kenex'], 'href_viakom': v['href_viakom'], 'href_eurosat': e['href_eurosat']}))
#
#                 elif v['availability_kenex'] == 'Не на складе' and v['availability_viakom'] == 'На складе' and e['availability_eurosat'] == 'На складе':
#                     results.append(({'name': v['name'], 'availability_kenex': 'Не на складе',\
#                     'availability_viakom': 'На складе', 'availability_eurosat': 'На складе',\
#                     'href_kenex': v['href_kenex'], 'href_viakom': v['href_viakom'], 'href_eurosat': e['href_eurosat']}))
#
#                 elif v['availability_kenex'] == 'Не на складе' and v['availability_viakom'] == 'Не на складе' and e['availability_eurosat'] == 'На складе':
#                     results.append(({'name': v['name'], 'availability_kenex': 'Не на складе',\
#                     'availability_viakom': 'Не на складе', 'availability_eurosat': 'На складе',\
#                     'href_kenex': v['href_kenex'], 'href_viakom': v['href_viakom'], 'href_eurosat': e['href_eurosat']}))
#
#                 elif v['availability_kenex'] == 'Не на складе' and v['availability_viakom'] == 'На складе' and e['availability_eurosat'] == 'Не на складе':
#                     results.append(({'name': v['name'], 'availability_kenex': 'Не на складе',\
#                     'availability_viakom': 'На складе', 'availability_eurosat': 'Не на складе',\
#                     'href_kenex': v['href_kenex'], 'href_viakom': v['href_viakom'], 'href_eurosat': e['href_eurosat']}))
#
#             else:
#                 if v['availability_kenex'] != v['availability_viakom']:
#                     results.append(({'name': v['name'], 'availability_kenex': v['availability_kenex'],\
#                     'availability_viakom': v['availability_viakom'], 'availability_eurosat': 'Нет в продаже',\
#                     'href_kenex': v['href_kenex'], 'href_viakom': v['href_viakom']}))
#
#                 elif e['availability_kenex'] != e['availability_eurosat']:
#                     results.append(({'name': e['name'], 'availability_kenex': e['availability_kenex'],\
#                     'availability_eurosat': e['availability_eurosat'], 'availability_viakom': 'Нет в продаже',\
#                     'href_kenex': e['href_kenex'], 'href_eurosat': e['href_eurosat']}))
#
#     results.sort(key = lambda n: n['name'])
#     with open('cam.json', 'w') as file:
#         json.dump(results, file, indent=2)
#     return len(results)
#
# print(cam())
#
#
#
# # def main():
# # if __name__ == '__main__':
# #     main()

import json
def viakom_comparison(kenex_parser_results, viakom):
    url_1 = 'https://www.viakom.cz/kategorie/kamery-ip/#vendors=43,93&page=1&onstock=0&tabselect=0&navdatafilter=1,1,0&sortpar=16&sortdir=asc&ajx=true&navdata=1,1&view=table&rows=12'
    number_1 = 165
    url_2 = 'https://www.viakom.cz/kamery/turbo-hd-a-4v1-kamery/n-1,2,0#view=table&rows=12&page=1&onstock=0&tabselect=0&navdatafilter=1,2,0&sortpar=16&sortdir=asc&ajx=true&navdata=1,2,0&vendors=43,93,38'
    number_2 = 100
    viakom_parser_results = viakom
    viakom_comparison_list = []

    for k in kenex_parser_results:
        for v in viakom_parser_results:

            kenex_replaced = k['name'].replace(' ', '').replace('.', '')
            viakom_replaced = v['name'].replace(' ', '').replace('.', '')

            if viakom_replaced in kenex_replaced:
                viakom_comparison_list.append({'name': k['name']})
    i = 0
    c = 0
    import re
    print(len(viakom_comparison_list))
    # print(viakom_comparison_list[809]['name'])

    while i <= len(viakom_comparison_list) - 1:
        if "camvia" in viakom_comparison_list[i]['name']:
            viakom_comparison_list.pop(i)
            c += 1
            continue

        i += 1

    # for i in range(len(viakom_comparison_list)-1):
    #     try:
    #         if "camvia" in viakom_comparison_list[i]['name']:
    #             count += 1
    #
    #             viakom_comparison_list.pop(i)
    #     except:
    #         pass
    print(len(viakom_comparison_list))
    print(c)
    return viakom_comparison_list


with open('data0.json', 'r') as file:
        kenex_parser_results = json.load(file)

with open('data1.json', 'r') as file:
        viakom = json.loads(file.read())
        print(len(viakom))

a = viakom_comparison(viakom, kenex_parser_results)
from pprint import pprint

pprint(a)
# with open('cam.json', 'w') as file:
#         json.dump(a, file, indent=2)

# a = ['camvia ', 'df', 'camvia sdlfkm']
#
# for i in range(len(a)-1):
#     if 'camvia' in a[i]:
#         a.pop(i)
#
# print(a)


