from django import forms



class CommentForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput)
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea)
    # accept_terms = forms.BooleanField(label='Accept Terms and Conditions', widget=forms.CheckboxInput)