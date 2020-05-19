# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function
import json


# get keys 
import http.client
from random import randrange

# email
email = "%3Cyour_email_address%3E"

# get keys
# import requests
# url_endpoint = 'https://shortrndexercise.singular.net'
# mydict = {'email': '<your_email_address>f'}
# resp = requests.get(url_endpoint, params=mydict)
# print(resp.url)
# print(resp.text)
# data = resp.json()
# print(data)

conn = http.client.HTTPSConnection("")
conn.request("GET", "/get-key?email=%3Cyour_email_address%3E")
response = conn.getresponse()
print(response.status, response.reason)
json_data = response.read().decode()
data = json.loads(json_data)
print(data)
conn.close()

 
# # Variables Used
# sharedPrime = data["p"]    # p
# sharedBase = data["g"]     # g 
# A = data["A_public"]       # A_public key
 
# # # Begin
# print( "Publicly Shared Variables:")
# print( "    Publicly Shared Prime: " , sharedPrime )
# print( "    Publicly Shared Base:  " , sharedBase )
# print( "    A_public key: " , A )
 

# bobSecret = randrange(10)     # Random Integer from 0 to 9 inclusive
 
# # # Bob Sends Alice B = g^b mod p
# # B = (sharedBase ** bobSecret) % sharedPrime
# # print(" Bob Sends Over Public Chanel: ", B )

# # submit
# conn = http.client.HTTPSConnection("shortrndexercise.singular.net")
# conn.request("GET", "/submit?email=%3Cyour_email_address%3E&B_public=%3CB_public%3E&solution=%3Cshared_secret%3E")
# response = conn.getresponse()
# print(response.status, response.reason)
# json_data = response.read().decode()
# data = json.loads(json_data)
# print(data)
# conn.close()
 
# print( "\n------------\n" )
# print( "Privately Calculated Shared Secret:" )
# # Alice Computes Shared Secret: s = B^a mod p
# aliceSharedSecret = (B ** aliceSecret) % sharedPrime
# print( "    Alice Shared Secret: ", aliceSharedSecret )
 
# # Bob Computes Shared Secret: s = A^b mod p
# bobSharedSecret = (A**bobSecret) % sharedPrime
# print( "    Bob Shared Secret: ", bobSharedSecret )