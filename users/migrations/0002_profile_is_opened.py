# Generated by Django 3.2.3 on 2021-07-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_opened',
            field=models.CharField(choices=[('OPEN', '공개'), ('NOT_OPEN', '비공개')], default='OPEN', max_length=10, null=True),
        ),
    ]