# Generated by Django 2.2.7 on 2019-11-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191117_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartasemjogo',
            name='ID_carta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartasemjogo',
            name='ID_partida',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartasemjogo',
            name='Posicao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogada',
            name='ID_jogada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogada',
            name='ID_jogador',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogada',
            name='ID_partida',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogada',
            name='Posicao_Carta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogada',
            name='Turno_da_jogada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lobby',
            name='ID_partida',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lobby',
            name='Status_partida',
            field=models.IntegerField(default=0),
        ),
    ]
