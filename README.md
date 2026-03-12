# AWS CloudTrail and Lambda Security Automation

AWS security automation using CloudTrail, Lambda, and EventBridge to monitor and enforce cloud trail logging policies.

## Project Overview

This project demonstrates event-driven security automation in AWS, using Lambda functions triggered by EventBridge to automatically enforce CloudTrail logging when it is disabled.

## What It Does

- Creates and configures AWS CloudTrail trails
- Enforces S3 bucket policies for log storage
- Deploys Lambda functions to automatically restart disabled trails
- Monitors trail logging status programmatically

## Technologies Used

- Python 3
- AWS Lambda
- AWS CloudTrail
- AWS EventBridge
- AWS S3
- Boto3 SDK

## Prerequisites

- Python 3 installed
- AWS CLI configured with valid credentials
- Required packages: `pip install -r requirements.txt`