import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

URL = "https://localelection.ekantipur.com/pradesh-3/district-kathmandu/kathmandu?lng=eng"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

t = PrettyTable(['Name', 'Party', 'Vote Count'])

nominee_list_group = soup.find('div', attrs = { 'class': 'nominee-list-group' })

first_column = nominee_list_group.select_one('.col-xl-6')

table = first_column.find_all('div', attrs = { 'class': 'candidate-list' })

for row in table:
  name = row.select_one('.candidate-name').text
  if name == 'Balendra Shah' or name == 'Keshav Sthapit' or name == 'Shirjana Shrestha':
    name = row.select_one('.candidate-name').text
    party_name = row.select_one('.candidate-party-name').text
    vote_count = row.select_one('.vote-numbers').text
    t.add_row([name, party_name, vote_count])

print(t)
