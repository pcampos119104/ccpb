from django import forms
from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    birth_dt = forms.DateField(
            widget=forms.SelectDateWidget(years=range(1900, 2040)), 
            label='Data nascimento',
            )
    member_since_dt = forms.DateField(
            widget=forms.SelectDateWidget(years=range(1900, 2040)),
            label='Membro desde')
    baptism_dt = forms.DateField(
            widget=forms.SelectDateWidget(years=range(1900, 2040)),
            label='Data de batismo')

