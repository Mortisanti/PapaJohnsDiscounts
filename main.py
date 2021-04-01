import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
url = 'https://betsapi.com/t/57721/MIA-Heat'

def get_latest_game():
    src = response.content
    soup = BS(src, 'lxml')
    tables = soup.find_all('table')
    rows = tables[1].find_all('tr')
    columns = rows[0].find_all('td')
    game_date = columns[1]['data-dt']
    outcome = columns[4].text
    return game_date, outcome

def format_and_parse_dates(game_date):
    today_string = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    todays_date_parsed = datetime.strptime(today_string, '%Y-%m-%dT%H:%M:%SZ')
    games_date_parsed = datetime.strptime(game_date, '%Y-%m-%dT%H:%M:%SZ')
    return todays_date_parsed, games_date_parsed

def get_seconds_since_win(todays_date_parsed, games_date_parsed):
    difference = abs(todays_date_parsed - games_date_parsed)
    seconds_since_win = (difference.days * 86400) + difference.seconds
    return seconds_since_win

def compare(outcome):
    thirty_six_hours = 129600
    if outcome == 'W':
        if get_seconds_since_win(todays_date_parsed, games_date_parsed) < thirty_six_hours:
            result = "The Miami Heat recently won! Promo code HEATWIN is valid."
    elif outcome == 'L':
        result = "The Miami Heat recently lost."
    elif outcome == '-':
        result = "The Miami Heat's latest game was postponed."
    elif outcome == 'D':
        result = "The Miami Heat's latest game ended in a draw."
    return result

response = requests.get(url, headers=headers)
if response.status_code == 200:
    game_date, outcome = get_latest_game()
    todays_date_parsed, games_date_parsed = format_and_parse_dates(game_date)
    print(compare(outcome))
else:
    print("No response from webpage.")