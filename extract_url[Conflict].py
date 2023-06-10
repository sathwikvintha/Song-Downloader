from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # already existing class
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # used as a method of finding objects from the browser page(,here,youtube website) ,
                                                                 # we are also supposed to gives "CLUES" (they are called attributes in html)
                                                                 # within the function , to web-scrape it precisely


from bs4 import BeautifulSoup

import time

from threading import Thread
from download_part import down_song

def get_url(song_name,widgets):

    chrome_options = Options() # new method added in selenium webdirver , that helps user change the default settings of selenium using the webdriver ,
                               # here we are instantiating chrome_options to the already-existing 'Options()' class

    chrome_options.headless = True # hides the browser window , so , it hence runs in the background and not showing us the browser window

    chrome_options.add_argument('--disable-gpu') #  temporary 'work-around' for a few bugs , not necessarily needed , but it's best to!

    chrome_options.add_argument("--log-level=3") # run it silently in the background

    driver = webdriver.Chrome(options=chrome_options) # here , we are assigning it to the driver we initiated

    driver.get('https://www.youtube.com/') # accesses the website thru chrome

    wait = WebDriverWait(driver,20) # this is used for the reason that , when u go to a website , it takes time to fully load the page properly ,
                                    # using this will help python script to wait executing until the page loads completely

    search_box = wait.until(EC.visibility_of_element_located( (By.NAME,'search_query') ) ) # the python script 'WAITS' , 'UNTIL' ,
                                                                                           # the expected_condition given inside is 'VISIBLE' for the web-scraping tool
                                                                                           # 'By' is the method used , using which the attributes are given in as clues
                                                                                           # syntax : ( By.<attribute_name> , '<value_of_attribute_as_given_in_the_html_source_page>' )

    search_box.send_keys(song_name) # Sending in values into the search_box object that we have just scraped.
                                    # song_name is the string that you have entered thru the main output screen.

    search_box.send_keys(Keys.RETURN) # just like how we press ENTER button in keyboard , similarly , we use Keys.RETURN thru the python script

    time.sleep(3) # we are simply waiting only for the reason that , after clicking enter in the previous line , we are waiting for the next page that appears to load fully

    article = driver.page_source # we are extracting the page's source code that we presently are in.

    driver.quit() # we no longer need the webdriver , so we are exiting from it

    soup = BeautifulSoup(article,'html.parser') # BeautifulSoup is ONLY being used for the purpose of parsing the page_source
                                                # syntax : BeautfulSoup(<content_you_want_to_parse> , <parsing_tool_you_wish_to_use> )
                                                # html.parser is what we will be using here to convert the html code into a conveniently organised human-readable form
                                                # this method is essential so that we can scrape content conveniently in the later code

    song= soup.find('a' , id = 'video-title') # from the 'soup' variable , we are finding a 'TAG' , this Tag will possess the unique address (stored in attribute form)
                                              # which identifies itself to the video  ,here, 'id' is one of the attribute the tag contains
                                              # syntax : soup.find( <tag-name> , <unique-attribute-name-that-the-tag-contains> = 'attribute's-value' )
                                              # this will ultimately scrape off the 'VERY-FIRST' tag in the source code which satisfies the given conditions.

    song_link = song.get('href') # 'href' is one of the atributes stored under the TAG we scraped above , hence , we are scraping the value of the 'href' attribute
                                 # as if it were a dictionary
                                 # syntax : song.get('<attribute-name>') .... in the html ,attributes and their corresponding values behave as key-value pairs , i.e. , like a dictionary.

    song_title = song['title']  # the syntax : song['<attribute-name>'] , also PERFORMS THE EXACT-SAME FUNCTION as the above line
                                # we are scraping the value of the 'title' attribute from the TAG , as a dictionary
                                # the 'title' attribute actually contains the name of the Youtube video
                                # we are scraping it only so that , we can give the same name as title to the downloaded mp3 audio

    song_title = song_title.strip() # we use strip() function so that we can remove any un-necessary wide spaces before the starting and after the ending of the song-title variable

    sub_url = 'https://www.youtube.com/'

    complete_url = sub_url + song_link # this will give out the proper url for the youtube video that we will use to extract the audio using youtube-dl

    Thread(target=down_song,args=(complete_url,song_title,widgets),daemon=True).start() # for now ,please IGNORE this.
