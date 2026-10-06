from django.db import migrations, models


class Migration(migrations.Migration):
    """Крок 1/3: старе текстове поле лишається як seats_text, поруч зʼявляється числове seats."""

    dependencies = [
        ("exchange", "0004_split_university_country"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exchangeprogram",
            old_name="seats",
            new_name="seats_text",
        ),
        migrations.AddField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveSmallIntegerField(null=True, verbose_name="кількість місць"),
        ),
    ]
