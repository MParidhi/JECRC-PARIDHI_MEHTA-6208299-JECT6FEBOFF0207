## dumps(): Encryption
## loads(): Decryption

'''
1. JSON
2. pickle
'''

import json
file=open('json.txt', 'a+')
data={
    'fullname':'Paridhi Mehta',
    'userid':'987654321',
    'password':'*****'
}
# print(f'Original Data: {data}')
# print(f'Type of original data: {type(data)}')
# ## Original Data: {'fullname': 'Paridhi Mehta', 'userid': '987654321', 'password': '*****'}
# ## Type of original data: <class 'dict'>

# enc_data=json.dumps(data)
# print(f'Encrypted Data: {enc_data}')
# print(f'Type of encrypted data: {type(enc_data)}')
# ## Encrypted Data: {"fullname": "Paridhi Mehta", "userid": "987654321", "password": "*****"}
# ## Type of encrypted data: <class 'str'>

# dec_data=json.loads(enc_data)
# print(f'Decrypted Data: {dec_data}')
# print(f'Type of decrypted data: {type(dec_data)}')
# ## Decrypted Data: {'fullname': 'Paridhi Mehta', 'userid': '987654321', 'password': '*****'}
# ## Type of decrypted data: <class 'dict'>

enc_data=json.dumps(data)
file.write(enc_data)

file.seek(0)
enc_data=file.read()
print(type(enc_data)) ##<class 'str'>


ori_data=json.loads(enc_data)
print(ori_data, type(ori_data)) ##{'fullname': 'Paridhi Mehta', 'userid': '987654321', 'password': '*****'} <class 'dict'>

file.close()

'''
For pickle, replace json with pickle
and it will convert data into binary just like json convert to str
'''

