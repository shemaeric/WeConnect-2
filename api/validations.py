'''
Validations Methods Class
'''

import re


class Validations():
    '''Validations class'''

    def __init__(self, all_inputs):
        ''' All inputs dictionary should be available to the class'''
        for key, value in all_inputs.items():
            if (all_inputs[key] is not None and
                    not isinstance(all_inputs[key], int)):
                if all_inputs[key].strip() is '':
                    all_inputs[key] = None
        self.all = all_inputs

    def string(self, key, string):
        '''Check if input is required'''
        if key in self.all and self.all[key] is not None:
            if not re.match(r"[^[a-zA-Z0-9]+$", self.all[key]):
                return True
            return key.capitalize() + " should be string"
        return True

    def minimum(self, key, minimum):
        '''Check required character size'''
        if key in self.all and self.all[key] is not None:
            if len(self.all[key]) < int(minimum):
                return "{} should not be less than {} characters".format(
                    key.capitalize(), str(minimum))
            return True
        return True

    def maximum(self, key, maximum):
        '''Check required character size'''
        if key in self.all and self.all[key] is not None:
            if len(self.all[key]) > int(maximum):
                return "{} should not be greater than {} characters".format(
                    key.capitalize(), str(maximum)
                )
            return True
        return True

    def email(self, key, email):
        '''Check required character size'''
        if key in self.all and self.all[key] is not None:
            if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z]+$", self.all[key]):
                return "Invalid email address"
            return True
        return True

    def same(self, key, same):
        '''Check if given '''
        if key in self.all and same in self.all:
            if self.all[same] != self.all[key]:
                return same.capitalize() + " don't match"
            return True
        return True

    def required(self, key, is_required=True):
        '''Check input it is required'''
        if key in self.all:
            if self.all[key] is None or self.all[key].strip() == '':
                return key.capitalize() + " should not be empty"
            return True
        return key.capitalize() + " is required"
