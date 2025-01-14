# Generated by Django 5.1.4 on 2025-01-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='description',
        ),
    ]