FROM postgres:11.5

COPY ./init.sql /setup/
COPY ./setup.sh .

RUN chmod +x setup.sh