
class InvalidKeyFile(Exception):
    ''' Raised when the key file format is invalid '''
    pass

class InvalidPermissionFormat(Exception):
    ''' Raised when the permission format is invalid'''
    pass

class ActKeyError(Exception):
    ''' Raised when there is an ActKey error '''
    pass

class ErrMsigInvalidProposal(Exception):
    ''' Raised when an invalid proposal is queried'''
    pass

class ErrBufferInvalidType(Exception):
    ''' Raised when trying to encode/decode an invalid type '''
    pass

class ErrInvalidSchema(Exception):
    ''' Raised when trying to process a schema '''
    pass

class ErrUnknownObj(Exception):
    ''' Raised when an object is not found in the ABI '''
    pass

class ErrAbiProcessingError(Exception):
    ''' Raised when the abi action cannot be processed '''
    pass

class ErrSetSameCode(Exception):
    ''' Raised when the code would not change on a set'''
    pass

class ErrSetSameAbi(Exception):
    ''' Raised when the abi would not change on a set'''
    pass
