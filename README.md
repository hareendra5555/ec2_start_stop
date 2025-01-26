# **Automating EC2 Instance Management with AWS Lambda**

## **Project Description**
This project demonstrates how to automate the management of AWS EC2 instances using AWS Lambda and Python. It includes Lambda functions to start and stop EC2 instances at scheduled times, triggered by Amazon EventBridge (formerly CloudWatch Events). This project showcases cloud engineering skills, including automation, serverless architecture, and Python scripting.

---

## **Table of Contents**
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Lambda Functions](#lambda-functions)
5. [IAM Role Configuration](#iam-role-configuration)
6. [CloudWatch EventBridge Setup](#cloudwatch-eventbridge-setup)
7. [Testing](#testing)
8. [Future Enhancements](#future-enhancements)

---

## **Features**
- Automates starting and stopping EC2 instances.
- Uses AWS Lambda for serverless execution.
- Scheduled triggers via Amazon EventBridge.
- Logs execution details to Amazon CloudWatch.

---

## **Technologies Used**
- **AWS Services**: Lambda, EC2, EventBridge (CloudWatch Events), IAM, CloudWatch.
- **Programming Language**: Python 3.x.
- **Python Libraries**: Boto3 (AWS SDK for Python).

---

## **Setup Instructions**

### **1. Prerequisites**
- An active AWS account.
- IAM role with permissions for EC2 management and CloudWatch logging.
- Python environment installed locally.

### **2. Deploy Lambda Functions**
1. Create two separate Lambda functions in the AWS Management Console:
   - One for starting EC2 instances (`StartEC2Instances`).
   - One for stopping EC2 instances (`StopEC2Instances`).
2. Use the provided code snippets in the [Lambda Functions](#lambda-functions) section.

### **3. Attach IAM Role**
Attach an IAM role to your Lambda functions with the required permissions (see [IAM Role Configuration](#iam-role-configuration)).

### **4. Configure CloudWatch EventBridge Rules**
Set up EventBridge rules to trigger the Lambda functions at your desired schedule (see [CloudWatch EventBridge Setup](#cloudwatch-eventbridge-setup)).

---

## **Lambda Functions**

### **1. Start EC2 Instances**
This function starts specified EC2 instances.


### **2. Stop EC2 Instances**
This function stops specified EC2 instances.


---

## **IAM Role Configuration**

### **1. Trust Policy**
This allows AWS Lambda to assume the role.


### **2. Permissions Policy**
This grants permissions for managing EC2 instances and logging to CloudWatch.


---

## **CloudWatch EventBridge Setup**

### Steps to Create Scheduled Triggers:
1. Go to the **Amazon EventBridge** console.
2. Click on **Rules** → **Create Rule**.
3. Provide a name for the rule (e.g., `StartEC2Schedule` or `StopEC2Schedule`).
4. Under **Define pattern**, select **Schedule** and set a cron expression:
   - Example to run daily at 6 AM UTC: `cron(0 6 * * ? *)`
   - Example to run daily at 6 PM UTC: `cron(0 18 * * ? *)`
5. Under **Select targets**, choose:
   - Target type: `Lambda function`.
   - Select the appropriate Lambda function (`StartEC2Instances` or `StopEC2Instances`).
6. Save the rule.

---

## **Testing**

### Manual Testing via AWS Console:
1. Navigate to your Lambda function in the AWS Management Console.
2. Click on the **Test** button and create a test event with an empty payload (`{}`).
3. Trigger the function by clicking **Test**.
4. Verify that the EC2 instance state changes in the EC2 dashboard:
   - If running `StartEC2Instances`, check that the instance state is `running`.
   - If running `StopEC2Instances`, check that the instance state is `stopped`.

### Logs:
Check execution logs in Amazon CloudWatch:
1. Go to CloudWatch → Log Groups → `/aws/lambda/<FunctionName>`.
2. Review logs for any errors or messages.

---

## **Future Enhancements**
- Add functionality to dynamically select instances based on tags.
- Implement SNS notifications for status updates.
- Add error handling and retry mechanisms using AWS Step Functions.
- Extend automation to other AWS services like RDS or S3.

