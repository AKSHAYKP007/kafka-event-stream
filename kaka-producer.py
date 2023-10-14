from kafka import KafkaProducer
from time import sleep
import requests
import json

# Coinbase API endpoint
url = 'https://api.coinbase.com/v2/prices/btc-usd/spot'

# Producing as JSON
producer = KafkaProducer(bootstrap_servers=['43.204.232.133:9092'],
value_serializer=lambda m: json.dumps(m).encode('ascii'))

while(True):
  sleep(2)
  price = ((requests.get(url)).json())
  print("Price fetched")
  producer.send('quickstart-events', price)
  print("Price sent to consumer")
