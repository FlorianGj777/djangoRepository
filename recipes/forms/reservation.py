from django import forms


class ReservationForm(forms.Form):
    date = forms.DateField(label="date")

    def clean(self):
        pass

    def clean_date(self):
        if self.cleaned_data['date'] == '':
            self.add_error('date', 'date can t be empty:')
        return self.cleaned_data['date']
