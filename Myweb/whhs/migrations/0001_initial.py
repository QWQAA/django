# Generated by Django 4.0.4 on 2023-04-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('stu_id', models.UUIDField(primary_key=True, serialize=False)),
                ('stu_user', models.CharField(max_length=20)),
                ('stu_pwd', models.CharField(max_length=20)),
            ],
        ),
    ]
