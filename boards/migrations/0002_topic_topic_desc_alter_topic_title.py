# Generated by Django 4.0.3 on 2022-05-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_desc',
            field=models.CharField(default='auto', max_length=300),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
