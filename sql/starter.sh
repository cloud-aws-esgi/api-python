#!/bin/bash
sed -i -e '1ihost    all             django            0.0.0.0/0               md5\' /etc/postgresql/11/main/pg_hba.conf
sed -i -e '1ilocal    all             django                           md5\' /etc/postgresql/11/main/pg_hba.conf
echo "listen_addresses = '*'" >> /etc/postgresql/11/main/postgresql.conf

service postgresql start
exec /bin/bash