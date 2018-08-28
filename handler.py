import json
import device_manager

def generateCert(event, context):
    """
    Assume event contains thingName of the thing which will be created
    """
    deviceManager = device_manager.DeviceManager()
    deviceManager.createThing(event["thingName"])
    deviceManager.createKeysAndCertificate()
    deviceManager.attachThingPrincipal()
    deviceManager.attachPolicy()
    body = {
        "certificateArn" : deviceManager.certificateArn,
        "certificateId"  : deviceManager.certificateId,
        "certificatePem" : deviceManager.certificatePem,
        "keyPair"        : deviceManager.keyPair,
        "thingName"      : deviceManager.thingName,
        "thingArn"       : deviceManager.thingArn,
        "thingId"        : deviceManager.thingId,
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
