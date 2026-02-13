#!/usr/bin/env bash

# backend
source venv/Scripts/activate
which pip
cd main
python manage.py runserver &
BACK_PID=$!

# ждём оба процесса
wait $BACK_PID $FRONT_PID
