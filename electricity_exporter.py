#!/usr/bin/env python

from prometheus_client import start_http_server, Gauge
from time import gmtime, strftime
import time
import requests
import socket
import argparse
import json

version = 0.58


# Parse commandline arguments
parser = argparse.ArgumentParser(description="Electricity company price Prometheus exporter v" + str(version))
parser.add_argument("-p", "--port", metavar="<port>", required=False, help="Port for listenin", default=8111, type=int)
args = parser.parse_args()


listen_port = args.port
ELECTRICITY_PRICE_ENDESA   = Gauge('electricity_price_endesa_kwh_eur_price', 'endesa kwh euro price')


ELECTRICITY_PRICE_ENDESA.set_function(lambda: get_endesa_price() )

def get_endesa_price():
    nowDate = strftime("%Y-%m-%d", gmtime())
    data={u'currentDate':nowDate,'currentRate':'GEN'}
    headers={u"Content-Type":"application/x-www-form-urlencoded","x-requested-with":"XMLHttpRequest"}
    r = requests.post("https://www.endesaclientes.com/sites/Satellite/?pagename=SiteEntry_IB_ES/LandingPrice/GetPrices",headers=headers,data=data)
    pos = r.text.find("var actualPrice = ")+19
    parsed = r.text[pos:]
    end = parsed.find("\"")
    parsed = parsed[:end]
    return  parsed



# Main entry point
if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(listen_port)

    # Main loop
    while True:
        time.sleep(5000)