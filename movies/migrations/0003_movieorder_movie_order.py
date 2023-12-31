# Generated by Django 4.2.2 on 2023-06-16 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_alter_movie_duration_alter_movie_synopsis'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyed_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_movie', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order_movie', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='order',
            field=models.ManyToManyField(related_name='movie_order', through='movies.MovieOrder', to=settings.AUTH_USER_MODEL),
        ),
    ]
