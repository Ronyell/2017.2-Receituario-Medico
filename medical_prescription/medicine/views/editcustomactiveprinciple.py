# Django
import time
from django.views.generic import UpdateView

from medicine.models import ActivePrinciple
from medicine.forms import CustomActivePrincipleForm


class EditCustomActivePrinciple(UpdateView):
    model = ActivePrinciple  # Defines which model will be edited
    form_class = CustomActivePrincipleForm  # Class forms.py define how the form will be
    template_name = 'register_custom_principle.html'   # Template define html redirect create
    success_url = '/medicine/list/'  # Redirect this url when post is success

    def get(self, request, *args, **kwargs):
        return super(EditCustomActivePrinciple, self).post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        time.sleep(0.4)  # Time to wait to inform the creation of the principle
        return super(EditCustomActivePrinciple, self).post(request, *args, **kwargs)
