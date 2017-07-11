
# Farm Finder Catalog Site ![Site Logo](https://github.com/lmitchell4/farm-finder/blob/master/itemcatalog/static/images/logo.png)

## Overview

This is a version of the [Farm Finder](https://github.com/lmitchell4/farm-finder) 
project configured to use Postgresql instead of SQLite and run on 
an Apache server. A copy of the site is currently being hosted on Amazon Lightsail.

The IP address is `34.209.131.9` and the complete URL is 

[http://ec2-34-209-131-9.us-west-2.compute.amazonaws.com/login](http://ec2-34-209-131-9.us-west-2.compute.amazonaws.com/login)


## Software

To host the site you will need to install the following packages:

  ```
  apt-get install libapache2-mod-wsgi

  apt-get install libpq-dev python-dev
  apt-get install postgresql python-psycopg2
  apt-get install postgresql-contrib
  apt-get install python-oauth2client

  pip install sqlalchemy
  pip install flask
  pip install psycopg2
  pip install bleach
  pip install requests
  pip install httplib2
  pip install redis
  pip install passlib
  pip install itsdangerous
  pip install flask-httpauth
  ```


## Configuration

Next, create an Apache configuration file for the project:

  ```
  $ sudo vim /etc/apache2/sites-available/ItemCatalog.conf
  ```

and put the following in the file:

  ```
  <VirtualHost *:80>
      ServerName mywebsite.com
      ServerAdmin admin@mywebsite.com
      WSGIScriptAlias / /my_path/itemcatalog/flaskapp.wsgi
      DocumentRoot /my_path/itemcatalog
      <Directory /my_path/itemcatalog/itemcatalog>
          Order allow,deny
          Allow from all
      </Directory>
      Alias /static /my_path/itemcatalog/itemcatalog/static
      <Directory /my_path/itemcatalog/itemcatalog/static/>
          Order allow,deny
          Allow from all
      </Directory>
      ErrorLog ${APACHE_LOG_DIR}/error.log
      LogLevel warn
      CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```

Replace `my_path` with the appropriate path on your server and make any 
further changes you would like, then run the following to enable the 
VirtualHost:

  ```
  $ sudo a2ensite ItemCatalog
  ```

If the default VirtualHost is set to the same port you want to use for 
ItemCatalog, you may need to disable the default VirtualHost by running the 
following:

  ```
  $ sudo a2dissite 000-default.conf
  ```

or chaning the default's port.


## Other Resources

The project uses [Flask](http://flask.pocoo.org/) and 
[Bootstrap](http://getbootstrap.com/css/).

