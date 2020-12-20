import re
import requests
import logging
from bs4 import BeautifulSoup
from settings import ScraperEnv

ENV = ScraperEnv()
logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(ENV.log_level)

HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, "
                  "like Gecko) Version/4.0 Mobile Safari/534.30"
}


class CcyPairNotFound(Exception):
    """Currency Pair not found exception"""


def get_rate(from_ccy: str, to_ccy: str) -> str:
    """ Searches for currency rate using BeautifulSoup
    :param from_ccy: base currency symbol
    :param to_ccy: quote currency symbol
    :return: quote value
    :raises CcyPairNotFound
    """

    ccy_pair = f"{from_ccy}/{to_ccy}"
    LOGGER.info(f"Getting rate for {ccy_pair}")
    response = requests.get(ENV.url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    ccy_td = soup.find("td", text=f"{ccy_pair}")
    if ccy_td is None:
        raise CcyPairNotFound
    result = ccy_td.next_sibling.text
    LOGGER.info(f"Got: {result}")
    return result


def get_rate_regex(from_ccy: str, to_ccy: str) -> str:
    """ Searches for currency rate using regex
    :param from_ccy: base currency symbol
    :param to_ccy: quote currency symbol
    :return: quote value
    :raises CcyPairNotFound
    """

    ccy_pair = f"{from_ccy}/{to_ccy}"
    LOGGER.info(f"Getting rate for {ccy_pair}")
    response = requests.get(ENV.url, headers=HEADERS)
    pattern = re.compile(f">{ccy_pair}</td><td.*?>([0-9]+.[0-9]+)</td>")
    match = pattern.search(response.text)
    if match is None:
        raise CcyPairNotFound
    result = match.group(1)
    LOGGER.info(f"Got: {result}")
    return result
