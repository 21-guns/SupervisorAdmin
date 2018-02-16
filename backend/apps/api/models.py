from django.db import models


class Base(models.Model):
    class Meta:
        abstract = True

    created_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


class SupervisorAuth(Base):
    class Meta:
        db_table = 'supervisor_auth'

    username = models.CharField(null=True, max_length=128, verbose_name="用户名")
    password = models.CharField(null=True, max_length=128, verbose_name="密码")


class SupervisorAPI(Base):
    class Meta:
        db_table = 'supervisor_api'

    name = models.CharField(null=True, max_length=128, verbose_name="名字")
    api = models.CharField(null=True, max_length=128, verbose_name="API")
    version = models.CharField(null=True, max_length=64, verbose_name="版本")


class SupervisorInstance(Base):
    class Meta:
        db_table = 'supervisor_instance'

    instance_name = models.CharField(null=True, max_length=128, verbose_name="实例名")
    host = models.CharField(null=True, max_length=128, verbose_name="主机")
    port = models.CharField(null=True, max_length=128, verbose_name="端口")
    api = models.ForeignKey(SupervisorAPI, null=True, verbose_name="api", on_delete=models.SET_NULL)
    auth = models.ForeignKey(SupervisorAuth, null=True, verbose_name="认证", on_delete=models.SET_NULL)
