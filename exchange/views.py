from django.shortcuts import render

from .models import ExchangeProgram


def exchange_list(request):
    countries = list(
        ExchangeProgram.objects.order_by("country")
        .values_list("country", flat=True)
        .distinct()
    )
    selected = request.GET.get("country", "")
    programs = ExchangeProgram.objects.all()
    if selected:
        programs = programs.filter(country=selected)
    return render(
        request,
        "exchange/exchange_list.html",
        {"programs": programs, "countries": countries, "selected": selected},
    )
