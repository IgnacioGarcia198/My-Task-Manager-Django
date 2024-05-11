from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],  # This format must match the input's string
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'step': 60,  # Increment of step in seconds (set to 60 for minute-wise selection)
            'class': 'input'  # Add a class for styling
        }),
    )
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 6,
        'class': 'textarea'  # Use class instead of 'cols' and inline styles
    }))
    is_done = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}),
        label='Done',
        required=False
    )
    class Meta:
        model = Task
        fields = ['title', 'text', 'due_date', 'is_done']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input'})  # Apply consistent input class
        self.fields['is_done'].widget.attrs.update({'class': 'checkbox'})
        self.fields['is_done'].initial = False
