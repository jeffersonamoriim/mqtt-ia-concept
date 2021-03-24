import pika, json, time, random
from decouple import config
from datetime import datetime

credentials = pika.PlainCredentials(username=config('RABBITMQ_DEFAULT_USER'), password=config('RABBITMQ_DEFAULT_PASS'))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=config('RABBITMQ_DEFAULT_HOST'), credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='input_data', durable=True)

value = 50
i = 0
ids =(1, 2)
while (i < 100):
    valueChange = random.randint(-5, 5)
    value = value + valueChange
    dict_msg = {
        "device": random.choice(list(ids)),
        "value": value,
        "type": "temperature",
        "datetime": str(datetime.now()),
        'status': 'active'
    }
    msg = json.dumps(dict_msg)
    channel.basic_publish(exchange='device-input',
                          routing_key='device/input',
                          body=msg,
                          properties=pika.BasicProperties(
                          delivery_mode = 2,
                          ))
    print(msg)
    time.sleep(1)
    i += 1
    
connection.close()