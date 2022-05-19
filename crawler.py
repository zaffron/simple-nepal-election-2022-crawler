import requests
from bs4 import BeautifulSoup

URL = "https://localelection.ekantipur.com/pradesh-3/district-kathmandu/kathmandu?lng=eng"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

results = []

nominee_list_group = soup.find('div', attrs = { 'class': 'nominee-list-group' })

first_column = nominee_list_group.select_one('.col-xl-6')

table = first_column.find_all('div', attrs = { 'class': 'candidate-list' })

for row in table:
  name = row.select_one('.candidate-name').text
  if name == 'Balendra Shah' or name == 'Keshav Sthapit' or name == 'Shirjana Shrestha':
    result = {}
    result['name'] = row.select_one('.candidate-name').text
    result['party_name'] = row.select_one('.candidate-party-name').text
    result['vote-numbers'] = row.select_one('.vote-numbers').text
    results.append(result)

print(results)
