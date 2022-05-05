import stocks_scraper

def number_company(data: list):
    number_of_company = []
    names = data
    for i in range(len(names)):
        number_of_company.append([names[i], i])
    return (number_of_company)
