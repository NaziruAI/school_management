from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import School, Section, Class

# List views
class SchoolListView(ListView):
    model = School
    template_name = 'school/school_list.html'
    context_object_name = 'schools'

class SectionListView(ListView):
    model = Section
    template_name = 'school/section_list.html'
    context_object_name = 'sections'

class ClassListView(ListView):
    model = Class
    template_name = 'school/class_list.html'
    context_object_name = 'classes'

# Detail views
class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'
    context_object_name = 'school'

class SectionDetailView(DetailView):
    model = Section
    template_name = 'school/section_detail.html'
    context_object_name = 'section'

class ClassDetailView(DetailView):
    model = Class
    template_name = 'school/class_detail.html'
    context_object_name = 'class'
