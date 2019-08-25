# Mission-To-Mars

![](Mars.gif)

12-Web-Scraping-and-Document-Databases-Homework

## # Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

##Scraping

Initial scraping complied Jupyter Notebook using BeautifulSoup, Pandas, and Requests/Splinter.

* See Jupyter Notebook `Mission_To_Mars.ipynb` for scraping and analysis tasks:

    1. NASA Mars News

        * Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.

    2. JPL Mars Space Images - Featured Image

        * Scraped the JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

        * Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

            * Found the image url to the full size `.jpg` image.

            * Saved a complete url string for this image.

    3. Mars Weather

        * Scraped the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) for the latest Mars weather tweet from the page. 
            * Saved the tweet text for the weather report as a variable called `mars_weather`.

    4.  Mars Facts

        * Scraped the Mars Facts webpage [here](https://space-facts.com/mars/)  
            
            * Used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

            * Used Pandas to convert the data to a HTML table string.

    5. Mars Hemispheres

        * Scraped the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

            * Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

            * Appended scarpped data into a dictionary containing the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


## MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* See file `scrape_mars.py` with a function called `scrape` that executes all of your scraping code from the jupyter notebook and return one Python dictionary containing all of the scraped data.

* See route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* See template HTML file called `index.html` that will takes the mars data dictionary and display all of the data in the appropriate HTML elements. 






