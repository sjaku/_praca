# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup, Tag
import csv
import pyodbc
import urllib
import os

url_otodom = "https://www.otodom.pl/sprzedaz/dom/poznan/"

r = requests.get(url_otodom)
soup = BeautifulSoup(r.content, "html.parser")


def get_max_category_pages(url_otodom):
    r = requests.get(url_otodom)
    soup = BeautifulSoup(r.content, "html.parser")

    #main_container = soup.find("div", class_="col-md-content")
    #print main_container

    pageCounter = soup.find("input", {"id": "pageParam"}).text
    pageCounter = int(pageCounter.split("\t")[4])
    #print pageCounter
    return pageCounter

#get_max_category_pages(url_otodom)


def get_data_save_CSV(url):

    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.content, "html.parser")

    #os.remove(destinationPath+csvfile)
    courses_list = []
    global pokoje, rok_budowy, rodzaj_zabudowy, stan_wykonczenia, okna, polozenie

    for dom in soup.find_all('div', class_='article-offer'):
        #print dom
        title = dom.find("h1").text.encode("utf-8")
        #print title
        price = dom.find("strong", class_="box-price-value").text.encode("utf-8")
        #print price
        ul_main_list = dom.find("ul", class_="main-list")
        #print ul_main_list

        li_price_full = dom.find("li", class_="param_price").strong.text.encode("utf-8")
        print li_price_full
        li_param_area_house = dom.find("li", class_="param_m").strong.text.encode("utf-8")
        print li_param_area_house
        li_param_area = dom.find("li", class_="param_terrain_area")
        if li_param_area is None:
            li_param_area = 'n/a'
            print li_param_area
        else:
            li_param_area = li_param_area.strong.text.encode("utf-8")
            print li_param_area

        li_floors = dom.find("li", class_="param_floors_num")
        if li_floors is None:
            li_floors = 'n/a'
            print li_floors
        else:
            li_floors = li_floors.strong.text.encode("utf-8")
            print li_floors

        price = float(li_price_full.rsplit(" ", 1)[0].replace(" ", ""))
        #print type(price), price
        area = float(li_param_area_house.rsplit(" ",1)[0].replace(" ","").replace(",","."))
        #print area
        price_meter = round(price/area,2)
        #print price_meter

        sub_list = dom.find("ul", class_="sub-list")
            #li = sub_list.findAll("li")[1]

        li_rynek = sub_list.find_all('li')
        for result in li_rynek:
            if result.text.startswith("Rynek:"):
                rynek = result.text.split(" ")[1]
                rynek = rynek.encode("utf-8")
                print "Rynek:", rynek

        li_pokoje = sub_list.find_all('li')
        for result in li_pokoje:
            if result.text.startswith("Liczba pokoi"):
                pokoje = result.text.rsplit(" ",1)[1]
                print "Pokoje:", pokoje

        li_rok_budowy = sub_list.find_all('li')
        for result in li_rok_budowy:
            if result.text.startswith("Rok budowy"):
                rok_budowy = result.text.split(":")[1]
                print "Rok budowy:", rok_budowy

        li_rodzaj_zabudowy = sub_list.find_all('li')
        for result in li_rodzaj_zabudowy:
            if result.text.startswith("Rodzaj zabudowy:"):
                rodzaj_zabudowy = result.text.split(":")[1]
                rodzaj_zabudowy = rodzaj_zabudowy.encode("utf-8")
                print "Rodzaj zabudowy:", rodzaj_zabudowy

        li_stan_wykonczenia = sub_list.find_all('li')
        for result in li_stan_wykonczenia:
            if result.text.startswith("Stan wyko"):
                stan_wykonczenia = result.text.split(":")[1]
                stan_wykonczenia = stan_wykonczenia.encode("utf-8")
                print "Stan wykończenia:", stan_wykonczenia

        li_okna = sub_list.find_all('li')
        for result in li_okna:
            if result.text.startswith("Okna:"):
                okna = result.text.split(":")[1]
                okna = okna.encode("utf-8")
                print "Okna:", okna


        li_polozenie = sub_list.find_all('li')
        for result in li_polozenie:
            if result.strong.text.endswith("enie:"):
                polozenie = result.text.split(":")[1]
                #print "p:", polozenie
                polozenie = polozenie.encode("utf-8")
                print "Położenie:", polozenie



        course = [title, li_price_full, price_meter, li_param_area_house, li_param_area, li_floors, rynek, pokoje, rok_budowy,
                   rodzaj_zabudowy, stan_wykonczenia, okna, polozenie  ]



    courses_list.append(course)

    print courses_list


    with open('house_list.csv', 'ab') as f:
        w = csv.writer(f)
        #w.writerow(["Title", "Pelna_cena", "Powierzchnia", "Powierchnia_dzialki", "Ilosc_pieter"])
        for row in courses_list:
            w.writerow(row)
        #w.writerows(courses_list)
        #for row in courses_list:
        #    w.writerow(row)



def main_spider(max_page):
    os.remove('house_list.csv')
    for num in range(1,max_page):
        #utworzenie nowego stringa przechowujacego ziterowane adresy stron do przetworzenia
        url_otodom_new = url_otodom + '?page=' + str(num)

        print url_otodom_new

        source_code = requests.get(url_otodom_new)
        soup = BeautifulSoup(source_code.content, "html.parser")
        count = 0
        for link in soup.find_all('article', class_='offer-item'):
            href = link.findAll('a')[0].get('href')
            print href

            count = count + 1

            #zapisywanie danych pliku csv
            get_data_save_CSV(href)

            #zapisywanie zdjec z funkcji
            #extract_product_images(href)


        print "Pobrano produktow : ", count

main_spider(10)

