# Generated by Django 3.1.7 on 2021-03-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20210308_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='create_ts',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='modified_ts',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='employee',
            table='apis_employee',
        ),
    ]