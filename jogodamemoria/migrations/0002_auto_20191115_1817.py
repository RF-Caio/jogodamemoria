# Generated by Django 2.2.6 on 2019-11-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogodamemoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlecarta',
            name='anexo_frente',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='controlecarta',
            name='anexo_verso',
            field=models.ImageField(upload_to=''),
        ),
    ]
