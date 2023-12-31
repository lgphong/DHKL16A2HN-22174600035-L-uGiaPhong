import feedparser
import csv

def parse_rss_feed(url):
    feed = feedparser.parse(url)
    news_items = []

    for entry in feed.entries:
        news_item = {}
        news_item['title'] = entry.title
        news_item['link'] = entry.link
        news_item['description'] = entry.summary
        news_items.append(news_item)

    return news_items

def save_to_csv(news_items, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['title', 'link', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(news_items)

if __name__ == "__main__":
    rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
    csv_filename = "news_items.csv"

    news_items = parse_rss_feed(rss_url)
    save_to_csv(news_items, csv_filename)
