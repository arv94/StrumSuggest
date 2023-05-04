## Import libraries
from bs4 import BeautifulSoup  ## BeautifulSoup library for scraping from the bs4 package
import requests ## Establish website connection using the requests library
import pandas as pd ## Use dataframes

## Webscrape data
k=1 ## Read the initial page of guitars
site = f'https://www.guitarguitar.co.uk/guitars/electric/page-{k}/'
resp = requests.get(site)
soup = BeautifulSoup(resp.text)

dic_list = []

print(resp)

while k < 82: ## Capture all 81 pages
    site = f'https://www.guitarguitar.co.uk/guitars/electric/page-{k}/'
    resp = requests.get(site)
    soup = BeautifulSoup(resp.text)
    print(site)

    ## Loop products tags to get link for each product page on home page
    for x in soup.find('div', class_="products").findAll('a'):
        ## hyperlink them
        site = 'https://www.guitarguitar.co.uk' + x.get('href')

        ## Access product page to scrape
        resp = requests.get(site)
        soup = BeautifulSoup(resp.text)


        ## Brand embedded in the a href of the second <li class="breadcrumb-item"> element - must iterate over all to extract brand
        brand = soup.find('ol', class_='breadcrumb').findAll('li')

        ## Map iteration to a list and extract just the brand element
        brand = [x.find('a').text for x in brand]
        brand = brand[1]

        ## Get model info
        model = soup.find('h1').text

        ## Not every product has a user rating or id so try-except branches used
        try:
            rating = soup.find('div', class_='product-reviews-heading').find('h4').find('strong').text
        except AttributeError:
            rating = None

        try:
            id = soup.find('div', class_='description-full').find('p').find('strong').text
        except AttributeError:
            id = None

        ## If price is discounted class_='product-price no-savings' will not exist and we will have to use a savings class
        try:
            guitar_dict['price'] = soup.find('p', class_='product-price no-savings').text
        except AttributeError:
            guitar_dict['price'] = soup.find('p', class_='product-price has-savings').text

        ## Create empty dict
        guitar_dict = {}


        ## Add our global variables (some may be None-type due to try-except branches)
        guitar_dict['brand'] = brand
        guitar_dict['model'] = model
        guitar_dict['link'] = site
        guitar_dict['rating'] = rating
        guitar_dict['id'] = id

        ## Scrape remaining specs from table
        specs = [x.text for x in soup.findAll('td')]

        # Add k-v pairs from specs list to dict
        for i in range(0, len(specs), 2):
            key = specs[i]
            ## IndexError occurred for some entries so this branch was needed
            try:
                value = specs[i+1]
            except IndexError:
                value = None
            guitar_dict[key] = value

        ## Add dictionary to dic list
        dic_list.append(guitar_dict)

    ## Move to next homepage to repeat
    k+=1

## Create and export DF

dfs = []
for d in dic_list:
    df = pd.DataFrame.from_dict(d, orient='index').T
    dfs.append(df)

## Concatenate into one df and export
guitar_df = pd.concat(dfs, ignore_index=True)
guitar_df.to_csv('guitars.csv', index=False)