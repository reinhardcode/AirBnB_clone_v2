#!/usr/bin/env bash
# bash sscript that sets up the server for deplyment
# -----update the rest-----

# install Nginx
sudo apt update
sudo apt install -y nginx
sudo ufw allow 'Nginx HTTP'
sudo service nginx start

# create ---- folder for test i guess
sudo mkdir -p /data/web_static/releases/test/
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

sudo mkdir -p /data/web_static/shared/
echo "$content" > /data/web_static/releases/test/index.html

#creatnig a symbolic link that links /data/web_static/current
# -to /data/web_static/releases/test/
ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership of the data folder to the ubuntu user <rescursive>
sudo chown -R ubuntu:ubuntu /data/

#update the nginx config file to serve content of /data/web_static/current/
# to hbnb_static  ex (https://mydomainname.tech/hbnb_static)
# create a new conf file for teh server that will get included in the
# nginx.conf
conf="
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        index index.html index.htm index.nginx-debian.html;
        server_name reinhardservices.tech;
        root /data/web_static/current/;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }

}"

FILE=/etc/nginx/sites-enabled/default
if test -f "$FILE";
then
    sudo unlink $FILE
fi

echo "$conf" > /etc/nginx/sites-enabled/reinhard
sudo nginx -s reload