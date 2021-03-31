#TODO Check date of last win, compare to today's date (give or take a day or two)
import requests
from bs4 import BeautifulSoup as BS
from requests.models import Response
from datetime import datetime

"""
# JUST REALIZED THIS WAS USELESS. Use built-in method to determine difference between dates, compare result to 1 or 2 day difference
# Get today's date; do not format as to keep integer values
today = datetime.now()
print(f'{today.month}/{today.day}')

# Get last win date, convert to datetime object so that the values are integers
last_win_date = '03/29 23:30'
last_win_date_converted = datetime.strptime(last_win_date, '%m/%d %H:%M')
print(f'{last_win_date_converted.month}/{last_win_date_converted.day}')
"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
url = 'https://betsapi.com/t/57721/MIA-Heat'

def get_latest_game():
    src = response.content
    soup = BS(src, 'lxml')
    tables = soup.find_all('table')
    rows = tables[1].find_all('tr')
    columns = rows[0].find_all('td')
    latest_date = columns[1]['data-dt']
    # Outcome can either be W (win), L (loss), - (postponed), or D (draw)
    latest_outcome = columns[4].text
    return latest_date, latest_outcome

def convert(latest_date):
    today = datetime.now().strftime("%Y-%m-%d")
    latest_date_formatted = datetime.strptime(latest_date, '%Y-%m-%dT%H:%M:%SZ')
    latest_date_converted = latest_date_formatted.strftime("%Y-%m-%d")
    return latest_date_converted

def compare():
    return

# Maybe check response headers too
response = requests.get(url, headers=headers)
if response.status_code == 200:
    latest_date, latest_outcome = get_latest_game()
    latest_date_converted = convert(latest_date)
else:
    print("No response from webpage.")