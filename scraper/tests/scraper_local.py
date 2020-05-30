from bs4 import BeautifulSoup
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from scraper import Scraper


class ScraperLocal(Scraper):
    """
    Class created only for testing purpose.
    """
    def __init__(self):
        with open('data/sample_page.html', 'r') as f:
            self.static_page = f.read()
        self.soup = BeautifulSoup(self.static_page, 'html.parser')
        self.result = self.soup.find(id='resultsCol')
        self.jobs = self.find_jobs_div()
        self.offers = {}

    def find_jobs(self):
        for job in self.jobs:
            title = job.find('h2', class_='title')
            company = job.find('span', class_='company')
            location = job.find('div', class_='location')

            if not location:
                location = job.find('span', class_='location')
                if not location:
                    continue

            date = job.find('span', class_='date')
            link = job.find('a')['href']

            if location is None:
                print("\nSomething went wrong...")
                continue
            self.add_to_offers(title, company, location, date, link)


scraper = ScraperLocal()
scraper.find_jobs()
