# Generated by Django 4.0.3 on 2022-05-28 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_topic_desc_alter_topic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_pk',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_pk',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_pk',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]