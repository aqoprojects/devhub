# Generated by Django 5.1.3 on 2025-06-25 22:10

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=70)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_overview_image/')),
                ('description', models.TextField(blank=True, null=True, verbose_name='about project')),
                ('source_code_link', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('posted_date', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stacks', models.ManyToManyField(to='devsocial.technology')),
            ],
            options={
                'unique_together': {('title', 'user')},
            },
        ),
        migrations.CreateModel(
            name='ProjectRating',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('rating', models.CharField(default=0, max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='devsocial.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('review', models.CharField(choices=[('1', '1 STARS'), ('2', '2 STARS'), ('3', '3 STARS'), ('4', '4 STARS'), ('5', '5 STARS')], max_length=10)),
                ('comment', models.TextField(blank=True, max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devsocial.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'project')},
            },
        ),
    ]
