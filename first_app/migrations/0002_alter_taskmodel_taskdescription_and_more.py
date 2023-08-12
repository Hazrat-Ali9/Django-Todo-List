from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='taskDescription',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='taskTitle',
            field=models.CharField(max_length=30),
        ),
    ]
