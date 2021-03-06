# Generated by Django 3.2.9 on 2022-01-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clash', '0005_alter_submission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('WA', 'Wrong Answer'), ('AC', 'Accepted'), ('TLE', 'Time Limit Exceeded'), ('CTE', 'Compile Time Error'), ('RE', 'Runtime Error'), ('MLE', 'Memory Limit Exceeded')], max_length=10, null=True),
        ),
    ]
