# Generated by Django 5.2 on 2025-04-09 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم المشروع')),
                ('company', models.CharField(max_length=200, verbose_name='الشركة المنفذة')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/', verbose_name='شعار الشركة')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(verbose_name='تاريخ الانتهاء')),
                ('client', models.CharField(max_length=200, verbose_name='العميل')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'مشروع',
                'verbose_name_plural': 'المشاريع',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='رقم المرحلة')),
                ('name', models.CharField(max_length=200, verbose_name='اسم المرحلة')),
                ('supervisor', models.CharField(max_length=200, verbose_name='المشرف')),
                ('recipient', models.CharField(max_length=200, verbose_name='المستلم')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(verbose_name='تاريخ الاستلام')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='projects.project')),
            ],
            options={
                'verbose_name': 'مرحلة',
                'verbose_name_plural': 'المراحل',
                'ordering': ['number'],
                'unique_together': {('project', 'number')},
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم المهمة')),
                ('description', models.TextField(blank=True, verbose_name='وصف المهمة')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.stage')),
            ],
            options={
                'verbose_name': 'مهمة',
                'verbose_name_plural': 'المهام',
                'ordering': ['created_at'],
            },
        ),
    ]
