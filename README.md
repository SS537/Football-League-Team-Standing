# Football-League-Team-Standing

## Description

This is a simple web scraping project where you can find a football league team standing. It’s easy to use, you have to just enter the league name that you like and you will get your favorite league's team standing.

The project will run through goal.com and scrap data and save it in a CSV file. You can only get La liga, EPL, Serie A and Bundesliga point table.

## Requirement

Python 3.6+

## Installation

Install  requests and BeautifulSoup libraries
```bash
pip install beautifulsoup4
pip install requests
```
## How to Use
Just run the program 

```bash
python scraper.py
```
In the input enter any league name. After the scraping is finished the team standing will save in a CSV file by their league name (example: EPL point table will be saved like this "epl_standing.csv")
