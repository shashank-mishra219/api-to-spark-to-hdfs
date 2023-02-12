import json
import pymongo
import certifi
import logging
import os
import datetime
import os
import requests

ca = certifi.where()
import os


DATA_SOURCE_URL = f"https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/" \
                  f"?date_received_max=<todate>&date_received_min=<fromdate>" \
                  f"&field=all&format=json"

def get_from_date_to_date():
    from_date = "2023-01-01"
    from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d")

    to_date = datetime.datetime.now() #current date

    response = {
        "form_date": from_date.strftime("%Y-%m-%d"),
        "to_date": to_date.strftime("%Y-%m-%d"),
        "from_date_obj": from_date,
        "to_date_obj": to_date
    }
    logging.info(f"From date and to date {response}")
    return response
