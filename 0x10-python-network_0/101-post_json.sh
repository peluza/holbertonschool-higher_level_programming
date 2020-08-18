#!/bin/bash
#JSON
curl -s -X PUT -H "Content-Type: application/json" -X POST -d @"$2" "$1"