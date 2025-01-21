from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from .models import School, Section, SchoolClass, Score, Student, Subject


# List Views
class IndexView(ListView):
    model = SchoolClass
    template_name = "school/index.html"
    context_object_name = "school_classes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()  # Add students to the context
        return context

class SchoolListView(ListView):
    model = School
    template_name = 'school/school_list.html'
    context_object_name = 'schools'


class SectionListView(ListView):
    model = Section
    template_name = 'school/section_list.html'
    context_object_name = 'sections'


class ClassListView(ListView):
    model = SchoolClass
    template_name = 'school/class_list.html'
    context_object_name = 'classes'


# Detail Views
class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'
    context_object_name = 'school'


class SectionDetailView(DetailView):
    model = Section
    template_name = 'school/section_detail.html'
    context_object_name = 'section'


class ClassDetailView(DetailView):
    model = SchoolClass
    template_name = 'school/class_detail.html'
    context_object_name = 'school_class'



