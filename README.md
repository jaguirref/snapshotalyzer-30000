# snapshotalyzer-30000
demo project to manage AWS EC2 instance snapshots

## About
usage of boto3 to manage AWS EC2 instance snapshots

## Configuring
shotty uses the config file from AWS cli.

`aws configure --profile shotty`

## Running 

`pipenv run python shotty/shotty.py <command> <--project=PROJECT>`

*command* is list, start, stop
*project* is optional