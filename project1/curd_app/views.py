from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company


@login_required(login_url="login_url")
def company_view(request):
    template_name = "curd_app/conpany_info.html"
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_company(request):
    template_name = "curd_app/show_company.html"
    orders = Company.objects.all()
    context = {"orders": orders}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Company.objects.get(id=pk)
    form = CompanyForm(instance=obj)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = 'curd_app/company_info.html'
    context = {'form': form}
    return render(request, template_name, context)


def cancel_view(request,  pk):
    obj = Company.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, 'curd_app/confirm.html')
