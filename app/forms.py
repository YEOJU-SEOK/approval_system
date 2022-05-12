from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('summary', 'description', 'start_time', 'end_time')
        # widget을 사용해 html input태그 생성
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'start_time': forms.TextInput(attrs={'class': 'form-control', }),
            'end_time': forms.TextInput(attrs={'class': 'form-control', }),
        }

    def clean_end_time(self):
        # cleaned_data : is_valid()함수로 값이 유효한 경우 여기에 저장된다고
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time <= start_time:
            raise forms.ValidationError('end time is faster than start time')
        return end_time

