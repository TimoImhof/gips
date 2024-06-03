import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import re


def retrieve_country_urls():
    start_url = "https://www.everyculture.com/index.html"
    page = requests.get(start_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all the links to the country guides
    links = soup.findAll('a')
    region_links = []
    base_url = 'https://www.everyculture.com/'
    pattern = re.compile(r'[A-Z][a-z]{0,1}-[A-Z][a-z]{0,1}/index.html')

    # filter the links to only include the A-Z links
    for link in links:
        href = link.get('href')
        if pattern.match(href):
            # assemble the full url
            full_link = base_url + href
            region_links.append(base_url + href)

    # Given the A-Z links, retrieve the links to the individual country guides
    country_urls = []
    for link in tqdm(region_links):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        tags = soup.findAll('a')

        base_url_parts = link.split('/')[:-1]
        # Join the components back into a URL
        base_url = '/'.join(base_url_parts) + '/'

        for tag in tags:
            if tag.text.startswith('Culture of'):
                country_url = base_url + tag.get('href')
                country_urls.append(country_url)

    # store the country urls in a csv file
    with open('country_urls.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['COUNTRY', 'URL'])
        for url in country_urls:
            country_name = url.split('/')[-1].split('.')[0]
            writer.writerow([country_name, url])


def retrieve_country_info():
    # read the csv file with the country urls
    df = pd.read_csv('country_urls.csv')
    data_rows = []

    # for each country, retrieve the information
    i = 0
    for url in tqdm(df['URL']):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get all <p> tags
        tags = soup.findAll('p')

        # extract the information
        country_text = []
        for entry in tags:
            country_text.append(entry.text)

        # rough cleaning of the text
        country_text = clean_text(country_text)

        country_name = df['COUNTRY'][i]
        data_rows.append([country_name, country_text])
        i += 1

    # store the information in a csv file
    with open('country_info.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['COUNTRY', 'INFO'])
        for row in data_rows:
            writer.writerow(row)


def clean_text(text_list):
    # Join the list into one string
    joined_text = ' '.join(text_list)

    # Replace newlines with spaces
    joined_text = joined_text.replace('\n', ' ')

    # Replace multiple spaces with a single space
    cleaned_text = re.sub(' +', ' ', joined_text).strip()

    return cleaned_text


retrieve_country_info()
