from django import forms

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Project Name', max_length=200,
                           widget=forms.TextInput(attrs={'class':'input'}))

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Task Title', max_length=200,
                           widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label='Description', max_length=400,
                           widget=forms.Textarea(attrs={'class':'input'}))
    project = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input'}))
