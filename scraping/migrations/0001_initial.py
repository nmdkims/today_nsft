<<<<<<< HEAD
# Generated by Django 3.2.5 on 2022-02-25 11:37
=======
# Generated by Django 4.0.2 on 2022-02-25 11:39
>>>>>>> cd6280aa3a9c84347d6d00cee7da9f97558a499b

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=30, null=True)),
                ('weather', models.CharField(blank=True, max_length=30, null=True)),
<<<<<<< HEAD
                ('h_temp', models.CharField(blank=True, max_length=30, null=True)),
                ('l_temp', models.CharField(blank=True, max_length=30, null=True)),
=======
                ('h_temp', models.FloatField()),
                ('l_temp', models.IntegerField()),
>>>>>>> cd6280aa3a9c84347d6d00cee7da9f97558a499b
            ],
            options={
                'db_table': 'climate',
            },
        ),
    ]
