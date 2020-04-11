# aws-management-functions

This project contains source code and supporting files for a series of Lambda function you can use to manage you AWS environment.

## EC2 Instances
You can use the StopEC2Function and StartEC2Function Lambda functions to stop/start EC2 instances on-demand or based on CloudWatch Schedule events.

By default, after deploying the project the StopEC2Function will run every night at 10PM CST.

You can use the EC2_REGION environment variable to specify which region you want to manage or remove the variable if you want to manage EC2 instances on all the AWS regions at once.

You can use the EC2_TAG variable to manage instances based on a specific tag name.

## Deploy application

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
