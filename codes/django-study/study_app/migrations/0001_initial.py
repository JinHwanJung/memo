# Generated by Django 3.2.4 on 2021-07-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean_field', models.BooleanField(default=False)),
                ('char_field', models.CharField(max_length=50, null=True)),
                ('integer_field', models.IntegerField(null=True)),
                ('date_field', models.DateField(null=True)),
                ('datetime_field', models.DateTimeField(null=True)),
            ],
        ),
    ]
