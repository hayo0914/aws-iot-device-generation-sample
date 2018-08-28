import boto3

class DeviceManager:
    POLICY_NAME = 'test-device-policy'
    THING_TYPE_NAME = 'test-thing'

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
    
    def createThing(self, thingName):
        response = self.client.create_thing(
            thingName = thingName,
            thingTypeName = self.THING_TYPE_NAME,
            attributePayload = {
                'attributes': {
                    'test': '1'
                },
            }
        )
        self.certificateArn = response['certificateArn']
        self.certificateId = response['certificateId']
        self.certificatePem = response['certificatePem ']
        self.keyPair = response['keyPair']
        return response

    def createKeysAndCertificate(self):
        response = self.client.create_keys_and_certificate(
            setAsActive=True
        )
        self.thingName = response['thingName']
        self.thingArn = response['thingArn']
        self.thingId = response['thingId']
        return response
    
    def attachThingPrincipal(self):
        self.client.attach_thing_principal(
            thingName = this.thingName,
            principal = certificateArn
        )

    def attachPolicy(self):
        self.client.attach_policy(
            policyName = self.POLICY_NAME,
            target = self.certificateArn
        )
