from jinja2 import Environment, PackageLoader, select_autoescape


class Template:
    def __init__(self, offers, number_of_offers):
        self.offers = offers
        self.number_of_offers = number_of_offers
        self.env = Environment(
            loader=PackageLoader('scraper', 'templates'),
        )
        self.template = self.env.get_template('template.html')
        self.__render_output()

    def __render_output(self):
        with open('output.html', 'w') as f:
            f.write(self.template.render(offers=self.offers,
                    number_of_offers=self.number_of_offers))

    def __repr__(self):
        return f'Template object: {self.env}'
