from django import forms
from .models import CLT,SCD,CFC,IIPC,SRI
class CLTForm(forms.ModelForm):
    class Meta:
        model = CLT
        fields = ['username','event_name', 'college_name', 'date', 'prize_won', 'position']
        
class SCDForm(forms.ModelForm):
    class Meta:
        model = SCD
        fields = ['username','event_name', 'college_name', 'date', 'prize_won', 'position']

class CFCForm(forms.ModelForm):
    class Meta:
        model = CFC
        fields = ['username','event_name', 'college_name', 'date']
        
class IIPCForm(forms.ModelForm):
    class Meta:
        model = IIPC
        fields = ['username','program','date']
        
class SRIForm(forms.ModelForm):
    class Meta:
        model = SRI
        fields = ['username','club']