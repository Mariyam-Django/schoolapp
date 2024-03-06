# Generated by Django 4.2.7 on 2023-11-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('picture', models.ImageField(null=True, upload_to='schoolimg')),
            ],
        ),
    ]