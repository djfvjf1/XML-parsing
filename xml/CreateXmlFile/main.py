# Программа парсит XML-файл

import urllib.request
import xml.dom.minidom as minidom

def get_data(xml_url):
    web_file = urllib.request.urlopen(xml_url)
    return web_file.read()

def get_dictionary(xml_content):
    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict


def print_dict(dict):
    for key in dict.keys():
        print(key, dict[key])


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currency_dict = get_dictionary(get_data(url))
    print_dict(currency_dict)