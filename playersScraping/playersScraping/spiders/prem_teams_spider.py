import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess


class PremTeamsSpider(scrapy.Spider):
    name = "PLteams"

    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        }
    )

    def start_requests(self):
        url = "https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        teamLinks = response.xpath('//div[@id="switcher_results2022-202391"]//div["@id=div_results2022-202391_overall"]'
                                   '//table["@id=results2022-202391_overall"]//tbody//tr//td["@class=left"]'
                                   '//a[contains(@href, "squad")]//@href').extract()
        teamLinks = teamLinks[:len(teamLinks) // 2]

        df = pd.DataFrame(teamLinks)
        df[0] = 'https://fbref.com' + df[0]
        df.rename(columns={0:'Link to Team Page'}, inplace=True)

        df.to_csv('PLTeamLinks.csv')

        self.log("Saved file")
