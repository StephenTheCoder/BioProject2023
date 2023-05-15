import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

x = input("What is the sequence? ")

# Have Python code get the data
driver = webdriver.Firefox()

# driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")

driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?QUERY=" + x + "&DATABASE=nt&PROGRAM=blastnt&CMD=put")

QUERY = + x + "&DATABASE=nt&PROGRAM=blastn&CMD=Put"

"RID=" + requestID + "CMD=Get"

search_box = driver.find_element("name", QUERY)

search_box.send_keys(x)


search_box.send_keys(Keys.RETURN)
result_url = driver.current_url


# Getting info from URL

url = "result_url"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table")

df = pd.read_html(str(table))[0]

df_sorted = df.sort_values(by="E value", ascending=True).head(5)

print("The five most similar animals are ")
print(df_sorted.loc[:, 'scientific name'])


# Compare 2 DNA sequences and make a cladogram 