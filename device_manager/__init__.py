import boto3

class DeviceManager:

    def __init__(self):
        self.client = boto3.client('iot')
        self.certificateArn = ""
        self.certificateId = ""
        self.certificatePem = ""
        self.keyPair = {
            'PublicKey': "",
            'PrivateKey': ""
        }
        self.thingName = ""
        self.thingArn = ""
        self.thingId = ""
    
    def createThing(self, thingName, thingTypeName):
        response = self.client.create_thing(
            thingName = thingName,
            thingTypeName = thingTypeName,
            attributePayload = {
                'attributes': {
                    'test': '1'
                },
            }
        )
        self.thingName = response['thingName']
        self.thingArn = response['thingArn']
        self.thingId = response['thingId']
        return response

    def createKeysAndCertificate(self):
        response = self.client.create_keys_and_certificate(
            setAsActive=True
        )
        self.certificateArn = response['certificateArn']
        self.certificateId = response['certificateId']
        self.certificatePem = response['certificatePem']
        self.keyPair = response['keyPair']
        return response
    
    def attachThingPrincipal(self):
        self.client.attach_thing_principal(
            thingName = self.thingName,
            principal = self.certificateArn
        )

    def attachPolicy(self, policyName):
        self.client.attach_policy(
            policyName = policyName,
            target = self.certificateArn
        )
