#!/bin/bash
#OPTIONS
curl -s -X OPTIONS "$1" -i | awk '$1=="Allow:" {print $2, $3, $4}'
