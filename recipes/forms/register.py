from django import forms


class RegisterForm(forms.Form):
    user_name = forms.CharField(label="User name",
                                 max_length=100)
    email = forms.EmailField(label="Email",
                                max_length=100)
    password = forms.CharField(label="Password",
                                min_length=5,
                                max_length=100,
                                widget=forms.PasswordInput())

    def clean(self):
        pass

    def clean_user_name(self):
        if self.cleaned_data['user_name'] == '':
            self.add_error('user_name', 'First name can t be empty:')
        return self.cleaned_data['user_name']

    def clean_email(self):
        if self.cleaned_data['email'] == '':
            self.add_error('email', 'email name can t be empty:')
        return self.cleaned_data['email']

    def clean_password(self):
        if self.cleaned_data['password'] == '':
            self.add_error('password', 'password name can t be empty:')
        return self.cleaned_data['password']
