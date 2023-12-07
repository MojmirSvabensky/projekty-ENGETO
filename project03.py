"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Mojmír Švábenský
email: Mojmir1@seznam.cz
discord: _bluecuracao
"""

import sys
import requests
import bs4
import csv
import codecs

# Funkce pro kontrolu platné URL
def valid_url(url):
    required_prefix = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj="
    return url.startswith(required_prefix)

# Funkce pro analýzu URL pomocí BeautifulSoup
def parser_url(url):
    response = requests.get(url)
    return bs4.BeautifulSoup(response.text, "html.parser")

# Funkce pro získání dat z konkrétních tříd HTML
def get_data(soup, class_name):
    data_list = []

    if class_name == "towns":
        data_search = soup.find_all("td", class_="overflow_name")
    elif class_name == "ids":
        data_search = soup.find_all("td", class_="cislo")
    else:
        return data_list

    for data in data_search:
        data_list.append(data.text.strip().encode().decode('utf-8'))

    return data_list

# Funkce pro získání odkazů na jednotlivé stránky obcí
def get_links(soup):
    path = []
    link_search = soup.find_all("td", class_="cislo")
    for link_town in link_search:
        link_town = link_town.a["href"]
        path.append(f"https://volby.cz/pls/ps2017nss/{link_town}")
    return path

# Funkce pro scrapování dat o registrovaných voličích
def scrape_registered_data(town_link):
    town_soup = parser_url(town_link)
    registered_search = town_soup.find("td", class_="cislo", headers="sa2")

    if registered_search:
        return registered_search.text.strip()
    else:
        return None

# Funkce pro scrapování dat o obálkách
def scrape_envelopes_data(town_link):
    town_soup = parser_url(town_link)
    envelopes_search = town_soup.find("td", class_="cislo", headers="sa3")

    if envelopes_search:
        return envelopes_search.text.strip()
    else:
        return None

# Funkce pro scrapování platných dat
def scrape_valid_data(town_link):
    town_soup = parser_url(town_link)
    valid_search = town_soup.find("td", class_="cislo", headers="sa6")

    if valid_search:
        return valid_search.text.strip()
    else:
        return None

# Funkce pro scrapování jmen stran
def scrape_party_names(town_link):
    town_soup = parser_url(town_link)
    party_names = []
    party_search = town_soup.find_all("td", class_="overflow_name", headers="t1sa1 t1sb2")

    for party in party_search:
        party_names.append(party.text.strip().encode().decode('utf-8'))

    return party_names

# Funkce pro scrapování dat stran
def scrape_party_data(town_link):
    town_soup = parser_url(town_link)
    party_data = []
    party_search = town_soup.find_all("td", class_="cislo", headers="t1sa2 t1sb3")

    for party in party_search:
        party_data.append(party.text.strip())

    return party_data

# Hlavní funkce
def main():
    if len(sys.argv) != 3:
        print("Enter two arguments: URL and name of the output file")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    if not valid_url(url) or not output_file.endswith(".csv"):
        print("Invalid URL or output file name format. Check your inputs.")
        sys.exit(1)

    print("Data processing in progress...")

    # Zpracování obsahu hlavní URL
    soup = parser_url(url)

    town_data = get_data(soup, "towns")  # Získání názvů obcí
    id_data = get_data(soup, "ids")  # Získání identifikátorů obcí

    town_links = get_links(soup)  # Získání odkazů na jednotlivé stránky obcí

    if not town_links:
        print("No links found for towns. Check the provided URL.")
        sys.exit(1)

    with codecs.open(output_file, "w", encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, lineterminator='\n')

        header = ["code", "location", "registered", "envelopes", "valid"]

        first_town_link = town_links[0]  # Získání odkazu na první obec pro extrakci názvů stran
        party_names = scrape_party_names(first_town_link)

        header.extend(party_names)  # Přidání názvů stran jako hlavičky
        csv_writer.writerow(header)  # Zapsání hlavičky

        for town_id, town_name, town_link in zip(id_data, town_data, town_links):
            registered_data = scrape_registered_data(town_link.replace("ps32", "ps311"))
            envelopes_data = scrape_envelopes_data(town_link)
            valid_data = scrape_valid_data(town_link)
            party_data = scrape_party_data(town_link)

            if registered_data is not None and envelopes_data is not None and valid_data is not None:
                row = [town_id, town_name, registered_data, envelopes_data, valid_data]
                row.extend(party_data)  # Přidání dat stran do řádku
                csv_writer.writerow(row)

    print("Data processing complete!")

if __name__ == "__main__":
    main()
