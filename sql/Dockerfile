FROM ubuntu:19.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y -q apt-utils
RUN apt-get install -y -q postgresql-11

COPY database.sql /data/database.sql

USER postgres
RUN sed -i -e '1ihost    all             django            0.0.0.0/0               md5\' /etc/postgresql/11/main/pg_hba.conf \
    && sed -i -e '1ilocal    all             django                           md5\' /etc/postgresql/11/main/pg_hba.conf \
    && echo "listen_addresses = '*'" >> /etc/postgresql/11/main/postgresql.conf \
    && service postgresql start \
    && psql -c "CREATE ROLE django WITH ENCRYPTED PASSWORD 'django' LOGIN" \
    && createdb -U postgres -O django HOME_IOT \
    && export PGPASSWORD=django \
    && psql -U django -d HOME_IOT < /data/database.sql
USER root

VOLUME ["/etc/postgresql", "/var/lib/postgresql", "/data"]

WORKDIR /data

EXPOSE 5432

COPY starter.sh /starter.sh
RUN chmod 760 /starter.sh
ENTRYPOINT ["/starter.sh"]
