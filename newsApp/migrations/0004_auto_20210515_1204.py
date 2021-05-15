# Generated by Django 3.2.3 on 2021-05-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('newsApp', '0003_auto_20210515_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsappmodel',
            name='contactNumber',
            field=models.CharField(default='+91', max_length=12),
        ),
        migrations.AlterField(
            model_name='newsappmodel',
            name='fb',
            field=models.CharField(default='http://fb.com/', max_length=50),
        ),
        migrations.AlterField(
            model_name='newsappmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='newsappmodel',
            name='twitter',
            field=models.CharField(default='http://twitter.com/', max_length=50),
        ),
        migrations.AlterField(
            model_name='newsappmodel',
            name='youtube',
            field=models.CharField(default='http://youtube.com/', max_length=50),
        ),
    ]
