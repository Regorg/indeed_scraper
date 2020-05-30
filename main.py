from scraper.scraper import Scraper
from scraper.template import Template


def start_scraping():
    job_name = input('Enter job name: ')
    place = input('Enter place: ')
    radius = int(input('Enter radius: '))

    scraper = Scraper(job_name, place, radius)
    print(f'URL: {scraper.page.url}, Place: {scraper.location}, Job name: \
{scraper.job_name}\n')

    template = Template(scraper.offers, scraper.number_of_offers)


if __name__ == '__main__':
    start_scraping()
