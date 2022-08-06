import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class ht_laz_crawl:
    def __init__(self, driver, link):
        
        self.driver = driver
        self.XPATH = {'title': '//span[@class="title"]',\
                        'load-more': '//a[@class="button J_LoadMoreButton"]'}
        self.link = link
        self.wait = random.randint(15, 20)
        
    def open_browser(self):
        self.driver.get(self.link)
        return None

    def close_browser(self):
        self.driver.quit()
        return None
    
    def get_title(self):
        lst = []
        titles = self.driver.find_elements(By.XPATH, self.XPATH['title'])
        for t in titles:
            lst.append(t.text)
        return lst
    
    def load_more(self):        
        load_more = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, self.XPATH['load-more'])))
        while True:
            try:
                load_more.click()
                print('click')
                time.sleep(self.wait)
            except:
                print('Done clicking')
                break



