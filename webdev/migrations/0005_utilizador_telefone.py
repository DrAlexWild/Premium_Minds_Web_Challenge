# Generated by Django 4.1 on 2022-08-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0004_remove_utilizador_tipo_utilizador_architect_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='telefone',
            field=models.CharField(default='+351 000000000', max_length=15),
        ),
    ]
