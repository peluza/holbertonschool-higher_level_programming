#!/bin/bash
#OPTIONS
curl -s -v "$1" -i | awk '$1=="Allow:" {print $2, $3, $4}'
