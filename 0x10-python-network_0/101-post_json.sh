#!/bin/bash
#JSON
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"