import re

from django.db import migrations


def text_to_number(apps, schema_editor):
    """Крок 2/3: бере перше число з тексту. "до 4" -> 4, "2 місця" -> 2, "1 місце" -> 1."""
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        match = re.search(r"\d+", program.seats_text)
        if not match:
            raise ValueError(f"У значенні {program.seats_text!r} немає числа")
        program.seats = int(match.group())
        program.save(update_fields=["seats"])


def number_to_text(apps, schema_editor):
    
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        if program.seats is not None:
            program.seats_text = str(program.seats)
            program.save(update_fields=["seats_text"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0005_add_seats_number"),
    ]

    operations = [
        migrations.RunPython(text_to_number, number_to_text),
    ]
