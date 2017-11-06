__author__ = 'sjaku'
import requests
from bs4 import BeautifulSoup, Tag
import csv
import pyodbc
import urllib
import os

url = "https://www.otodom.pl/oferta/dom-w-poznaniu-cena-tylko-539-000zl-ID3qyMk.html"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


#for dom in soup.find_all('section', class_='section-offer-title'):
title = soup.find("h1", {"itemprop": "name"}).text
print title

price = soup.find("strong", class_='box-price-value no-estimates').text
print price

phone = soup.find("span", class_="phone-number").text
#print phone

pelna_cena = soup.find("li", class_="param_price").text
print pelna_cena

powierzchnia = soup.find("li", class_="param_m").text
p = powierzchnia.split(" ")[1]
print powierzchnia

powierzchnia_dzialki = soup.find("li", class_="param_terrain_area").text
print powierzchnia_dzialki

liczba_pieter = soup.find("li", class_="param_floors_num").text
print liczba_pieter

main_list = soup.find("ul", class_="main-list")
#print main_list




