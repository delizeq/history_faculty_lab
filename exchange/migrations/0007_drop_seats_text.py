from django.db import migrations, models


class Migration(migrations.Migration):
    """Крок 3/3: seats стає обовʼязковим, старе текстове поле видаляється."""

    dependencies = [
        ("exchange", "0006_fill_seats_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveSmallIntegerField(verbose_name="кількість місць"),
        ),
        
        
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats_text",
            field=models.CharField(max_length=50, default="", verbose_name="кількість місць"),
        ),
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="seats_text",
        ),
    ]
