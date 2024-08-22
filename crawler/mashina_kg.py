import requests
from parsel import Selector
from pprint import pprint


class MashinaCrawler:
    MAIN_URL = "https://www.mashina.kg/search/all/?region=all"
    BASE_URL = "https://www.mashina.kg"

    def get_page(self):
        page = requests.get(url=MashinaCrawler.MAIN_URL, timeout=10)
        # print(page.text[:400])
        self.page = page.text

    def get_page_title(self):
        html = Selector(text=self.page)
        title = html.css('title::text').get()
        print(title)

    def get_car_links(self):
        html = Selector(text=self.page)
        links = html.css('div.list-item a::attr(href)').getall()
        links = list(map(lambda l: MashinaCrawler.BASE_URL + l, links))
        # pprint(links)
        return links[:3]


if __name__ == "__main__":
    crawler = MashinaCrawler()
    crawler.get_page()
    # crawler.get_page_title()
    crawler.get_car_links()
