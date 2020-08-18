#!/bin/bash
#JSON
curl -s -X PUT -H "Content-Type: application/json" -d @"$2" "$1"
