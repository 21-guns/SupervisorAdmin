# Generated by Django 2.0.2 on 2018-02-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupervisorAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updated_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='名字')),
                ('api', models.CharField(max_length=128, null=True, verbose_name='API')),
                ('version', models.CharField(max_length=64, null=True, verbose_name='版本')),
            ],
            options={
                'db_table': 'supervisor_api',
            },
        ),
        migrations.CreateModel(
            name='SupervisorAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updated_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('username', models.CharField(max_length=128, null=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, null=True, verbose_name='密码')),
            ],
            options={
                'db_table': 'supervisor_auth',
            },
        ),
        migrations.CreateModel(
            name='SupervisorInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updated_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('instance_name', models.CharField(max_length=128, null=True, verbose_name='实例名')),
                ('host', models.CharField(max_length=128, null=True, verbose_name='主机')),
                ('port', models.CharField(max_length=128, null=True, verbose_name='端口')),
                ('api', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.SupervisorAPI', verbose_name='api')),
                ('auth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.SupervisorAuth', verbose_name='认证')),
            ],
            options={
                'db_table': 'supervisor_instance',
            },
        ),
    ]
