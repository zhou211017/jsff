# Generated by Django 2.2 on 2021-01-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='major',
        ),
        migrations.AlterField(
            model_name='user',
            name='classname',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='专业班级'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('student', '学生'), ('teacher', '教师')], default='学生', max_length=20, verbose_name='用户类型'),
        ),
    ]
