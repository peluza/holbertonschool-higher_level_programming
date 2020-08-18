#!/bin/bash
#http_code
curl -s -o /dev/null -w "%{http_code}" "$1"