docker exec -it postgres_mqtt_ia_concept /bin/sh /setup.sh

python3 -m venv .venv

pwd

. .venv/bin/activate

pip install -r requirements.txt