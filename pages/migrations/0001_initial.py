# Generated by Django 2.2.3 on 2019-08-01 21:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import feincms3.cleanse
import imagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, help_text='Used for Open Graph and other meta tags.', max_length=200, verbose_name='title')),
                ('meta_description', models.TextField(blank=True, help_text='Override the description for this page.', verbose_name='description')),
                ('meta_image', imagefield.fields.ImageField(blank=True, height_field='meta_image_height', help_text='Set the Open Graph image.', upload_to='meta/%Y/%m', verbose_name='image', width_field='meta_image_width')),
                ('meta_canonical', models.URLField(blank=True, help_text='If you need this you probably know.', verbose_name='canonical URL')),
                ('meta_author', models.CharField(blank=True, help_text='Override the author meta tag.', max_length=200, verbose_name='author')),
                ('meta_robots', models.CharField(blank=True, help_text='Override the robots meta tag.', max_length=200, verbose_name='robots')),
                ('meta_image_width', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('meta_image_height', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('meta_image_ppoi', imagefield.fields.PPOIField(default='0.5x0.5', max_length=20)),
                ('redirect_to_url', models.CharField(blank=True, max_length=200, verbose_name='Redirect to URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('position', models.PositiveIntegerField(db_index=True, editable=False, validators=[django.core.validators.MinValueValidator(limit_value=1, message='Position is expected to be greater than zero.')])),
                ('path', models.CharField(blank=True, help_text="Generated automatically if 'static path' is unset.", max_length=1000, unique=True, validators=[django.core.validators.RegexValidator(message='Path must start and end with a slash (/).', regex='^/(|.+/)$')], verbose_name='path')),
                ('static_path', models.BooleanField(default=False, verbose_name='static path')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pages.Page', verbose_name='parent')),
                ('redirect_to_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.Page', verbose_name='Redirect to page')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='RichText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', feincms3.cleanse.CleansedRichTextField(verbose_name='text')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_richtext_set', to='pages.Page')),
            ],
            options={
                'verbose_name': 'rich text',
                'verbose_name_plural': 'rich texts',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagefield.fields.ImageField(height_field='height', upload_to='images/%Y/%m', verbose_name='image', width_field='width')),
                ('width', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='image width')),
                ('height', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='image height')),
                ('ppoi', imagefield.fields.PPOIField(default='0.5x0.5', max_length=20, verbose_name='primary point of interest')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('caption', models.CharField(blank=True, max_length=200, verbose_name='caption')),
                ('css_class', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default='left', max_length=5, verbose_name='CSS class')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_image_set', to='pages.Page')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'abstract': False,
            },
        ),
    ]