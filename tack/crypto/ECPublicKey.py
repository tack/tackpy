from .python.Python_ECPublicKey import Python_ECPublicKey
from .openssl.OpenSSL import openssl as o
from .openssl.OpenSSL_ECPublicKey import OpenSSL_ECPublicKey

class ECPublicKey:

    @staticmethod
    def new(rawPublicKey):
        if o.enabled:
            return OpenSSL_ECPublicKey(rawPublicKey)
        else:
            return Python_ECPublicKey(rawPublicKey)