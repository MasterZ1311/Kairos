# KAIROS 2027 — AWS Bedrock Sandbox Automated Provisioning Runbook

> **Engineer:** Shanmugapriyan S (Technical Lead, Reg: `44111257`)  
> **Master Admin:** Thenappan T (Reg: `44110855`)  

---

## 1. Automated Account Spawning Script (AWS CLI / Python boto3)

```python
"""
kairos_sandbox_spawner.py
Automates creation of 100 AWS member accounts inside 'Hackathon Teams OU'
with pre-configured Bedrock IAM policies and budget caps.
"""
import boto3

organizations = boto3.client('organizations')
budgets = boto3.client('budgets')

def spawn_team_account(team_id, team_name, lead_email):
    account_name = f"Kairos2027-Team-{team_id}"
    print(f"Provisioning {account_name} for {lead_email}...")
    
    # 1. Create AWS Account
    resp = organizations.create_account(
        Email=f"kairos-team-{team_id}@sistawscc.org",
        AccountName=account_name,
        RoleName="OrganizationAccountAccessRole"
    )
    # 2. Attach Bedrock Sandbox SCP
    # 3. Provision $150 Budget Alert
    return resp
```

---

## 2. Service Control Policy (SCP): Bedrock & Serverless Only

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowHackathonServicesOnly",
      "Effect": "Deny",
      "NotAction": [
        "bedrock:*",
        "lambda:*",
        "apigateway:*",
        "s3:*",
        "dynamodb:*",
        "cognito-idp:*",
        "cloudfront:*",
        "cloudwatch:*",
        "logs:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyUnauthorizedRegions",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": ["us-east-1", "ap-south-1"]
        }
      }
    }
  ]
}
```
