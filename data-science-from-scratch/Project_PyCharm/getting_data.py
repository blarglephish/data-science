from collections import Counter
import math, random, csv, json, re
from matplotlib import pyplot as plt
import os.path

from bs4 import BeautifulSoup
import requests

#####
#
# O'Reilly Books About Data
#
#####

FILE_NAME = "comma_delimited_book_info.csv"

def is_video(td):
    """it's a video if it has exactly one pricelabel, and if
    the stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and
            pricelabels[0].text.strip().startswith("Video"))

def new_book_info(article):
    """given a BeautifulSoup <article> Tag representing content,
    extract the book's details and return a dict"""
    title = article.find('p', {'class' : 'title'}).a.text.strip()

    author_name = article.find('p', {'class' : 'note'}).text
    authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]

    publisher = (re.sub("^Publisher: ", "", article.find('p', {'class' : 'note publisher'}).text)).strip()

    release_date = (re.sub("^Release Date: ", "", article.find('p', {'class' : 'note date2'}).text)).strip()

    return {
        "title" : title,
        "authors" : authors,
        "publisher" : publisher,
        "date" : release_date
    }

# url = "http://shop.oreilly.com/category/browse-subjects/" + \
#            "data.do?sortby=publicationDate&page=1"
# soup = BeautifulSoup(requests.get(url).text, 'html5lib')

# new_url = "https://ssearch.oreilly.com/?i=1;m_Sort=searchDate;q=data;q1=Books;x1=t1&act=sort"
# new_soup = BeautifulSoup(requests.get(new_url).text, 'html5lib')
#
# # first_article = new_soup.find('article', {'class' : 'result product-result'})
# # print(first_article)
# for article in new_soup('article', {'class' : 'result product-result'}):
#     print(new_book_info(article))

from time import sleep

def scrape():
    books = []

    if os.path.exists(FILE_NAME):
        books = get_books_from_file(FILE_NAME)
    else:
        base_url = "https://ssearch.oreilly.com/?i=1;m_Sort=searchDate;q=data;q1=Books;x1=t1;page="
        NUM_PAGES = 105      # As of 11/1/2018, 11:39 AM

        for page_num in range(1, NUM_PAGES + 1):
            print("souping page", page_num, ",", len(books), "found so far")
            url = base_url + str(page_num)
            soup = BeautifulSoup(requests.get(url).text, 'html5lib')

            for article in soup('article', {'class' : 'result product-result'}):
                books.append(new_book_info(article))

            # now be a good citizen and respect the robots.txt!
            sleep(30)
        write_books(books, FILE_NAME)

    return books

def get_year(book):
    """book["date"] looks like 'November 2014' so we need to
    split on the space and then take the second piece"""
    date = book["date"]
    return int(book["date"].split()[1]) if book["date"] != "None" else 1900

def get_books_from_file(filename = FILE_NAME):
    books = []
    with open(filename, 'r') as f:
        field_names = ["title", "authors", "publisher", "date"]
        reader = csv.DictReader(f, delimiter=',', fieldnames=field_names)
        next(reader)
        for row in reader:
            books.append(row)
    return books

def write_books(books, filename=FILE_NAME):
    """writes out the file"""
    with open(filename, 'w', newline='') as f:
        fieldnames = ['title', 'authors', 'publisher', 'date']
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()

        for book in books:
            writer.writerow(book)

def plot_books_on_date():
    books = scrape()
    year_counts = Counter(get_year(book) for book in books if book["date"] != "None" and get_year(book) <= 2014)
    print(year_counts)
    years = sorted(year_counts)
    book_counts = [year_counts[year] for year in years]
    # plt.bar([x for x in years], book_counts)
    plt.plot(years, book_counts)
    plt.xlabel("year")
    plt.ylabel("# of data books")
    plt.title("Data is Big!")
    plt.show()

#####
#
# APIs
#
#####

endpoint = "https://api.github.com/users/joelgrus/repos"
repos = json.loads(requests.get(endpoint).text)

from dateutil.parser import parse

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repositories = sorted(repos,
                             key=lambda r: r["created_at"],
                             reverse=True)[:5]
last_5_languages = [repo["language"]
                    for repo in last_5_repositories]

for repo in last_5_repositories:
    print(repo)
print(last_5_languages)

#####
#
# TWITTER API
#
#####
