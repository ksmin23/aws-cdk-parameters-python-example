#!/usr/bin/env python3
import os

from aws_cdk import (
  core as cdk,
  aws_dynamodb,
  aws_lambda
)

from aws_cdk.aws_lambda_python import PythonFunction


class CdkParametersStack(cdk.Stack):

  def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    #XXX: parameter of type Number
    database_port = cdk.CfnParameter(self, 'databasePort',
      type='Number',
      description='The database port to open for ingress connections',
      min_value=1,
      max_value=10000,
      default=3306,
      allowed_values=['1000', '3000', '3306']
    )

    #XXX: parameter of type String
    ddb_table_name = cdk.CfnParameter(self, 'dynamoDBTableName',
      type='String',
      description='The name of the DynamoDB table'
    )

    ddb_table = aws_dynamodb.Table(self, 'MyDynamoDBTable',
      table_name=ddb_table_name.value_as_string,
      removal_policy=cdk.RemovalPolicy.DESTROY,
      partition_key=aws_dynamodb.Attribute(name='pkid',
        type=aws_dynamodb.AttributeType.STRING),
      sort_key=aws_dynamodb.Attribute(name='sortkey',
        type=aws_dynamodb.AttributeType.NUMBER),
      time_to_live_attribute='ttl',
      billing_mode=aws_dynamodb.BillingMode.PROVISIONED,
      read_capacity=15,
      write_capacity=5,
    )

    _lambda_fn = PythonFunction(self, 'MyLambdaFunction',
      environment={
        'databasePort': database_port.value_as_string,
        'ddbTableName': ddb_table_name.value_as_string
      },
      entry=os.path.join(os.path.dirname(__file__), 'src/main/python'),
      index='my_lambda_fn.py', # optional, defaults to 'index.py'
      handler='lambda_handler', # optional, defaults to 'handler'
      runtime=aws_lambda.Runtime.PYTHON_3_7
    )

    #XXX: parameter of type CommaDelimitedList
    favorite_regions = cdk.CfnParameter(self, 'favoriteRegions',
      type='CommaDelimitedList',
      description='An array of regions'
    )


app = cdk.App()
CdkParametersStack(app, "CdkParametersPythonExampleStack",
  env=cdk.Environment(
    account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION'))
)

app.synth()
