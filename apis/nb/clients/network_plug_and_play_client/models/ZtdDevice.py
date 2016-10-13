#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdDevice(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'macAddress': 'str',
            
            
            'serialNumber': 'str',
            
            
            'aliases': 'list[str]',
            
            
            'ipAddress': 'str',
            
            
            'versionString': 'str',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'site': 'str',
            
            
            'configId': 'str',
            
            
            'pkiEnabled': 'bool',
            
            
            'imageId': 'str',
            
            
            'fileDestination': 'str',
            
            
            'backoffTimer': 'str',
            
            
            'provisioningType': 'str',
            
            
            'unclaimedHint': 'str',
            
            
            'bootstrapId': 'str',
            
            
            'oldNetworkDeviceId': 'str',
            
            
            'hwRevision': 'str',
            
            
            'mainMemSize': 'str',
            
            
            'boardId': 'str',
            
            
            'boardReworkId': 'str',
            
            
            'midplaneVersion': 'str',
            
            
            'imageFile': 'str',
            
            
            'returnToRomReason': 'str',
            
            
            'bootVariable': 'str',
            
            
            'bootLdrVariable': 'str',
            
            
            'configVariable': 'str',
            
            
            'configReg': 'str',
            
            
            'configRegNext': 'str',
            
            
            'topologyInfo': 'str',
            
            
            'filesystemInfo': 'str',
            
            
            'deviceDetailsLastUpdate': 'str',
            
            
            'slotNumber': 'str',
            
            
            'certificateNeededState': 'str',
            
            
            'pnpProfileUsedAddr': 'str',
            
            
            'pnpProfileUsedHost': 'str',
            
            
            'authStatus': 'DeviceAuthState',
            
            
            'deviceCertificate': 'str',
            
            
            'deviceType': 'str',
            
            
            'memberDetail': 'list[ZtdMemberDetail]',
            
            
            'deviceDiscoveryInfo': 'ZtdDeviceDiscoveryInfo',
            
            
            'licenseString': 'str',
            
            
            'apCount': 'str',
            
            
            'isMobilityController': 'str',
            
            
            'sudiRequired': 'bool',
            
            
            'memberUdi': 'str',
            
            
            'licenseLevel': 'str',
            
            
            'eulaAccepted': 'bool',
            
            
            'lastStateTransitionTime': 'str',
            
            
            'firstContact': 'str',
            
            
            'lastContact': 'str',
            
            
            'cleanup': 'bool',
            
            
            'templateConfigId': 'str',
            
            
            'versionCompatible': 'str',
            
            
            'stateDisplay': 'str',
            
            
            'state': 'str',
            
            
            'hostName': 'str'            
        }

        self.attributeMap = {
            
            'macAddress': 'macAddress',
            
            'serialNumber': 'serialNumber',
            
            'aliases': 'aliases',
            
            'ipAddress': 'ipAddress',
            
            'versionString': 'versionString',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'site': 'site',
            
            'configId': 'configId',
            
            'pkiEnabled': 'pkiEnabled',
            
            'imageId': 'imageId',
            
            'fileDestination': 'fileDestination',
            
            'backoffTimer': 'backoffTimer',
            
            'provisioningType': 'provisioningType',
            
            'unclaimedHint': 'unclaimedHint',
            
            'bootstrapId': 'bootstrapId',
            
            'oldNetworkDeviceId': 'oldNetworkDeviceId',
            
            'hwRevision': 'hwRevision',
            
            'mainMemSize': 'mainMemSize',
            
            'boardId': 'boardId',
            
            'boardReworkId': 'boardReworkId',
            
            'midplaneVersion': 'midplaneVersion',
            
            'imageFile': 'imageFile',
            
            'returnToRomReason': 'returnToRomReason',
            
            'bootVariable': 'bootVariable',
            
            'bootLdrVariable': 'bootLdrVariable',
            
            'configVariable': 'configVariable',
            
            'configReg': 'configReg',
            
            'configRegNext': 'configRegNext',
            
            'topologyInfo': 'topologyInfo',
            
            'filesystemInfo': 'filesystemInfo',
            
            'deviceDetailsLastUpdate': 'deviceDetailsLastUpdate',
            
            'slotNumber': 'slotNumber',
            
            'certificateNeededState': 'certificateNeededState',
            
            'pnpProfileUsedAddr': 'pnpProfileUsedAddr',
            
            'pnpProfileUsedHost': 'pnpProfileUsedHost',
            
            'authStatus': 'authStatus',
            
            'deviceCertificate': 'deviceCertificate',
            
            'deviceType': 'deviceType',
            
            'memberDetail': 'memberDetail',
            
            'deviceDiscoveryInfo': 'deviceDiscoveryInfo',
            
            'licenseString': 'licenseString',
            
            'apCount': 'apCount',
            
            'isMobilityController': 'isMobilityController',
            
            'sudiRequired': 'sudiRequired',
            
            'memberUdi': 'memberUdi',
            
            'licenseLevel': 'licenseLevel',
            
            'eulaAccepted': 'eulaAccepted',
            
            'lastStateTransitionTime': 'lastStateTransitionTime',
            
            'firstContact': 'firstContact',
            
            'lastContact': 'lastContact',
            
            'cleanup': 'cleanup',
            
            'templateConfigId': 'templateConfigId',
            
            'versionCompatible': 'versionCompatible',
            
            'stateDisplay': 'stateDisplay',
            
            'state': 'state',
            
            'hostName': 'hostName'            
        }       

        
        
        self.macAddress = None # str
        
        #Serial number
        
        self.serialNumber = None # str
        
        
        self.aliases = None # list[str]
        
        
        self.ipAddress = None # str
        
        #IOS Version
        
        self.versionString = None # str
        
        #Device ID
        
        self.id = None # str
        
        #Platform ID
        
        self.platformId = None # str
        
        #Project to which device belongs if pre-provisioned
        
        self.site = None # str
        
        #Configuration file ID
        
        self.configId = None # str
        
        #Configure PKCS#12 trust point during PNP workflow if true
        
        self.pkiEnabled = None # bool
        
        #Image file ID
        
        self.imageId = None # str
        
        #Location on device to which image/config files will be copied
        
        self.fileDestination = None # str
        
        #Backoff timer
        
        self.backoffTimer = None # str
        
        #Type of device
        
        self.provisioningType = None # str
        
        #Hint whether device might be RMA
        
        self.unclaimedHint = None # str
        
        #Bootstrap file ID
        
        self.bootstrapId = None # str
        
        #Inventory device of which this device is the replacement
        
        self.oldNetworkDeviceId = None # str
        
        #HW revision
        
        self.hwRevision = None # str
        
        #Main memory size
        
        self.mainMemSize = None # str
        
        #Board ID
        
        self.boardId = None # str
        
        #Board rework ID
        
        self.boardReworkId = None # str
        
        #Mid plane version
        
        self.midplaneVersion = None # str
        
        #Image ID
        
        self.imageFile = None # str
        
        #Return to rom reason
        
        self.returnToRomReason = None # str
        
        #Boot variable
        
        self.bootVariable = None # str
        
        #Boot ldr variable
        
        self.bootLdrVariable = None # str
        
        #Config variable
        
        self.configVariable = None # str
        
        #Config reg
        
        self.configReg = None # str
        
        #Config reg next
        
        self.configRegNext = None # str
        
        #Information about topology
        
        self.topologyInfo = None # str
        
        #Information about filesystem
        
        self.filesystemInfo = None # str
        
        #Timestamp when the device details were last read
        
        self.deviceDetailsLastUpdate = None # str
        
        #Slot number
        
        self.slotNumber = None # str
        
        #State which is detected as happening over http instead of https
        
        self.certificateNeededState = None # str
        
        #PnP server ipv4 address used by pnp profile
        
        self.pnpProfileUsedAddr = None # str
        
        #PnP server hostname used by pnp profile
        
        self.pnpProfileUsedHost = None # str
        
        
        self.authStatus = None # DeviceAuthState
        
        
        self.deviceCertificate = None # str
        
        
        self.deviceType = None # str
        
        
        self.memberDetail = None # list[ZtdMemberDetail]
        
        #Device discovery info
        
        self.deviceDiscoveryInfo = None # ZtdDeviceDiscoveryInfo
        
        #License information
        
        self.licenseString = None # str
        
        #Wireless AP count
        
        self.apCount = None # str
        
        #Specify if device is a wireless mobility controller
        
        self.isMobilityController = None # str
        
        
        self.sudiRequired = None # bool
        
        #Unique device ID of redundant/stack switches
        
        self.memberUdi = None # str
        
        #CLI execution license level
        
        self.licenseLevel = None # str
        
        #CLI execution EULA accepted or not
        
        self.eulaAccepted = None # bool
        
        #Last state transition time of device
        
        self.lastStateTransitionTime = None # str
        
        #First contact time of device
        
        self.firstContact = None # str
        
        #Last contact time of device
        
        self.lastContact = None # str
        
        
        self.cleanup = None # bool
        
        #Template config ID
        
        self.templateConfigId = None # str
        
        
        self.versionCompatible = None # str
        
        
        self.stateDisplay = None # str
        
        #Device state
        
        self.state = None # str
        
        #Host name
        
        self.hostName = None # str        
