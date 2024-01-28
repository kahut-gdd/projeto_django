from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Kahut


class KahutListView(ListView):
    model = Kahut


class KahutCreateView(CreateView):
    model = Kahut
    fields = ["tittle", "deadline"]
    success_url = reverse_lazy("kahut_list")


class KahutUpdateView(UpdateView):
    model = Kahut
    fields = ["tittle", "deadline"]
    success_url = reverse_lazy("kahut_list")


class KahutDeleteView(DeleteView):
    model = Kahut
    success_url = reverse_lazy("kahut_list")


class KahutCompleteView(View):
    def get(self, request, pk):
        kahut =  get_object_or_404(Kahut, pk=pk)
        kahut.mark_has_complete()
        return redirect("kahut_list")