#!/usr/bin/env bash
#displays the size of the body of the response
curl -sI klase.tech | head -n 5 | tail -n 1 | awk '{print $2}'