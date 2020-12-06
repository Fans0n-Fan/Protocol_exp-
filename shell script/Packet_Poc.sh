#!/bin/sh
echo "run POC"
curlCmd ="curl -H 'header' -H 'cookies' http://demo -d 'data'
eval $curlCmd

