from django import forms
from .models import Mobile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['model_name', 'company_name', 'price','os', 'processor', 'data_transfer', 'processor_speed']

        def clean_model_name(self):
            model_name = self.cleaned_data.get('model_name')
            return model_name
        
        def clean_company_name(self):
            company_name = self.cleaned_data.get('company_name')
            return company_name

        def clean_price(self):
            price = self.cleand_data.get('price')
            return price

        def clean_os(self):
            os = self.cleand_data.get('os')
            return os

        def clean_processor(self):
            processor = self.cleand_data.get('processor')
            return processor
        
        def clean_data_transfer(self):
            data_transfer = self.cleand_data.get('data_transfer')
            return data_transfer
        
        def clean_processor_speed(self):
            processor_speed = self.cleand_data.get('processor_speed')
            return processor_speed 

        