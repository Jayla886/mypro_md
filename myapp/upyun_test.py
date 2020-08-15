import upyun

# 新建又拍云实例
up = upyun.UpYun('jiale-meiduo', 'fanjiale',
                 'SjFkpfCt94p7rIp1DlIdznP1v2NWmcFp')

# 上传文件,路径是云端路径
# 适用于小文件的上传
# up.put('/upyun_test.txt','sdds你好\n你好')

# 文件流操作 （可以节省内存）
# django路径
# 用于大文件的分片上传
# with open('./md.png','rb')as f:
#     # 上传操作
#     ret = up.put('/upyun_test.png',f,checksum=True)

# 目录操作
# up.mkdir('/upyun_test/')

# 移动文件
# up.move('/upyun_test.png','/upyun_test/upyun_test.png')

# 复制文件
# up.copy('/upyun_test.txt','/upyun_test/upyun_test1.txt')

# 断点续传
# with open('./test.mp4','rb')as f:
#     res = up.put('/upyun_test/test.mp4',f,checksum=True,need_resume=True)

# 下载文件
# res = up.get('/upyun_test/upyun_test.png')
# print(res)

# 删除文件
# up.delete('/upyun_test/upyun_test.png')





















































