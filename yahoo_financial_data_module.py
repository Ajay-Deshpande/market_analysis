import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance

class Ticker:
    def __init__(self,ticker):
        self.ticker = ticker
    def get_stats_page_data(self):
        statistic_page = "https://in.finance.yahoo.com/quote/{0}/key-statistics?p={0}".format(self.ticker.upper())
        content = requests.get(statistic_page).content
        stats_page_dfs = pd.read_html(content)
        stats_page_dfs = pd.concat(stats_page_dfs)
        stats_page_dfs.columns = ['field_name','value']
        return stats_page_dfs.pivot(columns='field_name').fillna(method='bfill').iloc[0]

    def get_historical_stock_price(self,period = '1d', interval = '5m'):
        ticker_data = yfinance.Ticker(self.ticker)
        return ticker_data.history(period = period,interval = interval)

    def get_profile_data(self):
        prof_query = "https://in.finance.yahoo.com/quote/{0}/profile?p={0}".format(self.ticker)
        soup = BeautifulSoup(requests.get(prof_query).content)
        profile_data = list(soup.find_all('div',class_="asset-profile-container")[0].findChildren('p')[1].stripped_strings)
        profile_data = dict(zip(profile_data[::3],profile_data[2::3]))
        return profile_data

    def get_financial_data(self, data_classes = 'all'):
        query = "https://in.finance.yahoo.com/quote/{0}/{1}?p={0}"
        mapper = {'income_statement':'financials','cash_flow':'cash-flow','balance_sheet':'balance-sheet'}
        data_classes = mapper.get(data_classes,', '.join(mapper.values()))
        def scrape_data(query):
            soup = BeautifulSoup(requests.get(query).text)
            temp = soup.find_all(id='Col1-1-Financials-Proxy')[0]
            temp = list(list(temp.children)[0].children)[2]
            temp = list(temp.childGenerator())[0]
            temp = list(temp.childGenerator())[0]
            temp = list(temp.childGenerator())
            header = list(temp[0].stripped_strings)
            temp = temp[1]
            temp = list(temp.stripped_strings)
            final_list = []
            val_list = []
            for ind in range(len(temp)):
                try:
                    if temp[ind] == '-':
                        val_list.append(temp[ind])
                        continue
                    val_list.append(float(temp[ind].replace(',','')))
                except:
                    if val_list:
                        final_list.append(val_list + [np.NaN]*(len(header) - len(val_list)))
                    val_list = [temp[ind]]
            return pd.DataFrame(final_list,columns=header)
        data_list = []
        for data_class in data_classes.split(', '):
            data_list.append(scrape_data(query.format(self.ticker,data_class)))
        return data_list


# ticker = "INFY.NS"
# infy_stats = get_stats_page_data('INFY.NS')
# infy_history = get_historical_stock_price(ticker)
# profile_data = get_profile_data(ticker)
# financials = get_financial_data(ticker)