from bs4 import BeautifulSoup
import requests

def get_stocks_data():
    """Scrapes web page with companies names and PE trails coeficient. Creates a list for names and a list for coeficients.

    Returns:
        list: [names, pe_trails]
    """
    #Connecting with web page
    web_page = requests.get('https://fknol.com/list/market-cap-sp-500-index-companies.php?go=e0').text
    soup = BeautifulSoup(web_page, 'lxml')

    raw_data = soup.find_all('tr')

    names = []
    pe_trails = []

    #Getting the names of companies
    for data in raw_data:
        data_in_td = data.find_all('td')

        for data in data_in_td:
            data_in_b = [b.string for b in data.findAll('b')]

            if data_in_b != []:
                names.append(data_in_b[0])

    names = names[8:]

    #Getting the coeficients
    for data in raw_data:
        data_in_lower_td = data.findAll('td', align="center")
        
        for data in data_in_lower_td:
            for d in data:
                pe_trails.append(d)

    pe_trails = pe_trails[7::9]

    return [names, pe_trails] 
