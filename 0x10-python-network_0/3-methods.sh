#!/bin/bash
#OPTIONS
curl -s -i "$1" | awk '$1=="Allow:" {print $2, $3, $4}'
