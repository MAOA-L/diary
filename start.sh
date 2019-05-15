#!/bin/bash
python manage.py collectstatic
uwsgi yourfile.ini
