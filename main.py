# This is the main file that will be used to run the final scraping into a dataBase function

from playersScraping.scrapeToCSV import scrapeTeamsFromSite as teamScrape

def main():
    # Use a breakpoint in the code line below to debug your script.
    teamScrape()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
