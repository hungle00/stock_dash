import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#from format import format


# This will keep tickers + gics industries & sub industries
def save_sp500_stocks_info():
    print("Getting SP500 stocks info from wikipedia")
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    stocks_info=[]
    tickers = []
    securities = []
    gics_industries = []
    gics_sub_industries = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        security = row.findAll('td')[1].text
        gics_industry = row.findAll('td')[3].text
        gics_sub_industry = row.findAll('td')[4].text

        tickers.append(ticker.lower().replace(r"\n", " "))
        securities.append(security)
        gics_industries.append(gics_industry.lower())
        gics_sub_industries.append(gics_sub_industry.lower())
    
    stocks_info.append(tickers)
    stocks_info.append(securities)
    stocks_info.append(gics_industries)
    stocks_info.append(gics_sub_industries)
    
    stocks_info_df = pd.DataFrame(stocks_info).T
    stocks_info_df.columns=['tickers','security','gics_industry','gics_sub_industry']
    stocks_info_df['seclabels'] = 'SP500'
    stocks_info_df['labels'] = stocks_info_df[['tickers','security', 'gics_industry','gics_sub_industry','seclabels']].apply(lambda x: ' '.join(x), axis=1)

    # Create a list of dict based on tickers and labels
    dictlist = []
    for index, row in stocks_info_df.iterrows():
        dictlist.append({'value':row['tickers'], 'label':row['labels']})

    return dictlist

'''
def save_stocks_to_csv():
    import csv
    csv_columns = ['value', 'label']
    
    dict_data = save_sp500_stocks_info()
    csv_file = "stocks.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
'''
#save_stocks_to_csv()
'''
# This will keep tickers from russell
def save_russell_info():
    print("Getting russell stocks info")

    dfrussel=pd.read_csv('C:/Users/vintatan/Desktop/Investment/RussellandData.csv',index_col='Symbol')
    dfrussel['tickers'] = dfrussel.index.str.upper()
    dfrussel['tickers'] = dfrussel['tickers'].replace(r"\n", " ")
    dfrussel['security'] = dfrussel.Description.str.title()
    dfrussel['gics_industry'] = dfrussel.Sector.str.lower()
    dfrussel['gics_sub_industry'] = dfrussel.Industry.str.lower()
    dfrussel['seclabels'] = 'RUSSELL'

    dfrussel['labels'] = dfrussel[['tickers','security','gics_industry','gics_sub_industry','seclabels']].apply(lambda x: ' '.join(x), axis=1)

    dictlist = []
    for index, row in dfrussel.iterrows():
        dictlist.append({'value':row['tickers'], 'label':row['labels']})
    return dictlist
'''
# self append
def save_self_stocks_info():
    print("Adding own list of stocks info")

    dictlist = []

    dictlist.append({'value':'ajbu', 'label':'AJBU Keppel DC Reit Data REITS SA'})
    dictlist.append({'value':'gme', 'label':'GME Game Stop Corp SA'})
    dictlist.append({'value':'aeg', 'label':'AEG Aegon Insurance SA'})
    dictlist.append({'value':'ntic', 'label':'NTIC Northern Technologies International SA'})
    dictlist.append({'value':'sq', 'label':'SQ Square SA'})
    dictlist.append({'value':'kbsty', 'label':'Kobe steel'})
    dictlist.append({'value':'NESN', 'label':'Nestle'})
    dictlist.append({'value':'BN', 'label':'Danone'})
    dictlist.append({'value': 'DATA', 'label': 'Tableau Software Data Visualization'})



    return dictlist
