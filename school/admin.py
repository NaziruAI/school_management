from django.contrib import admin
from .models import School, Section, SchoolClass, Student, Subject, Teacher, Score


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)
    search_fields = ('name',)

@admin.register(SchoolClass)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')
    list_filter = ('section',)
    search_fields = ('name',)

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'continuous_assessment', 'exam_score', 'total_score')
    search_fields = ('student__first_name', 'student__last_name', 'subject__name')
    list_filter = ('subject', 'student__school_class')

    # Make the total score read-only since it's derived
    readonly_fields = ('total_score',)

    def total_score(self, obj):
        return obj.total_score
    total_score.short_description = 'Total Score'



from django import forms

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student', 'subject', 'continuous_assessment', 'exam_score']

    def clean_continuous_assessment(self):
        ca = self.cleaned_data['continuous_assessment']
        if ca < 0 or ca > 30:
            raise forms.ValidationError("CA score must be between 0 and 30.")
        return ca

    def clean_exam_score(self):
        exam = self.cleaned_data['exam_score']
        if exam < 0 or exam > 70:
            raise forms.ValidationError("Exam score must be between 0 and 70.")
        return exam


class ScoreAdmin(admin.ModelAdmin):
    form = ScoreForm
