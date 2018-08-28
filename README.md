# AWS IoT Device Registration using Lambda Example

This is an example of creating AWS IoT Device and generate Certificate using Lambda.

## Use Case
Set up "Thing" automatically and register to AWS IoT by executing Lambda Function. This is very useful when you have to register a lot of devices at a factory or something.

## Notes
- The security is very important. So you have to make sure that anyone can NOT call this Lambda without any permission. (ex: in case using API Gateway, you can use API Key or Custom Authorizer)

## Set Up
- Create ThingType
- Create Policy

## How to run locally
- Run following command
```
$ sls invoke local -f registerDeviceToAWSIoT -d '{"thingName":"thing001","thingType":"test-thing-type","policy":"test-device-policy"}'
```

## How to deploy
- Run following command
```
$ serverless deploy
```
- execute lambda using AWS Console

