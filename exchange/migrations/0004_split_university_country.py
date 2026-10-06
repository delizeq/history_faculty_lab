import re

from django.db import migrations





PATTERNS = [
    re.compile(r"^(?P<name>.+?)\s*\((?P<country>[^()]+)\)\s*$"),
    re.compile(r"^(?P<name>.+?)\s+[-\u2013\u2014]\s+(?P<country>[^-\u2013\u2014]+?)\s*$"),
    re.compile(r"^(?P<name>.+),\s*(?P<country>[^,]+?)\s*$"),
]


def split_value(value):
    value = value.strip()
    for pattern in PATTERNS:
        match = pattern.match(value)
        if match:
            return match.group("name").strip(), match.group("country").strip()
    raise ValueError(f"Не вдалося розділити університет і країну: {value!r}")


def split_forward(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        name, country = split_value(program.university)
        program.university = name
        program.country = country
        program.save(update_fields=["university", "country"])


def split_backward(apps, schema_editor):
    
    
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        if program.country:
            program.university = f"{program.university}, {program.country}"
            program.save(update_fields=["university"])


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0003_add_country"),
    ]

    operations = [
        migrations.RunPython(split_forward, split_backward),
    ]
