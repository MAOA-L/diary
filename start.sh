#!/bin/bash
python manage.py collectstatic
uwsgi --ini uwsgi3031.ini
