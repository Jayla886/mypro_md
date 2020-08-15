# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class User(models.Model):
#     create_time = models.DateTimeField(blank=True, null=True)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     img = models.CharField(max_length=200)
#     type = models.IntegerField(blank=True, null=True)
#     phone = models.IntegerField(default=0)
#     num = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user'

from django.db import models
#导入时间域
from django.utils import timezone
# 基类
class Base(models.Model):
    #创建时间
    create_time = models.DateTimeField(default=timezone.now,null=True)
    class Meta:
        abstract = True

#商品类别表
class Comment(Base):
	uid = models.IntegerField()
	content = models.CharField(max_length=400)
	gid = models.IntegerField()
	#声明表名
	class Meta:
		db_table = "comment"

# 轮播图
class Carousel(Base):
    name = models.CharField(max_length=200)
    src = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    class Meta:
        db_table = 'carousel'

# 商品表
class Goods(Base):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200,null=True)
    img = models.CharField(max_length=200,null=True)
    # 演示视频
    video = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    params = models.CharField(max_length=400)
    flows = models.IntegerField(default=0,null=True)
    cid = models.IntegerField(null=True)
    # 表名
    class Meta:
        db_table = 'goods'
# 外键会影响性能


#用户表
class User(Base):
    #用户名
    username=models.CharField(max_length=200)
    #密码
    password=models.CharField(max_length=200)
    #头像
    img=models.CharField(max_length=200,null=True)
    #用户类别 (0普通用户，1超级管理员，2网站编辑,3新浪微博)
    type = models.IntegerField(default=0)
    #手机号
    phone = models.CharField(max_length=200,null=True)
    #个人主页
    num = models.IntegerField(default=0,null=True)

    class Meta:
        db_table='user'

# 商品分类
class Category(models.Model):
    name = models.CharField(max_length=200)
    careate_time = models.DateTimeField(default=timezone.now,null=True)
    class Meta:
        db_table = 'category'




class Image(models.Model):
    imgname = models.CharField(max_length=400,null =True)
    class Meta:
        db_table = 'image'
