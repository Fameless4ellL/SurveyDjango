# Generated by Django 2.2.10 on 2021-11-13 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_auto_20211113_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='QA',
            field=models.ManyToManyField(blank=True, help_text='Вопросы', to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='typeqa',
            name='tpe',
            field=models.CharField(max_length=256, verbose_name='тип вопроса'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
