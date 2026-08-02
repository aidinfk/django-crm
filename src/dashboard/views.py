from django.shortcuts import redirect, render
from django.conf import settings

TEMPLATES_DIR = settings.TEMPLATES_DIR
print(TEMPLATES_DIR)


def dashboard_webpage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/auth/google/login/")
    return render(request, "dashboard/main.html", {})
    # dashboard_html = TEMPLATES_DIR / "dashboard.html"
    # if not dashboard_html.exists():
    #     return HttpResponse("Not found", status=404)
    # dashboard_html_val = dashboard_html.read_text()
    # _html = dashboard_html_val.format(my_value=str(request.user))
    # return HttpResponse(_html)


def about_us_page(request):
    return render(request, "about.html")
