import bs4
import requests
import lxml
import pandas as pd
import re
import os

total_page = 5
data_df = pd.DataFrame(columns=["Reviews","Date","Rating"])

def process_url(url: str):
    url = re.sub("(\/dp\/)","/product-reviews/", url)
    return url


def get_request(path:str):
    """
    Get the request from the url passed in path -> str
    """
    res = requests.get(path)
    return res


def get_data(soup:bs4.BeautifulSoup):
    """
    Getting data in equal propertion of 6 reviews of each star
    """
    rows = soup
    global data_df
    for row in rows:
        reviews = row.find('span', {'class':'a-size-base review-text review-text-content'}).text
        star = row.find("span", {"class": "a-icon-alt"}).text
        date = row.find("span", {"class": "a-size-base a-color-secondary review-date"}).text
        data = [{"Reviews":reviews,
                 "Date":date[21::],
                 "Rating":star[0]
                 }]

        data_df = data_df.append(data)


def scrape(url:str):
    """
    Scrapes the reviews from the resuests object
    """
    i = 0
    stars = ["five_star","four_star","three_star","two_star","one_star"]

    for i in range(total_page):
        adder = f"/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&filterByStar={stars[i]}&pageNumber={1}"
        link = url+adder
        res = get_request(link)
        soup = bs4.BeautifulSoup(res.text,"lxml")
        rows = soup.find_all("div",{"class":"a-section celwidget"})
        get_data(rows)
        yield i
        

def save_data():
    global data_df
    data_df.to_csv("./reviews.csv")
    return os.getcwd()+"/reviews.csv"



