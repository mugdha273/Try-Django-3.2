# Generated by Django 3.2.5 on 2021-07-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publish',
        ),
    ]