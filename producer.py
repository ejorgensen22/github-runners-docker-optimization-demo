from kafka import KafkaProducer
import json
import time
import sys

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

print('Sending test messages to Kafka...')
for i in range(5):
    producer.send('test-topic', {'message': f'Hello from GitHub Actions Lambda simulation {i}', 'timestamp': time.time()})
    time.sleep(0.5)

print('Messages sent successfully!')
producer.flush()
sys.exit(0)