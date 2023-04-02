import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
import datetime

# Set up the URLs we want to scrape
urls = ['https://www.theverge.com']

# Create a function to scrape each article on the page
def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find('article')
    if article:
        headline = article.find('h2', {'class': 'c-entry-box--compact__title'}).text.strip()
        link = article.find('a', {'class': 'c-entry-box--compact__image-wrapper'})['href']
        author = article.find('a', {'class': 'c-byline__author-name'}).text.strip()
        date = article.find('time')['datetime']
        return (headline, link, author, date)
    else:
        return None

# Scrape all the articles on each URL and store the results in a list
articles = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_links = soup.find_all('a', {'class': 'c-entry-box--compact__image-wrapper'})
    for link in article_links:
        article = scrape_article(link['href'])
        if article:
            articles.append(article)

# Create a CSV file with the results
filename = datetime.datetime.now().strftime("%d%m%Y") + "_verge.csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "URL", "headline", "author", "date"])
    for i, article in enumerate(articles):
        writer.writerow([i, article[1], article[0], article[2], article[3]])

# Create an SQLite database and store the results in it
conn = sqlite3.connect('verge.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS articles
             (id INTEGER PRIMARY KEY, url TEXT, headline TEXT, author TEXT, date TEXT)''')
for i, article in enumerate(articles):
    c.execute("INSERT OR IGNORE INTO articles VALUES (?, ?, ?, ?, ?)", (i, article[1], article[0], article[2], article[3]))
conn.commit()
conn.close()
