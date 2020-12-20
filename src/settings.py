import os


class ScraperEnv:
    """Environment class for scraper module"""

    url: str
    log_level: str

    def __init__(self):
        self.url = os.getenv("URL") or "https://uk.finance.yahoo.com/currencies"
        self.log_level = os.getenv("LOG_LEVEL") or "INFO"


class ServerEnv:
    """Environment class for __main__ module"""

    host: str
    port: str
    log_level: str

    def __init__(self):
        self.host = os.getenv("HOST") or "localhost"
        self.port = os.getenv("PORT") or 8081
        self.log_level = os.getenv("LOG_LEVEL") or "INFO"
