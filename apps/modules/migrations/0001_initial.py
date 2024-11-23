# Generated by Django 5.1.3 on 2024-11-23 13:06

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
            name='Salawat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('salawat_title', models.CharField(max_length=255)),
                ('salawat_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Salawat',
                'verbose_name_plural': 'Salawat',
            },
        ),
        migrations.CreateModel(
            name='SalawatAudio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('salawat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.salawat')),
            ],
            options={
                'verbose_name': 'Salawat Audio',
                'verbose_name_plural': 'Salawat Audios',
            },
        ),
        migrations.CreateModel(
            name='SalawatTranslation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
                ('salawat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.salawat')),
            ],
            options={
                'verbose_name': 'Salawat Translation',
                'verbose_name_plural': 'Salawat Translations',
            },
        ),
    ]
