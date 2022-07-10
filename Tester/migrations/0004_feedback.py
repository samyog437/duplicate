# Generated by Django 4.0.5 on 2022-06-23 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_uxclient_isemailverified'),
        ('Tester', '0003_uploadvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('feedback', models.CharField(blank=True, max_length=255)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.uxclient')),
                ('tester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tester.uxtester')),
            ],
        ),
    ]
