# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt


def init_browser():
    # Chromedrive.exe for Windows
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image_url(browser),
        "hemispheres": hemisphere_image_urls(browser),
        "weather": weather_tweet(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

# News Scrape 
def mars_news():
    browser = init_browser()

    # Latest NASA News Article 
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)

    # HTML Object
    html = browser.html
    # Parse HTML with Beautiful Soup
    nasa_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest news_title and news_paragraph
    news_title = nasa_soup.find('div', class_='content_title').find('a').text
    news_p = nasa_soup.find('div', class_='article_teaser_body').text

    return news_title, news_p

    browser.quit()

# Featured Image Scrape 
def featured_image_url():
    browser = init_browser()
    # JPL Mars Space Images - Featured Image
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)

    # HTML Object
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    image_soup = BeautifulSoup(html_image, 'html.parser')

    # Retrieve background-image url from style tag
    featured_image_url = image_soup.find('article')['style'].replace('background-image: url(', '').replace(');', '')[1:-1]
    
    return featured_image_url

    browser.quit()
    
    # Mars Weather Scrape 
def weather_tweet():
    browser = init_browser()
    # Visit Mars Weather Twitter through splinter module
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    
    # HTML Object
    weather_html = browser.html

    # Parse HTML with Beautiful Soup
    tweet_soup = BeautifulSoup(weather_html, 'html.parser')

    # Find all elements that contain tweets
    weather_tweet = tweet_soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    return weather_tweet

    browser.quit()

    # Mars Facts Scrape
def mars_facts():
    browser = init_browser()

    # Scrape the table of Mars facts
    facts_url = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(facts_url)

    # Create datarame and columns
    df = tables[0]

    # Rename Columns
    df.columns = ['Fact_Category', 'Mars_Value', 'Earth_Value']

    # Remove Earth_Values
    facts_df = df[['Fact_Category', 'Mars_Value', ]]

    # Set Facts_Category as Index
    facts_df.set_index('Fact_Category', inplace=True)

    # Print Dataframe
    facts_df.head()

    # Convert Dataframe to HTML
    mars_facts = facts_df.to_html()

    return mars_facts

    browser.quit()

    # Mars Hemispheres
def hemisphere_image_urls():
    browser = init_browser()

    # Visit hemispheres website through splinter module
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    
    # HTML Object
    html_hemi = browser.html

    # Parse HTML with Beautiful Soup
    hemi_soup = BeautifulSoup(html_hemi, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = hemi_soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls
    hemisphere_image_urls = []

    # Store the main_ul
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    for i in items:
        # Store title
        title = i.find('h3').text

        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']

        # Visit the link that contains the full image website
        browser.visit(hemispheres_main_url + partial_img_url)

        # HTML Object of individual hemisphere information website
        partial_img_html = browser.html

        # Parse HTML with Beautiful Soup for every individual hemisphere information website
        soup = BeautifulSoup(partial_img_html, 'html.parser')

        # Retrieve full image source
        img_url = hemispheres_main_url + \
            soup.find('img', class_='wide-image')['src']

        # Append the retreived information into a list of dictionaries
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
        
        return hemisphere_image_urls

        browser.quit()
