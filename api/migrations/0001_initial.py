# Generated by Django 5.0.1 on 2024-01-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_tk', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_tk', models.CharField(max_length=100, null=True)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_tk', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('view', models.PositiveIntegerField(default=0)),
                ('like', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
