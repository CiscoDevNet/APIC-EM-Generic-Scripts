#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ApplicationDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'url': 'str',
            
            
            'category': 'str',
            
            
            'trafficClass': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'rank': 'int',
            
            
            'appProtocol': 'str',
            
            
            'applicationIpPortClassifiers': 'list[ApplicationIpPortClassifierDTO]',
            
            
            'tcpPorts': 'str',
            
            
            'indicativeTcpPorts': 'str',
            
            
            'udpPorts': 'str',
            
            
            'indicativeUdpPorts': 'str',
            
            
            'transportIps': 'str',
            
            
            'status': 'str',
            
            
            'longDescription': 'str',
            
            
            'ipPorts': 'str',
            
            
            'categoryId': 'str',
            
            
            'subCategory': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'dscp': 'str',
            
            
            'globalId': 'str',
            
            
            'engineId': 'str',
            
            
            'selectorId': 'str',
            
            
            'helpString': 'str',
            
            
            'references': 'str',
            
            
            'applicationGroup': 'str',
            
            
            'encrypted': 'str',
            
            
            'tunnel': 'str',
            
            
            'pfrThresholdJitter': 'int',
            
            
            'pfrThresholdLossRate': 'int',
            
            
            'pfrThresholdOneWayDelay': 'int',
            
            
            'popularity': 'int',
            
            
            'enabled': 'str',
            
            
            'indicativeIpPorts': 'str',
            
            
            'isRepresentativeApp': 'bool',
            
            
            'nbarId': 'str',
            
            
            'p2pTechnology': 'str',
            
            
            'pfrThresholdJitterPriority': 'int',
            
            
            'pfrThresholdLossRatePriority': 'int',
            
            
            'pfrThresholdOneWayDelayPriority': 'int',
            
            
            'ignoreConflict': 'bool'
            
        }

        self.attributeMap = {
            
            'url': 'url',
            
            'category': 'category',
            
            'trafficClass': 'trafficClass',
            
            'name': 'name',
            
            'id': 'id',
            
            'rank': 'rank',
            
            'appProtocol': 'appProtocol',
            
            'applicationIpPortClassifiers': 'applicationIpPortClassifiers',
            
            'tcpPorts': 'tcpPorts',
            
            'indicativeTcpPorts': 'indicativeTcpPorts',
            
            'udpPorts': 'udpPorts',
            
            'indicativeUdpPorts': 'indicativeUdpPorts',
            
            'transportIps': 'transportIps',
            
            'status': 'status',
            
            'longDescription': 'longDescription',
            
            'ipPorts': 'ipPorts',
            
            'categoryId': 'categoryId',
            
            'subCategory': 'subCategory',
            
            'instanceUuid': 'instanceUuid',
            
            'dscp': 'dscp',
            
            'globalId': 'globalId',
            
            'engineId': 'engineId',
            
            'selectorId': 'selectorId',
            
            'helpString': 'helpString',
            
            'references': 'references',
            
            'applicationGroup': 'applicationGroup',
            
            'encrypted': 'encrypted',
            
            'tunnel': 'tunnel',
            
            'pfrThresholdJitter': 'pfrThresholdJitter',
            
            'pfrThresholdLossRate': 'pfrThresholdLossRate',
            
            'pfrThresholdOneWayDelay': 'pfrThresholdOneWayDelay',
            
            'popularity': 'popularity',
            
            'enabled': 'enabled',
            
            'indicativeIpPorts': 'indicativeIpPorts',
            
            'isRepresentativeApp': 'isRepresentativeApp',
            
            'nbarId': 'nbarId',
            
            'p2pTechnology': 'p2pTechnology',
            
            'pfrThresholdJitterPriority': 'pfrThresholdJitterPriority',
            
            'pfrThresholdLossRatePriority': 'pfrThresholdLossRatePriority',
            
            'pfrThresholdOneWayDelayPriority': 'pfrThresholdOneWayDelayPriority',
            
            'ignoreConflict': 'ignoreConflict'
            
        }       

        
        #url of the app
        
        self.url = None # str
        
        #Category name
        
        self.category = None # str
        
        #Traffic class to which the app belongs
        
        self.trafficClass = None # str
        
        #App Name
        
        self.name = None # str
        
        #id
        
        self.id = None # str
        
        #rank
        
        self.rank = None # int
        
        #protocol of the app. Valid values are tcp, udp, tcp/udp, ip or it could be empty. Values are case sensitive.
        
        self.appProtocol = None # str
        
        #IP Port classifiers for the application
        
        self.applicationIpPortClassifiers = None # list[ApplicationIpPortClassifierDTO]
        
        #list of tcp ports
        
        self.tcpPorts = None # str
        
        #Indicative tcp ports
        
        self.indicativeTcpPorts = None # str
        
        #list of udp ports
        
        self.udpPorts = None # str
        
        #Indicative udp ports
        
        self.indicativeUdpPorts = None # str
        
        #Transport IP of the app
        
        self.transportIps = None # str
        
        #Gives status of the app
        
        self.status = None # str
        
        #Long description of the app
        
        self.longDescription = None # str
        
        #list of ip ports
        
        self.ipPorts = None # str
        
        #Category id
        
        self.categoryId = None # str
        
        #Sub-Category Id
        
        self.subCategory = None # str
        
        #
        
        self.instanceUuid = None # str
        
        #dscp value
        
        self.dscp = None # str
        
        #global id
        
        self.globalId = None # str
        
        #engine id
        
        self.engineId = None # str
        
        #selector id
        
        self.selectorId = None # str
        
        #help string to describe the app
        
        self.helpString = None # str
        
        #references of the app
        
        self.references = None # str
        
        #App group name
        
        self.applicationGroup = None # str
        
        #If the app is encrypted
        
        self.encrypted = None # str
        
        #If the app is a tunnel
        
        self.tunnel = None # str
        
        #PfR Threshold Jitter
        
        self.pfrThresholdJitter = None # int
        
        #PfR Threshold Loss Rate
        
        self.pfrThresholdLossRate = None # int
        
        #PfR Threshold One Way Delay
        
        self.pfrThresholdOneWayDelay = None # int
        
        #popularity of the app
        
        self.popularity = None # int
        
        #If the app enabled
        
        self.enabled = None # str
        
        #Indicative ip ports
        
        self.indicativeIpPorts = None # str
        
        #If the app is representative
        
        self.isRepresentativeApp = None # bool
        
        #nbar id
        
        self.nbarId = None # str
        
        #If the app is a p2p technology
        
        self.p2pTechnology = None # str
        
        #PfR Threshold Jitter Priority
        
        self.pfrThresholdJitterPriority = None # int
        
        #PfR Threshold Loss Rate Priority
        
        self.pfrThresholdLossRatePriority = None # int
        
        #PfR Threshold One Way Delay Priority
        
        self.pfrThresholdOneWayDelayPriority = None # int
        
        #If true ignore conflicts with other Applications
        
        self.ignoreConflict = None # bool
        
