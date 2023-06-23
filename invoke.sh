#!/bin/bash

while true; do aws lambda invoke --cli-binary-format raw-in-base64-out --function-name myPythonProvision-myPythonFunction-NlKQVVSyjdul:live --payload file://payload.json response.json && cat response.json && aws lambda get-provisioned-concurrency-config --function-name myPythonProvision-myPythonFunction-NlKQVVSyjdul --qualifier live; done