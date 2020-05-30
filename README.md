# Indeed Scraper
This program is designed to scrap job offers from https://pl.indeed.com/. Scraped offers go to output.html, and are nicely represented in form of bootstrap table.

![Indeed Web scraper](https://i.imgur.com/DVAChtO.png)

### Built With
* [Python](https://www.python.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://requests.readthedocs.io/en/master/)
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)



## Getting Started

```
git clone https://github.com/Regorg/indeed_scraper.git
```

### Prerequisites
* Python >=3.7
* requirements.txt
```
cd indeed_scraper
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

```
python main.py
Enter job name: <job name that you are looking for>
Enter place: <location>
Enter radius: <maximum distance from location>
```
Then after a while, you can check output.html in /indeed_scraper/

## Development usage

Fill < > parameters with specific data
```
scraper = Scraper(<job_name>, <location>, <radius>)
template = Template(scraper.offers, scraper.number_of_offers)
```

## Tests
You can find and run tests in /scraper/tests, by:
```
python test_scraper.py
```

### Additional info
Class ScraperLocal in /scraper/tests/scraper_local.py is designed to run tests on static version of indeed page, because some elements were hard to check on live version of site, due to constant changes. 
