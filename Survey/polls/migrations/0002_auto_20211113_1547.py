# Generated by Django 2.2.10 on 2021-11-13 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='typeQA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.TypeQA'),
        ),
    ]
