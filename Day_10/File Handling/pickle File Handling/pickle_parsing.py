## dumps(): Encryption
## loads(): Decryption

'''
1. JSON
2. pickle ---> for pickle mode should be 'ab+'
'''

import pickle
file=open('pickle.txt', 'ab+')
data={
    'fullname':'Paridhi Mehta',
    'userid':'987654321',
    'password':'*****'
}
# print(f'Original Data: {data}')
# print(f'Type of original data: {type(data)}')
# # Original Data: {'fullname': 'Paridhi Mehta', 'userid': '987654321', 'password': '*****'}
# # Type of original data: <class 'dict'>

# enc_data=pickle.dumps(data)
# print(f'Encrypted Data: {enc_data}')
# print(f'Type of encrypted data: {type(enc_data)}')
# # Encrypted Data: b'\x80\x05\x95H\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08fullname\x94\x8c\rParidhi Mehta\x94\x8c\x06userid\x94\x8c\t987654321\x94\x8c\x08password\x94\x8c\x05*****\x94u.'
# # Type of encrypted data: <class 'bytes'>

# dec_data=pickle.loads(enc_data)
# print(f'Decrypted Data: {dec_data}')
# print(f'Type of decrypted data: {type(dec_data)}')
# # Decrypted Data: {'fullname': 'Paridhi Mehta', 'userid': '987654321', 'password': '*****'}
# # Type of decrypted data: <class 'dict'>

enc_data=pickle.dumps(data)
file.write(enc_data)

file.seek(0)
enc_data=file.read()
print(type(enc_data)) ##<class 'bytes'>


ori_data=pickle.loads(enc_data)
print(ori_data, type(ori_data)) ##{'fullname': 'Paridhi Mehta', 'userid': '987654321', 'password': '*****'} <class 'dict'>

file.close()

'''
For pickle, replace json with pickle
and it will convert data into binary just like json convert to str
'''
