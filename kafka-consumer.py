from kafka import KafkaConsumer
import json
from s3fs import S3FileSystem

# Getting the data as JSON
consumer = KafkaConsumer('quickstart-events',
bootstrap_servers=['43.204.232.133:9092'],
value_deserializer=lambda m: json.loads(m.decode('ascii')))


s3 = S3FileSystem()

for count, i in enumerate(consumer):
    with s3.open("s3://kafka-event-stream/stock_market_{}.json".format(count), 'w') as file:
        print("writing to s3 bucket")
        json.dump(i.value, file)     