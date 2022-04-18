# Generated by Django 4.0.3 on 2022-04-08 20:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0003_alter_receita_data_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 4, 8, 17, 55, 1, 850172)),
        ),
    ]
