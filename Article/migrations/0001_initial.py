# Generated by Django 3.0.5 on 2020-04-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=200)),
                ('Title', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=100)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]
