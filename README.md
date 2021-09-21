# How to use Parameters in AWS CDK Python
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This is a repository to rewrite [bobbyhadz/aws-cdk-parameters-example \(TypeScript\)](https://github.com/bobbyhadz/aws-cdk-parameters-example) in Python.<br/>
Please checkout [bobbyhadz/aws-cdk-parameters-example \(Typescript\)](https://github.com/bobbyhadz/aws-cdk-parameters-example) and [How to use Parameters in AWS CDK - Complete Guide \(2021-04-23\)](https://bobbyhadz.com/blog/aws-cdk-parameters-example), if you want to see the original source code.

## How to use

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

<pre>
$ export CDK_DEFAULT_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
$ export CDK_DEFAULT_REGION=$(curl -s 169.254.169.254/latest/dynamic/instance-identity/document | jq -r .region)
$ cdk synth \
    --parameters databasePort=3306 \
    --parameters dynamoDBTableName=MyDynamoTable \
    --parameters favoriteRegions="us-east-1,us-west-2"
</pre>

If you generate a CloudFormation template based on our current CDK app, you would see the plain CloudFormation Parameters section:

<pre>
Parameters:
  databasePort:
    Type: Number
    Default: 3306
    AllowedValues:
      - "1000"
      - "3000"
      - "3306"
    Description: The database port to open for ingress connections
    MaxValue: 10000
    MinValue: 1
  dynamoDBTableName:
    Type: String
    Description: The name of the DynamoDB table
  favoriteRegions:
    Type: CommaDelimitedList
    Description: An array of regions
</pre>

Use `cdk deploy` command to create the stack shown above.

<pre>
$ cdk deploy \
    --parameters databasePort=3306 \
    --parameters dynamoDBTableName=MyDynamoTable \
    --parameters favoriteRegions="us-east-1,us-west-2"
</pre>

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

### Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

## References

 * [How to use Parameters in AWS CDK - Complete Guide \(2021-04-23\)](https://bobbyhadz.com/blog/aws-cdk-parameters-example)
 * [bobbyhadz/aws-cdk-parameters-example \(TypeScript\)](https://github.com/bobbyhadz/aws-cdk-parameters-example)

