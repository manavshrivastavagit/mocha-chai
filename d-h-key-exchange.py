import json
import http.client
from random import randrange

# email
email = "manavshrivastava@hotmail.com"

print("\n------Calling get-keys API------\n")
# Calling get-keys API
conn = http.client.HTTPSConnection("shortrndexercise.singular.net")
conn.request("GET", "/get-key?email=" + email)
response = conn.getresponse()
print(response.status, response.reason)  # 200 OK
json_data = response.read().decode()
data = json.loads(json_data)
conn.close()

# Variables
PrimeNumber = data["p"]  # p
GeneratorOfP = data["g"]  # g
A_public = data["A_public"]  # A_public

# Publicly Shared Variables
print("    Publicly Shared PrimeNumber: ", PrimeNumber)
print("    Publicly Shared GeneratorOfP:  ", GeneratorOfP)
print("    Publicly Shared A_public key: ", A_public)

bobSecret = randrange(
    10)  # Randomly generates private key integer from 0 to 9 inclusive

# Bob Sends Alice, B_public = g^bobSecret mod p
B_public = (GeneratorOfP**bobSecret) % PrimeNumber
print(" B_public key: ", B_public)

print("\n------Calculating Shared Secret:------\n")
# Bob Computes Shared Secret: s = A_public^bobSecret mod p
bobSharedSecret = (A_public**bobSecret) % PrimeNumber
print("    Bob Shared Secret: ", bobSharedSecret)

print("\n------Calling submit API------\n")
# Calling submit API
conn = http.client.HTTPSConnection("shortrndexercise.singular.net")
conn.request(
    "GET", "/submit?email=" + str(email) + "&B_public=" + str(B_public) +
    "&solution=" + str(bobSharedSecret))
response = conn.getresponse()
print(response.status, response.reason)  # 200 OK
json_data = response.read().decode()
data = json.loads(json_data)
print(data)  #  {'success': True}
conn.close()

