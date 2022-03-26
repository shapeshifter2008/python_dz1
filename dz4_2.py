import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def currency_rates(currency):
    currency = currency.upper()
    url_data = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(str(url_data)).text
    xml_parse = ET.fromstring(response)

    date_doc = datetime.strptime(xml_parse.attrib['Date'], '%d.%m.%Y')

    for char_code in xml_parse.findall('Valute'):
        if (char_code.find('CharCode').text == currency):
            return f"{float(char_code.find('Value').text.replace(',', '.'))} {date_doc}"

    return None

print('USD', currency_rates('USD'))
print('EUR', currency_rates('EUR'))
print('ABC', currency_rates('ABC'))