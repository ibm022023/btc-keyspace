import random
import ecdsa
import hashlib
from ecdsa.util import string_to_number, number_to_string

from bitcoin import *

# secp256k1, http://www.oid-info.com/get/1.3.132.0.10
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)
oid_secp256k1 = (1, 3, 132, 0, 10)
SECP256k1 = ecdsa.curves.Curve("SECP256k1", curve_secp256k1, generator_secp256k1, oid_secp256k1)
ec_order = _r

curve = curve_secp256k1
generator = generator_secp256k1


def get_key(privkey,search_for):
  count = 0 
  address = ''
  print("Addresses tried ... (just showing first six characters of address)")
  while not search_for.lower() in address.lower():
    privkey += 1
    pubkey_point =fast_multiply(G, privkey)
    address = pubkey_to_address(pubkey_point)
    print(address[:6], end=' ')
    count += 1
    if (count>99): 
	    return 0,0
  return address,privkey

seq="aa"
	
privkey = random.randrange(2**256)

address,privkey=get_key(privkey,seq)
if (address==0):
	print("Could not find sequence. Need a cluster!")
else:
	print("\n\nPublic Bitcoin address is",address)
	print("Private Bitcoin address is:",privkey)
