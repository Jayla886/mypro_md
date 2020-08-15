import jwt,datetime

# 载荷中加入生命周期的概念
playload = {
    # 过期时间
    'exp':int((datetime.datetime.now()+datetime.timedelta(seconds=60)).timestamp()),
    'data':{'uid':9}
}
# 生成jwt
# encode_jwt = jwt.encode(playload,'qwe123',algorithm='HS256')
# print(encode_jwt)
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI5In0.qKB-V_YqVtAlhPZuQSQ9Lf-iIj60ESiDJmH9emKhdFE'
# 以二进制显示结果，第一部分：头部信息、第二部分：载荷、第三部分：密钥
# 转码
# encode_str = str(encode_jwt,'utf-8')
# print(encode_str)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI5In0.qKB-V_YqVtAlhPZuQSQ9Lf-iIj60ESiDJmH9emKhdFE
# 解密操作
try:
    decode_jwt = jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODg4NTM5NTQsImRhdGEiOnsidWlkIjo5fX0.pdjz6Fatx60AnMtOhc9f3Q4dkT9E2fYx8QqaOPLF8oQ','qwe123',algorithms=['HS256'])
    print(decode_jwt)   # {'uid': '9'}
except Exception as e:
    print('密钥已过期')
# print(decode_jwt['uid'])  # 9

# # 载荷中加入生命周期的概念
# playload = {
#     # 过期时间
#     'exp':int((datetime.datetime.now()+datetime.timedelta(seconds=120)).timestamp()),
#     'data':{'uid':2}
# }
# # 生成jwt
# encode_jwt = jwt.encode(playload,'qwe123',algorithm='HS256')
#
# # 转码
# encode_str = str(encode_jwt,'utf-8')
#
# # 解密操作
# decode_jwt = jwt.decode('','qwe123',algorithms=['HS256'])
# print(encode_str)
# print(decode_jwt)




















































































