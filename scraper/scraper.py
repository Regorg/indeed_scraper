import requests
from bs4 import BeautifulSoup
import re
import math


class Scraper:
    def __init__(self, job_name: str, location: str, radius: int):
        self.job_name = job_name
        self.location = location
        self.radius = radius
        self._url = ''

        self.page = None
        self.page_number = 0
        self.get_content()

        self.is_skipped = ''
        self.offers = {}
        self.number_of_offers = 0

        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.result = None

        self.__find_job_offers()

    def get_url(self) -> str:
        return self._url

    def set_url(self, url: str) -> None:
        self._url = url

    def connect(self, url: str) -> object:
        try:
            self.set_url(url)
            connection = requests.get(self.get_url())
            return connection
        except requests.exceptions.RequestException as e:
            return e

    def get_content(self) -> None:
        self.page = self.connect(f'https://pl.indeed.com/jobs?q=\
{self.job_name}&l={self.location}&sort=date&radius={self.radius}\
&start={self.page_number}')
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.result = self.soup.find(id='resultsCol')

    def skip(self) -> None:
        self.is_skipped = input("Do you want to skip offers that are older\
 than 30 days? y/n: ")

    def find_jobs_div(self) -> str:
        return self.result.find_all('div', class_='jobsearch-SerpJobCard')

    def add_to_offers(self, title: str, company: str, location: str, date: str,
                      link: str) -> None:
        self.offers[title.text.strip()] = {
            'company': company.text.strip(),
            'location': location.text.strip(),
            'date': date.text.strip(),
            'link': "https://pl.indeed.com" + str(link)
        }

    def find_number_of_pages(self) -> int:
        pages = self.soup.find(id='searchCountPages')
        if not pages:
            return False
        text = pages.text.strip()

        # indeed display 15 offers on single page, that's why i divide by 15
        number_of_pages = int(re.findall(r'\d+', text)[1])
        return math.ceil(number_of_pages / 15)

    def update_pages(self, pages: int) -> list:
        pages_urls = []
        for i in range(pages):
            counter = i * 10
            pages_urls.append(counter)
        return pages_urls

    def is_location_set(self, location: str, job: object) -> tuple:
        if not location:
            location = job.find('span', class_='location')
            if not location:
                return False, None
        return True, location

    def is_over30_skipped(self, date: str) -> bool:
        if self.is_skipped.lower() == 'y':
            if date.text.strip()[:3] == '30+':
                return True
        return False

    def __find_job_offers(self) -> None:
        self.skip()
        pages = self.find_number_of_pages()
        if not pages:
            print('No offers found! Try to change your query.')
            return

        pages_updated = self.update_pages(pages)

        for page in pages_updated:
            self.page_number = page
            self.get_content()
            jobs = self.find_jobs_div()
            for job in jobs:
                title = job.find('h2', class_='title')
                company = job.find('span', class_='company')
                location = job.find('div', class_='location')
                date = job.find('span', class_='date')
                link = job.find('a')['href']

                is_location, location = self.is_location_set(location, job)

                if not is_location or self.is_over30_skipped(date):
                    continue

                if None in (title, company, location, date, link):
                    print("Something went wrong, offer skipped...")
                    continue

                self.add_to_offers(title, company, location, date, link)
                self.number_of_offers += 1
        print("Done! Go check output.html")

    def __repr__(self) -> str:
        return f'Scraper object with {self.get_url()} URL'
