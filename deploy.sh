/usr/bin/docker build --tag lukassimonis_net .
/usr/bin/docker stop lukassimonis_net_django
/usr/bin/docker rm lukassimonis_net_django
/usr/bin/docker run -d --name=lukassimonis_net_django -e DJANGO_SECRET -e MYSQL_PASSWORD --restart=always -p 8000:8000 -t lukassimonis_net
