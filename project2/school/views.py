from django.shortcuts import render
from school.models import Notice
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "index.html")
    
@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Notice.objects.order_by("-id")
        else:
            return Notice.objects.filter(branch=self.request.user.profile.branch).order_by("-id")

@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice