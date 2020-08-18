#!/bin/bash
#OPTIONS
curl -sI -X OPTIONS "$1" | awk '$1=="Allow:" {print $2, $3, $4}'
