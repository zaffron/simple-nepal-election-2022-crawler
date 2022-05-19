import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

URL = "https://localelection.ekantipur.com/pradesh-3/district-kathmandu/kathmandu?lng=eng"
r = requests.get(URL)

cb = 'Balendra Shah'
ck = 'Keshav Sthapit'
cs = 'Shirjana Shrestha'

soup = BeautifulSoup(r.content, 'html5lib')

t = PrettyTable(['Name', 'Party', 'Vote Count'])

nominee_list_group = soup.find('div', attrs = { 'class': 'nominee-list-group' })

first_column = nominee_list_group.select_one('.col-xl-6')

table = first_column.find_all('div', attrs = { 'class': 'candidate-list' })

leading_vote = 0
total_opposition_vote = 0

for row in table:
  name = row.select_one('.candidate-name').text
  if name == cb or name == ck or name == cs:
    party_name = row.select_one('.candidate-party-name').text
    vote_count = row.select_one('.vote-numbers').text
    if name == cb:
      leading_vote += int(vote_count)
    elif name == ck:
      leading_vote -= int(vote_count)
      total_opposition_vote += int(vote_count)
    else:
      total_opposition_vote += int(vote_count)
    t.add_row([name, party_name, vote_count])

print(t)

print(cb + " is leading " + ck + " by " + str(leading_vote))
print("Total vote of " + ck + " & " + cs + " : " + str(total_opposition_vote))
