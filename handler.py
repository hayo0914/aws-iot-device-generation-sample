import json
import device_manager

def generateCert(event, context):
    deviceManager = device_manager.DeviceManager()
    device = deviceManager.createThing('test123456')
    keysAndCertificate = deviceManager.createKeysAndCertificate()

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
