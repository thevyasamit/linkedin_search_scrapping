import pandas as pd 
import requests
from bs4 import BeautifulSoup
url = 'your_URL'
print(page) # if the output is 200 that means it is working
html_data= BeautifulSoup(page.content, 'html.parser')
print(html_data)
l = html_data.findAll(att = {'class': 'authentication-outlet'})
print(l)