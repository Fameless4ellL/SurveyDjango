# Generated by Django 2.2.10 on 2021-11-13 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeQA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpe', models.CharField(default=None, max_length=256, verbose_name='тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionQA', models.CharField(blank=True, max_length=255, verbose_name='текст вопроса')),
                ('start_date', models.DateTimeField(blank=True, default=None)),
                ('end_date', models.DateTimeField(blank=True, default=None)),
                ('typeQA', models.OneToOneField(blank=True, default=None, help_text='Тип вопроса', on_delete=django.db.models.deletion.CASCADE, to='polls.TypeQA')),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_p', models.CharField(blank=True, max_length=56, verbose_name='Тема')),
                ('desc_p', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('s_date', models.DateTimeField(blank=True, default=None)),
                ('e_date', models.DateTimeField(blank=True, default=None)),
                ('QA', models.ManyToManyField(blank=True, default=None, help_text='Вопросы', to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]