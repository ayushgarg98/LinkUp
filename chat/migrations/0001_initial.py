# Generated by Django 2.2.6 on 2019-11-14 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='person1', to='Person.PersonDetails')),
                ('person2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='person2', to='Person.PersonDetails')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.ChatInstance')),
            ],
        ),
    ]
