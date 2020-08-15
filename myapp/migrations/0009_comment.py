# Generated by Django 3.0.6 on 2020-05-17 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('uid', models.IntegerField()),
                ('content', models.CharField(max_length=400)),
                ('gid', models.IntegerField()),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]