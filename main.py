import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

url = 'https://blaze.com/pt/games/crash'

option = Options()
option.headless = False
driver = webdriver.Chrome(options=option)

driver.get(url)
driver.quit()