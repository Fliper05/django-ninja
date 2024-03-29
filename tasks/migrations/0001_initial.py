# Generated by Django 3.2 on 2024-01-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('CREATED', 'Vytvořen'), ('IN_PROGRESS', 'Probíhá'), ('COMPLETED', 'Dokončen')], default='CREATED', max_length=20)),
            ],
        ),
    ]
