from django import forms

class EngineDiagnosticsForms(forms.Form):
    vehicle_model = forms.CharField(label='vehicle_model', max_length=100)
    vin = forms.CharField(label='vin', max_length=100)
    engine = forms.CharField(label='engine', max_length=100)


'''
    time = forms.DateTimeField(blank=True, null=True)
    location = forms.CharField(max_length=255, blank=True, null=True)
    # vehicle_model = forms.CharField(max_length=255, blank=True, null=True)
    vin = forms.CharField(max_length=255, blank=True, null=True)
    engine_type = forms.CharField(max_length=255, blank=True, null=True)
    engine_displacement = forms.CharField(max_length=255, blank=True, null=True)
    fault_code = forms.CharField(max_length=255, blank=True, null=True)
    fault_phenomenon = forms.CharField(max_length=255, blank=True, null=True)
    diagnosis = forms.CharField(max_length=255, blank=True, null=True)
'''