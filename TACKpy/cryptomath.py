# Author: Trevor Perrin
# See the LICENSE file for legal information regarding use of this file.

from .compat import *

################ CRYPTOMATH ###

import math, hashlib, hmac

def bytesToNumber(bytes):
    "Convert a sequence of bytes (eg bytearray) into integer."
    total = 0
    multiplier = 1
    for count in range(len(bytes)-1, -1, -1):
        byte = bytes[count]
        total += multiplier * byte
        multiplier *= 256
    return total

def numberToBytes(n, howManyBytes=None):
    """Convert an integer into a bytearray, zero-pad to howManyBytes.
    
    The returned bytearray may be smaller than howManyBytes, but will
    not be larger.  The returned bytearray will contain a big-endian
    encoding of the input integer (n).
    """    
    if not howManyBytes:
        howManyBytes = numBytes(n)
    bytes = bytearray(howManyBytes)
    for count in range(howManyBytes-1, -1, -1):
        bytes[count] = int(n % 256)
        n >>= 8
    return bytes
    
def stringToNumber(s):
    "Convert a string - interpreted as a sequence of bytes - into integer."    
    return bytesToNumber(bytearray(s))
    
def numBits(n):
    "Return the number of bits needed to represent the integer n."
    if n==0:
        return 0
    s = "%x" % n
    return ((len(s)-1)*4) + \
    {'0':0, '1':1, '2':2, '3':2,
     '4':3, '5':3, '6':3, '7':3,
     '8':4, '9':4, 'a':4, 'b':4,
     'c':4, 'd':4, 'e':4, 'f':4,
     }[s[0]]
    
def numBytes(n):
    "Return the number of bytes needed to represent the integer n."
    if n==0:
        return 0
    bits = numBits(n)
    return int(math.ceil(bits / 8.0))

def SHA256(b):
    "Return a 32-byte bytearray which is the SHA256 of input bytearray."
    return bytearray(hashlib.sha256(compat26Str(b)).digest())

def HMAC_SHA256(k, b):
    """Return a 32-byte bytearray which is HMAC-SHA256 of key and input."""    
    return bytearray(hmac.new(bytes(k), bytes(b), hashlib.sha256).digest())

def constTimeCompare(a, b):
    """Compare two sequences of integer (eg bytearrays) without a timing leak.
    
    This function is secure when comparing against secret values, such as 
    passwords, MACs, etc., where a more naive, early-exit comparison loop
    would leak information that could be used to extract the secret.
    """
    if len(a) != len(b):
        return False
    result = 0
    for x in range(len(a)):
        result |= a[x]^b[x]
    if result:
        return False
    return True

    import zlib

def testOsUrandom():
    import zlib, os
    print("Testing OS_URANDOM")
    length = len(zlib.compress(os.urandom(1000)))
    assert(length > 900)
    return 1
