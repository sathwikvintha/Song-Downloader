from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import sqlite3


driver = webdriver.Chrome()

driver.get('https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg')
time.sleep(3)
page_source = driver.page_source

soup = BeautifulSoup(page_source,'html.parser')
songs = soup.find('ol','tracklist')
song_list = soup.find_all('div','tracklist-name ellipsis-one-line')

in_list = []
for i in range(len(song_list)):
    in_list.append((i+1,song_list[i].text))

driver.get('https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF')
time.sleep(3)
page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source,'html.parser')
songs = soup.find('ol','tracklist')
song_list = soup.find_all('div','tracklist-name ellipsis-one-line')

gb_list = []
for i in range(len(song_list)):
    gb_list.append((i+1,song_list[i].text))


conn = sqlite3.connect('songs.db')

c = conn.cursor()

c.execute('create table if not exists india (id integer ,song_name text)')

conn.commit()

c.execute('create table if not exists global (id integer ,song_name text)')

conn.commit()

c.executemany('insert into india values (?,?)',in_list)

c.executemany('insert into global values (?,?)',gb_list)

conn.commit()
