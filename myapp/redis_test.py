import redis

host = "localhost"
port = 6379

# 建立连接
r = redis.Redis(host=host,port=port)
#
# # 列表操作
# r.lpush("jiale",1)
# # 指定过期时间
r.expire("jiale",20)
# print(r.ttl("jiale"))
code = r.get('jiale')
print(code)
# 打印列表长度
# print(r.llen("jiale"))

# if r.llen("jiale") > 5:
#     print('您的账号已被锁定')


# 赋值
# r.set('test','test')

# # 取值
# code = r.get('test')
# print(code)
# # b'test'

# # 转码
# code = code.decode("utf-8")
# print(code)
# # test
