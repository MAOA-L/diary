from django.shortcuts import render
from diary.globalContext import Primary


def index(request):
    context = {
        "parent_id": Primary.global_context["xadmin"]["statistic"]["parent_id"] - 1,
        "current_id": Primary.global_context["xadmin"]["publish"]["current_id"] - 1,
    }
    return render(request, "statistic.html", context)


def publish(request):
    context = {
        "parent_id": Primary.global_context["xadmin"]["publish"]["parent_id"] - 1,
        "current_id": Primary.global_context["xadmin"]["publish"]["current_id"],
    }
    return render(request, "publish.html", context)
