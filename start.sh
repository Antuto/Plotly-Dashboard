#!/bin/sh
gunicorn --bind 0.0.0.0:8050 main:server