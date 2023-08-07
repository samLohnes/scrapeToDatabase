import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess


class TeamsSpider(scrapy.Spider):
    name = "teams"

    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        }
    )

    def start_requests(self):
        urls = [
            "https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats#all_results2022-202391"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        teamLinks = response.xpath('//div[@id="switcher_results2022-202391"]//div["@id=div_results2022-202391_overall"]'
                                   '//table["@id=results2022-202391_overall"]//tbody//tr//td["@class=left"]'
                                   '//a[contains(@href, "squad")]//@href').extract()
        teamLinks = teamLinks[:len(teamLinks) // 2]

        df = pd.DataFrame(teamLinks)
        df.to_csv('PLTeamLinks.csv')

        self.log("Saved file")
