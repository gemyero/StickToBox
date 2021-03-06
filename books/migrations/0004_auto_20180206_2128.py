# Generated by Django 2.0.1 on 2018-02-06 21:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180205_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('wishlist', 'Add To Wishlist'), ('read', 'Read'), ('reading', 'Currently Reading')], max_length=10)),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('comment', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='userbook',
            name='user',
        ),
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserBook',
        ),
        migrations.AddField(
            model_name='profilebook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AddField(
            model_name='profilebook',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Profile'),
        ),
        migrations.AddField(
            model_name='book',
            name='profile',
            field=models.ManyToManyField(through='books.ProfileBook', to='books.Profile'),
        ),
    ]
