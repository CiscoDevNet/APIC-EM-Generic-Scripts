#!/usr/bin/env python
#pylint: skip-file
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class Package(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'specificationTitle': 'str',
            
            
            'specificationVersion': 'str',
            
            
            'specificationVendor': 'str',
            
            
            'implementationTitle': 'str',
            
            
            'implementationVersion': 'str',
            
            
            'implementationVendor': 'str',
            
            
            'name': 'str',
            
            
            'annotations': 'list[Annotation]',
            
            
            'declaredAnnotations': 'list[Annotation]',
            
            
            'sealed': 'bool'
            
        }

        self.attributeMap = {
            
            'specificationTitle': 'specificationTitle',
            
            'specificationVersion': 'specificationVersion',
            
            'specificationVendor': 'specificationVendor',
            
            'implementationTitle': 'implementationTitle',
            
            'implementationVersion': 'implementationVersion',
            
            'implementationVendor': 'implementationVendor',
            
            'name': 'name',
            
            'annotations': 'annotations',
            
            'declaredAnnotations': 'declaredAnnotations',
            
            'sealed': 'sealed'
            
        }       

        
        
        self.specificationTitle = None # str
        
        
        self.specificationVersion = None # str
        
        
        self.specificationVendor = None # str
        
        
        self.implementationTitle = None # str
        
        
        self.implementationVersion = None # str
        
        
        self.implementationVendor = None # str
        
        
        self.name = None # str
        
        
        self.annotations = None # list[Annotation]
        
        
        self.declaredAnnotations = None # list[Annotation]
        
        
        self.sealed = None # bool
        
