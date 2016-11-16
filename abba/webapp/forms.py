from django.forms import ModelForm
from webapp.models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
