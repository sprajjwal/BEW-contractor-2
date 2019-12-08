# Generated by Django 2.2.6 on 2019-12-03 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of your page.', max_length=600, unique=True)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=600)),
                ('content', models.TextField(help_text='Write the content of your page here.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this page was created. Automatically generated when the model saves.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.')),
                ('author', models.ForeignKey(help_text='The user that posted this article.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
