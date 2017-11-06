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


    #for dom in soup.find_all('section', class_='section-offer-title'):
    title = soup.find("h1", {"itemprop": "name"}).text.encode("utf-8")

    #print type(title), title

    price = soup.find("strong", class_='box-price-value').text.encode("utf-8")
    #price = dom.find("strong", class_='box-price-value').text.encode("utf-8")
    #print price

    #phone = soup.find("span", class_="phone-number").text
    #print phone

    pelna_cena = soup.find("li", class_="param_price")
    if pelna_cena is None:
        pelna_cena = 'BRAK DANYCH'
        print pelna_cena
    else:
        pelna_cena = pelna_cena.text.encode("utf-8")
        #print pelna_cena

    powierzchnia = soup.find("li", class_="param_m")
    if powierzchnia is None:
        powierzchnia = 'BRAK DANYCH'
        print powierzchnia
    else:
        powierzchnia = powierzchnia.text.encode("utf-8")
        #print powierzchnia

    powierzchnia_dzialki = soup.find("li", class_="param_terrain_area")
    if powierzchnia_dzialki is None:
        powierzchnia_dzialki = 'BRAK DANYCH'
        print powierzchnia_dzialki
    else:
        powierzchnia_dzialki = powierzchnia_dzialki.text.encode("utf-8")
        #print powierzchnia_dzialki

    pietra = soup.find("li", class_="param_floors_num")
    if pietra is None:
        pietra = 'BRAK DANYCH'
        print pietra
    else:
        pietra = pietra.text.encode("utf-8")
        #print pietra

    #liczba_pieter = soup.find("li", class_="param_floors_num").text
    #print liczba_pieter

    #course=[title.decode("utf-8"), short_desc.decode("utf-8"), netto_float, brutto_float]
    for row in courses_list:
        course = [title, pelna_cena, powierzchnia, powierzchnia_dzialki, pietra]
        courses_list.append(course)

    print courses_list




    with open('file.csv', 'wb') as f:
         w = csv.writer(f)
         w.writerow(["Title", "Pelna_cena", "Powierzchnia", "Powierchnia_dzialki", "Ilosc_pieter"])
         w.writerows(courses_list)
         #for row in courses_list:
         #    w.writerow(row)


def main_spider(max_page):

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

main_spider(3)

