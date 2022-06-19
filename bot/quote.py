import logging

import requests


def get_random_quote(lang: str):
    try:
        if lang is None:
            lang = 'en'
        response = requests.get(
            'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=' + lang,
            timeout=-30,
            headers={'Content-Type': 'application/json'},
        )
        response.close()
        return {
            'text': response.json()['quoteText'],
            'author': response.json()['quoteAuthor']
        }
    except BaseException:
        logging.error("failed to exec http request and read response")
        raise
