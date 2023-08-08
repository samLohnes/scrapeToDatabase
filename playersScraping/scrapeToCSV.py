# This is the function where the players spider will be called, and then Pandas dataframes
# will be utilized to append each team's players into one dataFrame which will then be read
# into a CSV file
from playersScraping.playersScraping.spiders.prem_teams_spider import PremTeamsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import time
def scrapeTeamsFromSite():

    process = CrawlerProcess(get_project_settings())

    process.crawl(PremTeamsSpider)
    process.start()

def scrapePlayersFromSite():

    df = pd.read_csv('PLTeamLinks.csv')
    urls = df['Link to Team Page'].tolist()
    df = pd.read_html(urls[0], skiprows=0)[0]

    df = cleanTeamStates(df, True)
    dataFrames = [df]
    for i in urls[1:]:
        temp = pd.read_html(i)[0]
        temp = cleanTeamStates(temp)

        dataFrames.append(temp)
        print("Sleeping")
        time.sleep(1)

    df = pd.concat(dataFrames, ignore_index=True)
    df = df.drop("Unnamed: 33_level_0", axis=1)

    return df


def cleanTeamStates(dataframe, initialTeam=False):
    # Intened to take a dataframe and remove the unnecessary opponents data from the team statistics
    if initialTeam:
        return dataframe.drop(index=[dataframe.index[-2], dataframe.index[-1]])
    else:
        return dataframe.drop(index=[dataframe.index[0], dataframe.index[-2], dataframe.index[-1]])