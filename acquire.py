import pandas as pd
import os
import requests

def get_items_df(cached=False):
    '''
    This function creates a request
    from a REST API at https://python.zach.lol/api/v1/items
    and transforms the response into a dataframe
    named: items
    '''
    if cached == False:
        #create the empty list which will be appended with data with each iteration 
        items_list = []

        #define the url from where the data is stored
        url = "https://python.zach.lol/api/v1/items"

        #define the response by the request
        response = requests.get(url)

        #convert the response to json
        data = response.json()

        #define the number of pages based on the max_page value 
        n = data['payload']['max_page']

        #Create the loop to iterate through each page starting with page 1  and ending on page n + 1 
        for i in range(1, n+1):

            #define the new url returned for next page
            new_url = url+"?page="+str(i)

            #define the response requested
            response = requests.get(new_url)

            #convert response to json
            data = response.json()

            #create the variable to hold the items returned from the response
            page_items = data['payload']['items']

            #add the items from the page to the items list and continue to iterate through n pages
            items_list += page_items
        
        #Create a dataframe of the items_list that now hold all the items from all pages
        items = pd.DataFrame(items_list)

        #convert to a local csv to save time for future use
        items.to_csv('items.csv')

    else:
        #should the csv already exists locally, just read it in
        items = pd.read_csv('items.csv', index_col=0)

    
    return items


def get_stores_df(cached=False):
    '''
    This function creates a request
    from a REST API at https://python.zach.lol/api/v1/stores
    and transforms the json response into a dataframe
    named: stores
    '''
    if cached == False:
        #create the empty list which will be appended with data with each iteration 
        stores_list = []

        #define the url from where the data is stored
        url = "https://python.zach.lol/api/v1/stores"

        #define the response by the request
        response = requests.get(url)

        #convert the response to json
        data = response.json()

        #define the number of pages based on the max_page value 
        n = data['payload']['max_page']
        
        for i in range(1, n+1):
            new_url = url+"?page="+str(i)
            response = requests.get(new_url)
            data = response.json()
            page_stores = data['payload']['stores']
            stores_list += page_stores
            
        stores = pd.DataFrame(stores_list)
        stores.to_csv('stores.csv')
    else:
        stores = pd.read_csv('stores.csv', index_col=0)
    
    return stores


def get_sales_df(cached=False):
    '''
    This function requests data
    from a REST API at https://python.zach.lol/api/v1/sales
    and transform the json response into a
    dataframe named: sales
    '''
    if cached == False:

        sales_list = []
        url = "https://python.zach.lol/api/v1/sales"
        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']
        
        for i in range(1, n+1):
            new_url = url+"?page="+str(i)
            response = requests.get(new_url)
            data = response.json()
            page_sales = data['payload']['sales']
            sales_list += page_sales
            
        sales = pd.DataFrame(sales_list)
        sales.to_csv('sales.csv')

    else: 
        sales = pd.read_csv('sales.csv', index_col=0)

    return sales


def get_sales_stores_items(cached=False):
    '''
    This function reads in three csv files (stores, items, sales)
    and joins them onto one dataframe returned as sales_stores_items
    '''
    if cached == False: 
        #Get Sales df
        sales = get_sales_df(cached=True)

        #Get Stores df
        stores = get_stores_df(cached=True)

        #Get Items df
        items = get_items_df(cached=True)

        #rename store column in sales to store_id and item to item_id
        sales.columns = ['item_id', 'sale_amount', 'sale_date', 'sale_id', 'store_id']

        #join sales and stores dataframe
        sales_stores = pd.merge(sales, stores, how='inner', on='store_id')

        #join items to sales_stores
        sales_stores_items = pd.merge(sales_stores, items, how='inner', on='item_id')

        #convert to local csv
        sales_stores_items.to_csv('sales_stores_items.csv')

    else:
        #read in the sales_stores _items csv stored locally
        sales_stores_items = pd.read_csv('sales_stores_items.csv', index_col=0)

    return sales_stores_items

def get_open_power_data():
    '''
    This function reads in data for electrcity consumption, wind power 
    production, and solar power production for 2006 - 2017 in Germany
    and returns the data in a single dataframe named df
    '''
    base_url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
    df = pd.read_csv(base_url)
    
    return df



