# Python CCY Exchange Rate Task

For this task we want you to scrape live currency exchange rate data from
https://uk.finance.yahoo.com/currencies/ as it's requested by a client. This is
similar to something you might work on while at Mollybet.

## Getting started

You should make a python3.8 virtual env, and then install the dependencies in requirements.txt

```bash
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```

Inside `yahoo_scraper/__main__.py` you'll find a simple server that listens on
localhost 8080. Make sure you've activated the env and then start it with:

```bash
python -m yahoo_scraper
```

In another terminal you can connect to it as a client with `nc localhost 8080`
and send some requests, this is how we will test your solution.

```bash
$ nc localhost 8080
Connected!
EUR:USD
0.0
USD:EUR
0.0
```

## Your task

Spend 3 to 4 hours filling out the server so that it will scrape the live
exchange rate for the requested currency pair and send it back to the client.
We're happy for you to use any relatively common python library that you think
would help. If you do add it to the `requirements.in` file and then run:

```bash
pip-compile requirements.in > requirements.txt
```

This task is intentionally open ended, so you are free to structure the code
however you want, and make changes to the server if you think it will help.
Here are some things that we'll have in mind when judging your solution.

* Correctness: Does the server fetch the correct rate from the yahoo website
* Speed: How long does the client wait for a rate
* Style: Is your code idiomatic python

This is your opportunity to show us what you know and impress us, so don't
hesitate to make a change to the server or add parts if you think it would need
it. 

Once you've written your solution do a small write up of how it works and what
changes (if any) you would make before deploying this server to production.
After that please zip all the files and send it back to us.

## Write Up

For this task I used BeautifulSoup library with the lxml parser. I believe these are relatively common Python libraries.

Completed:
1. Reuse server connection
2. Input Validation
3. Request speed optimization (Mobile Headers and lxml parser)
4. Logging
5. Tests
6. Split code into modules
7. Snake case variable names
8. Retrieving config from Environment variables
9. User-friendly exceptions and error messages
10. Docstring


Considerations:

1. Scrape purely with regex for better performance (Arguably at the cost of readability, maintainability and extensibility)
   get_rate_regex method is available in the scraper.py module.
2. Write a deployment script (CDK for AWS services)
    
    




