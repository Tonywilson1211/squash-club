# Generated by Django 3.2.19 on 2023-06-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squash', '0002_remove_comment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
    ]
