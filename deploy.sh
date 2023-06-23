#! /bin/bash

rm package.yml

sam package \
  --template-file template.yml \
  --output-template-file package.yml \
  --s3-bucket sam-sourcecode-gmthomp

sam deploy \
  --template-file package.yml \
  --stack-name myPythonProvision \
  --capabilities CAPABILITY_IAM