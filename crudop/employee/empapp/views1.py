from django.views import generic
from .models import Employee
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class EmpUpdateView(LoginRequiredMixin,UpdateView):
    model = Employee
    fields =['empname', 'empemail', 'empcontact']
    template_name = 'empapp/edit.html'
    success_url = reverse_lazy('show')

class EmpDeleteView(LoginRequiredMixin,DeleteView):
    model = Employee
    template_name ='empapp/employee_confirm_delete.html'
    success_url = reverse_lazy('show')

class ShowView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = 'empapp/show.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'all_employees'  # Default: object_list
    paginate_by = 5
    queryset = Employee.objects.all()


class EmpDetailView(LoginRequiredMixin,DetailView):
    model =Employee
    template_name = 'empapp/detail.html'

class EmployeeAddView(LoginRequiredMixin,CreateView):
        model = Employee
        fields = ['empname', 'empemail', 'empcontact']
        template_name = 'empapp/index.html'
        #success_url = reverse_lazy('show')

        def get_success_url(self):
            return reverse('show')