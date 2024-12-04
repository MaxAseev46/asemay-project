from django import forms
class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента",
        widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст клиента",
        widget=forms.NumberInput(attrs={"class": "myfield"}))
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        # fields = ['title', 'image']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = '__all__'

class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'
