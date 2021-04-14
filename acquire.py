import pandas as pd
import requests

def get_items_df():
    '''
    This function creates a request
    from a REST API at https://python.zach.lol/api/v1/items
    and transforms the response into a dataframe
    named: items
    '''
    items_list = []
    url = "https://python.zach.lol/api/v1/items"
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload']['items']
        items_list += page_items
        
    items = pd.DataFrame(items_list)
    
    return items


def get_stores_df():
    '''
    This function creates a request
    from a REST API at https://python.zach.lol/api/v1/stores
    and transforms the json response into a dataframe
    named: stores
    '''
    stores_list = []
    url = "https://python.zach.lol/api/v1/stores"
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_stores = data['payload']['stores']
        stores_list += page_stores
        
    stores = pd.DataFrame(stores_list)
    
    return stores


def get_sales_df():
    '''
    This function requests data
    from a REST API at https://python.zach.lol/api/v1/sales
    and transform the json response into a
    dataframe named: sales
    '''
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
    
    return sales