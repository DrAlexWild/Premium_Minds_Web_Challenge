# Generated by Django 4.1 on 2022-08-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('Project Manager', 'Project Manager'), ('Developer', 'Developer'), ('Architect', 'Architect')], default='Developer', max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('palavra_passe', models.CharField(max_length=200)),
            ],
        ),
    ]
