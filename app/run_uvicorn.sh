#!/bin/bash
uvicorn main:app --workers 2 --port 8080 --log-config log.ini --reload
