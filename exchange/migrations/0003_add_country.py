from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0002_load_exchange_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(max_length=100, default="", verbose_name="країна"),
            preserve_default=False,
        ),
    ]
