import json
import logging
import boto3
import os
import sys
import time

def handler(event, context):
    print(json.dumps(event))
    status = 'Succeeded'
    deploymentId = event['DeploymentId']
    hooksExecutionId = event['LifecycleEventHookExecutionId']

    codedeploy = boto3.client('codedeploy')
    lambdaClient = boto3.client('lambda')

    response = lambdaClient.update_alias(
        FunctionName='myPythonProvision-myPythonFunction-NlKQVVSyjdul',
        Name='live',
        FunctionVersion='12',
        RoutingConfig={
            'AdditionalVersionWeights': {
                '13': 0
            }
        }
    )

    time.sleep(60)

    response = codedeploy.put_lifecycle_event_hook_execution_status(
                              deploymentId=deploymentId,
                              lifecycleEventHookExecutionId=hooksExecutionId,
                              status=status
                          )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }