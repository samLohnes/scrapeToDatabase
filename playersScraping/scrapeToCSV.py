# This is the function where the players spider will be called, and then Pandas dataframes
# will be utilized to append each team's players into one dataFrame which will then be read
# into a CSV file
from playersScraping.playersScraping.spiders.teams_spider import TeamsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
def scrapeTeamsFromSite():

    process = CrawlerProcess(get_project_settings())

    process.crawl(TeamsSpider)
    process.start()

def scrapePlayersFromSite(links):
    return