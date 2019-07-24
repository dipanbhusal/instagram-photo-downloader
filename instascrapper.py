import requests, time, shutil
import os
from selenium import webdriver
def instaScrapper(url):
    #Opens Instagram URL
    browser.get(url)
    
    #Scroll down until all images are loaded on the screen
    SCROLL_PAUSE_TIME = 5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #Get all img elements    
    imgelems = browser.find_elements_by_class_name('FFVAD')

    i=0
    path = os.path.join('pictures') #path for downloaded pictures
    for imgelem in imgelems:
	
        imglink = imgelem.get_attribute('src')
        response = requests.get(imglink, stream = True)
        with open(path+str(i)+'.png','wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        
        i+=1
        print(i)

#Opens the browser (Make sure you have the Chrome webdriver executable listed in your Environment Variable Path
        
browser = webdriver.Chrome('###') #Specify your own Chrome Driver Path here
time.sleep(5)
user_name = input('Enter the instagram username: ')
url = 'https://www.instagram.com/' + user_name

time.sleep(30)
#Enter username password after Instagram opens.
instaScrapper(url)
    
