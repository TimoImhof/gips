import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


def retrieve_country_urls():
    start_url = "https://www.worldtravelguide.net/country-guides/"
    page = requests.get(start_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all the links to the country guides
    links = soup.findAll('a')
    countries = []

    for link in links:
        href = link.get('href')
        if href is not None and href.startswith('/guides/'):
            countries.append(href)

    # create a csv file with the proper urls for each country
    base_url = 'https://www.worldtravelguide.net'
    with open('country_urls.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Continent', 'Country', 'URL'])
        for country_url in countries:
            # Try-except block to handle urls that don't follow the pattern
            try:
                continent, country = country_url.split('/')[2], country_url.split('/')[3]
                writer.writerow([continent, country, base_url + country_url])
            except:
                print('Error with url:', country_url)


def retrieve_country_info():
    # read the csv file with the country urls
    df = pd.read_csv('country_urls.csv')
    data_rows = []

    # for each country, retrieve the information
    for url in tqdm(df['URL']):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Find the div tag with the specific information needed
        target_div = soup.find('div', {'xmlns:fn': 'http://www.w3.org/2005/xpath-functions', 'itemprop': 'text'})

        # Extract all paragraph texts
        paragraphs = target_div.find_all('p')
        paragraph_texts = [p.get_text() for p in paragraphs]

        # Write the information to list
        splitted_url = url.split('/')
        continent, country = splitted_url[4], splitted_url[5]
        data_rows.append([continent, country, paragraph_texts])


    # Store the information in a csv file
    with open('worldtravelguide.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Continent', 'Country', 'Information'])

        for row in data_rows:
            continent, country, paragraph_texts = row
            writer.writerow([continent, country, paragraph_texts])

retrieve_country_info()