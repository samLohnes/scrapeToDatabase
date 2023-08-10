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
    # Input: None -> in the future may need to create a functionality to input a url or list of urls to
    # allow for a listing of leagues to be grabbed
    # Output: Pandas DataFrame

    # Reads in the team links csv file that the Scrapy Spider scraped into a dataframe
    urls = pd.read_csv('PLTeamLinks.csv')['Link to Team Page'].tolist()

    # Loop goes through the urls and grabs the information from them,
    # uses the length of dataFrames to determine which state of cleanTeamStats
    # to use
    # end state of the loop is to have a list of dataFrames which will then be concatenated
    # together to have a list of all the players in the premier league
    dataFrames = []
    for i in urls:
        # Takes the current team out of the url based on the FBRef standard format for urls, and has
        # functionality to remove hyphens and replace them with spaces
        currTeam = i.split('/')[-1].replace('-Stats','').replace('-',' ')
        # Reads in the table from the pandas read_html, cleans it using the cleanTeamStats method,
        # Then drops the extra header level, and then adds a new column to represent the current team that
        # was grabbed in the line above
        temp = pd.read_html(i)[0]
        temp = cleanTeamStats(temp, initialTeam=len(dataFrames))
        temp = temp.droplevel(0, axis=1)
        temp['Team'] = currTeam

        dataFrames.append(temp)
        print("Sleeping")
        time.sleep(1)

    df = pd.concat(dataFrames, ignore_index=True)
    df = df.drop(['Matches', 'MP'], axis=1)
    # Uses the replaceNations function, and then the dataframe has been fully cleaned so it is returned to main
    return replaceNations(df)


def cleanTeamStats(dataframe, initialTeam=False):
    # Intended to take a dataframe and remove the unnecessary opponents data from the team statistics
    if initialTeam:
        return dataframe.drop(index=[dataframe.index[-2], dataframe.index[-1]])
    else:
        return dataframe.drop(index=[dataframe.index[0], dataframe.index[-2], dataframe.index[-1]])


def replaceNations(dataframe):
    # Replaces the abbreviated nations of each player that FBRef uses as standard with the actual names
    # of the country that they represent
    nationsDict = {'al ALB': 'Albania', 'ar ARG': 'Argentina', 'at AUT': 'Austria', 'au AUS': 'Australia',
                   'ba BIH': 'Bosnia and Herzegovina', 'be BEL': 'Belgium', 'bf BFA': 'Burkina Faso',
                   'br BRA': 'Brazil',
                   'cd COD': 'DR Congo', 'ch SUI': 'Switzerland', 'ci CIV': 'Ivory Coast', 'cm CMR': 'Cameroon',
                   'co COL': 'Colombia', 'cr CRC': 'Costa Rica', 'cz CZE': 'Czechia', 'de GER': 'Germany',
                   'dk DEN': 'Denmark', 'dz ALG': 'Algeria',
                   'ec ECU': 'Ecuador', 'ee EST': 'Estonia', 'eg EGY': 'Egypt', 'es ESP': 'Spain', 'eng ENG': 'England',
                   'fi FIN': 'Finland', 'fr FRA': 'France', 'ga GAB': 'Gabon', 'gd GRN': 'Grenada', 'gh GHA': 'Ghana',
                   'gn GUI': 'Guinea', 'gr GRE': 'Greece',
                   'hr CRO': 'Croatia', 'hu HUN': 'Hungary', 'ie IRL': 'Ireland', 'il ISR': 'Israel', 'iq IRQ': 'Iraq',
                   'ir IRN': 'Iran', 'it ITA': 'Italy', 'jm JAM': 'Jamaica', 'jp JPN': 'Japan',
                   'kr KOR': 'Republic of Korea',
                   'lr LBR': 'Liberia', 'ma MAR': 'Morocco', 'me MNE': 'Montenegro', 'ml MLI': 'Mali',
                   'ms MSR': 'Monserrat',
                   'mx MEX': 'Mexico', 'ng NGA': 'Nigeria', 'nir NIR': 'Northern Ireland', 'nl NED': 'Netherlands',
                   'no NOR': 'Norway', 'nz NZL': 'New Zealand', 'pl POL': 'Poland', 'pt POR': 'Portugal',
                   'py PAR': 'Paraguay',
                   'rs SRB': 'Serbia', 'sct SCO': 'Scotland', 'se SWE': 'Sweden', 'sk SVK': 'Slovakia',
                   'sn SEN': 'Senegal',
                   'tr TUR': 'Turkey', 'ua UKR': 'Ukraine', 'us USA': 'United States', 'uy URU': 'Uruguay',
                   've VEN': 'Venezuela', 'wls WAL': 'Wales', 'zm ZAM': 'Zambia', 'zw ZIM': 'Zimbabwe'
                   }

    return dataframe.replace({'Nation':nationsDict})
