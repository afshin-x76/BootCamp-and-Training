# Generated by Django 3.1.7 on 2021-04-09 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210409_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='answers',
        ),
        migrations.AddField(
            model_name='testanswers',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.test'),
        ),
    ]
