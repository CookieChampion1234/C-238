import hashlib


text = "Hello World"



result = hashlib.sha3_256(text.encode())


print("The SHA256 is : ",result.hexdigest())