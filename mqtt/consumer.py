import pika, sys, os, json
from decouple import config
from datetime import datetime
import requests

def main():
    credentials = pika.PlainCredentials(username=config('RABBITMQ_DEFAULT_USER'), password=config('RABBITMQ_DEFAULT_PASS'))
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=config('RABBITMQ_DEFAULT_HOST'), credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='input_data', durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % json.loads(body))
        data = json.loads(body)
        headers = {'Content-Type': 'application/json'}
        r = requests.post('http://localhost:8000/inputdata/', data=json.dumps(data), headers=headers)
        print(r.status_code)
        print(r.json())

    channel.basic_consume(queue='input_data', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)