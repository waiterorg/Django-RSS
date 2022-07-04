# Django-RSS
Django RSS gather news from a list of RSS urls which are stored database.
This will be run every hour to gather new news.
## Setup
1. Either fork or download the app and open the folder in the cli.
2. Make sure you have the Docker app running on your computer, you can download docker from [here](https://www.docker.com/products/docker-desktop).
3. run this command to start the multicontainer application `docker-compose up`.
Note : For easy access sqlite db is in source .

## How to use
1. Follow link `http://127.0.0.1:8000/admin/`
<br /> Note : For easy access i create a user with `username : root` and `password : 123` .
2. Go `http://127.0.0.1:8000/admin/core/rss/`
3. Put some rss urls for example `https://www1.cbn.com/rss-cbn-articles-cbnnews.xml`.
<br /> Note : Some urls need VPN if you're from Iran .
4. Every hour on minutes 0, news be updated .

## Get news and updated that moment
If you want get news that moment:
1. Follow `http://127.0.0.1:8000/api/token/` and post username and password and get access token.
<br /> Note : For easy access i create a user with `username : root` and `password : 123`
2. Use JWT access token for `http://127.0.0.1:8000/` with POST method.
3. News are updated and you can get from `http://127.0.0.1:8000/news/`.
<br /> Note : For next page you can follow `http://127.0.0.1:8000/news/?page=2`

## Technologies
  - [Python](https://www.python.org/)
  - [Django](https://www.djangoproject.com/)
  - [Redis](https://redis.com/)
  - [Celery](https://docs.celeryq.dev/)
  - [DRF](https://www.django-rest-framework.org/)
  - [Docker](https://www.docker.com/)
