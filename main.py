# This is the main file that will be used to run the final scraping into a dataBase function

from playersScraping.scrapeToCSV import scrapeTeamsFromSite as PLteamScrape
from playersScraping.scrapeToCSV import scrapePlayersFromSite as ScrapePlayers

def main():
    PLteamScrape()
    allPlayers = ScrapePlayers()
    allPlayers.to_csv('allPlayers.csv')
    print(allPlayers)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
