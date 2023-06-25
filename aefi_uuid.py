# -*- coding: utf-8 -*-

import uuid

class AefiUuid():
    
    __aefi_namespace: str = 'http://ops.org/esavi/'
    __contry_code: str = ''
    
    def __init__(self, country_code: str):
        self.__contry_code = country_code
    
    def generate_aefi_id(self, seed: str) -> uuid.uuid5:
        """Generate a AEFi UUID."""
        return uuid.uuid5(uuid.NAMESPACE_DNS, '{0}/{1}/{2}'.format(
            self.__aefi_namespace, 
            self.__contry_code, 
            seed
        ))
    
    def generate_aefi_patient_id(self, seed: str) -> uuid.uuid5:
        """Generate a AEFi Patient UUID."""
        return uuid.uuid5(uuid.NAMESPACE_DNS, '{0}/{1}/paciente/{2}'.format(
            self.__aefi_namespace, 
            self.__contry_code, 
            seed
        ))
