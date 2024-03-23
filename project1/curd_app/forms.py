from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

        widgets = {
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "company_owner": forms.TextInput(attrs={"class": "form-control"}),
            "total_emp": forms.NumberInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control", "rows": 5}),
            "city_pincode": forms.NumberInput(attrs={"class": "form-control"}),
            "payment_mode": forms.Select(attrs={"class": "form-control"})
        }
