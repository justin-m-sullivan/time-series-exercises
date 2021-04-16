import pandas as pd
import numpy as np
from datetime import timedelta, datetime

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

def get_sales_stores_items_data():
    '''
    This function reads in the data from 
    a locally stored csv and retuns a dataframe
    named df
    '''
    df = pd.read_csv('sales_stores_items.csv')

    return df

def get_sales_total(df):
    '''
    This function creates a column for
    sales_total by multiplying the sale amount
    by the item price for each observation. 
    It returns a dataframe named df
    '''
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df

def prep_sales_store_items_df(df):
    '''
    This function read in the sale stores items dataframe
    and cleans it for analysis and returns the prepared 
    dataframe  named df
    '''

    #Drop extra unnamed column
    df.drop(columns={'Unnamed: 0'}, inplace=True)

    # Set the sale_date to datetime object
    df.sale_date = pd.to_datetime(df.sale_date)

    # Sort rows by the date and then set the index as that date
    df = df.set_index("sale_date").sort_index()

    #Create a column for month
    df['month'] = df.index.month_name()

    #Create a column for day of the week
    df['day_of_week'] = df.index.day_name()

    #create sales_total column
    df = df = get_sales_total(df)

    return df

