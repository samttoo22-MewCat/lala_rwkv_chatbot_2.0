import asyncio
import os
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import sys
import datetime
import time
import argparse
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


class WikiSearcher:
    def __init__(self):
        self.browser_executable_path = ""
        self.USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.driver = Driver(disable_gpu = False,
                             agent = self.USER_AGENT,
                             incognito = True,
                             headless=True,
                             browser = 'chrome',
                             #uc = True
                             )
        self.lock = asyncio.Lock()
        self.browser_executable_path = ""
        self.browser_executable_path = os.path.abspath("chromedriver.exe")
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        
        self.driver.get('https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5')
    
    def get_search_results(self, keyword, amount):
        result_links = []
        keyword = keyword.replace(' ', '+')
        search_link = f'https://zh.wikipedia.org/w/index.php?fulltext=1&search={keyword}&title=Special:%E6%90%9C%E7%B4%A2&ns0=1'
        self.driver.get(search_link)
        
        search_result_elements = self.driver.find_elements(By.XPATH, '//table[@class="searchResultImage"]/tbody/tr/td/a')
        for i in range(amount):
            result_link = search_result_elements[i].get_attribute('href')
            result_links.append(result_link)
        output = ''
        for link in result_links:
            output += self.scrap(link)
        return output
    
    def scrap(self, url):
        """抓取一篇維基百科文章的內文"""

        full_url = url
        try:
            r = requests.get(full_url, headers={'User-Agent': self.USER_AGENT})
        except requests.exceptions.ConnectionError:
            print("網路連線錯誤")
            return 0
        if r.status_code not in (200, 404):
            print("Request failed (code {})".format(r.status_code))
            return 0

        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find('div', {'id':'mw-content-text'})

        # add new related articles to queue
        # check if are actual articles URL
        for a in content.find_all('a'):
            href = a.get('href')
            if not href:
                continue
            if href[0:6] != '/wiki/':  # allow only article pages
                continue
            elif ':' in href:  # ignore special articles e.g. 'Special:'
                continue
            elif href[-4:] in ".png .jpg .jpeg .svg":  # ignore image files inside articles
                continue

        parenthesis_regex = re.compile('\(.+?\)')  # to remove parenthesis content
        citations_regex = re.compile('\[.+?\]')  # to remove citations, e.g. [1]

        # get plain text from each <p>


        p_list = content.find_all('p')
        output = ''
        for p in p_list:
            text = p.get_text().strip()
            text = parenthesis_regex.sub('', text)
            text = citations_regex.sub('', text)
            output += text
        output += '\n\n'
        return output
        
    


    