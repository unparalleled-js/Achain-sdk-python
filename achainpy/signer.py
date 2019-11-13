import sys
if sys.version > '3':
    from abc import ABC,abstractmethod
else:
    from abc import ABCMeta, abstractmethod

if sys.version > '3':
    class Signer(ABC):
        def __init__(self, private_str=''):
            super().__init__()
    
        @abstractmethod
        def to_public(self):
            pass

        @abstractmethod
        def to_wif(self):
            pass

        @abstractmethod
        def sign(self, digest):
            pass
    
        @abstractmethod
        def verify(self, encoded_sig, digest):
            pass
else:
    class Signer(ABCMeta):
        def __init__(self, private_str=''):
            super().__init__()
    
        @abstractmethod
        def to_public(self):
            pass

        @abstractmethod
        def to_wif(self):
            pass

        @abstractmethod
        def sign(self, digest):
            pass
    
        @abstractmethod
        def verify(self, encoded_sig, digest):
            pass
