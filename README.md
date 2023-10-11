# AWS Metrics to RDS

AWS Metrics to RDS is a Python utility to extract CloudWatch EC2 metrics data and store it on the RDS .

## Features:

Extract metric data from all EC2 instances of the selected region

Save output to csv file

## Upcoming Features:
Extract CPU metric data from all RDS instances of the selected region

Customize parameters: period, days and filename

Command line utility

Lambda Function

## Architeture
![EC2_metrics_to_RDS](https://github.com/Sampath005/AWS-CW-metrics-to-RDS/assets/97429122/a45d13b8-b1ac-4cb1-8e01-04e29b6f1586)

## Install packages:

```bash
pip install -r requirements.txt
```

## Install AWS CLI:

```bash
pip install awscli
```

## Configure the AWS CLI:

```bash
aws configure
```

## Usage

```bash
python3 CloudWatchMatrics.py
```

This will create the ec2.csv file.

## Issues
StopIteration - when no resource are running
