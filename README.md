# AWS IoT Device Registration using Lambda Example

This is an example of creating AWS IoT Device and generate Certificate using Lambda.

## Use Case
Set up "Thing" automatically and register to AWS IoT by executing Lambda Function which must be secured by some measures (ex: in case using API Gateway, you can use API Key or Custom Authorizer)

## Set Up
- Create ThingType
- Create Policy

## How to run locally
- Run following command
```
$ sls invoke local -f generateCert -d '{"thingName":"thing001","thingType":"test-thing-type","policy":"test-device-policy"}'
```

## How to deploy
- Run following command
```
$ serverless deploy
```
- execute lambda using AWS Console

