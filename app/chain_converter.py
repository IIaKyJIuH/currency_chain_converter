import requests

from bs4 import BeautifulSoup
from functools import reduce
from operator import mul

CURRENCY_LINK_TEMPL = 'https://www.google.com/finance/quote/{0}-{1}'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


def _get_currency_price(currency_link: str) -> str:
    full_page = requests.get(currency_link, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll('div', {'class': 'YMlKec', 'class': 'fxKbKc'})
    return float(convert[0].text.replace(',', '.'))


def convert_chain(orig_spent: float, chain: str) -> dict:
    splitted_chain = chain.split('-')
    orig_code, targ_code = splitted_chain[0], splitted_chain[-1]

    currency_factor = reduce(
        mul,
        (_get_currency_price(CURRENCY_LINK_TEMPL.format(*args)) * 1.002
         for args in zip(splitted_chain, splitted_chain[1::]))
    )

    target_spent = orig_spent * currency_factor

    return {
        'Spent equivalent': f'{orig_spent} {orig_code} = {target_spent} {targ_code}',
        'Exchange rate': f'{orig_code}/{targ_code} = {target_spent / orig_spent}'
    }