from bs4 import BeautifulSoup
import requests
import csv

def Web_Scraping(url):
    soup = BeautifulSoup(url.content, 'html.parser')

    table = soup.find_all('tr')

    for data in table[2:23]:

        stats = data.find_all("td")

        position = stats[0].text
        team_name = stats[1].text
        played = stats[2].text
        goal_diff = stats[3].text
        points = stats[4].text

        output_file.writerow([position, team_name, played, goal_diff, points])

s = input("Enter League Name : ")

if s[0] == "l" or s[0] == "L":

    url = requests.get("https://www.goal.com/en-in/primera-divisi%C3%B3n/table/34pl8szyvrbwcmfkuocjm3r6t")

    output_file = csv.writer(open('laliga_standing.csv', 'w'))

    output_file.writerow(['Position', 'Team', 'Played', 'GD', 'Points'])

    Web_Scraping(url)

elif s[0] == "e" or s[0] == "E":

    url = requests.get("https://www.goal.com/en-in/premier-league/table/2kwbbcootiqqgmrzs6o5inle5")

    output_file = csv.writer(open('epl_standing.csv', 'w'))

    output_file.writerow(['Position', 'Team', 'Played', 'GD', 'Points'])

    Web_Scraping(url)

elif s[0] == "s" or s[0] == "S":

    url = requests.get("https://www.goal.com/en-in/serie-a/table/1r097lpxe0xn03ihb7wi98kao")

    output_file = csv.writer(open('seria_standing.csv', 'w'))

    output_file.writerow(['Position', 'Team', 'Played', 'GD', 'Points'])

    Web_Scraping(url)

elif s[0] == "b" or s[0] == "B":

    url = requests.get("https://www.goal.com/en-in/bundesliga/table/6by3h89i2eykc341oz7lv1ddd")

    output_file = csv.writer(open('bundesliga_standing.csv', 'w'))

    output_file.writerow(['Position', 'Team', 'Played', 'GD', 'Points'])

    Web_Scraping(url)