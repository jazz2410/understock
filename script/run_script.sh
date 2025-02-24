#!/bin/bash
source /var/www/understock/script/.venv/bin/activate
python /var/www/understock/script/write_data.py
deactivate
