from django import forms

from WebApp.models import *

class WaiterModelForm(forms.ModelForm):
    class Meta:
        model = Waiter

        fields = ['name', 'salary', 'restaurant',]

        widgets = {'name': forms.TextInput,}

    def clean(self):
        cleaned_data = super(WaiterModelForm, self).clean()

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError("Please type in name.")

        return name

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')

        if not salary:
            raise forms.ValidationError("Please type in salary.")

        return salary

    def clean_restaurant(self):
        restaurant = self.cleaned_data.get('restaurant')

        if not restaurant:
            raise forms.ValidationError("Please type in restaurant.")

        return restaurant


class PlaceModelForm(forms.ModelForm):
    class Meta:
        model = Place

        fields = ['street', 'city', 'state',]

        widgets = {'street': forms.TextInput,
                   'city': forms.TextInput,
                   'state': forms.TextInput}

    def clean(self):
        cleaned_data = super(PlaceModelForm, self).clean()

        print(cleaned_data)

        return cleaned_data

    def clean_street(self):

        street = self.cleaned_data.get('street')

        if not street:
            raise forms.ValidationError('Please type in street.')

        return street

    def clean_city(self):
        city = self.cleaned_data.get('city')

        if not city:
            raise forms.ValidationError("Please type in city.")

        return city

    def clean_state(self):
        state = self.cleaned_data.get('state')

        if not state:
            raise forms.ValidationError('Please type in state.')

        return state


class RestaurantModelForm(forms.ModelForm):
    class Meta:
        model = Restaurant

        fields = ['name', 'place', 'serves_hot_dogs', 'serves_pizzas',]

        widgets = {'name': forms.TextInput,}

        labels = {'serves_hot_dogs': 'serves hot dogs?',
                  'serves_pizzas': 'serves pizza?'}

    def clean(self):
        cleaned_data = super(RestaurantModelForm, self).clean()

        return cleaned_data

    def clean_name(self):

        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError("Please type in name.")

        return name

    def clean_place(self):

        place = self.cleaned_data.get('place')

        if not place:
            raise forms.ValidationError("Please type in place.")

        return place

    def clean_serves_hot_dogs(self):

        serves_hot_dogs = self.cleaned_data.get('serves_hot_dogs')

        if serves_hot_dogs == None:
            raise forms.ValidationError("Please type in serves_hot_dogs.")

        return serves_hot_dogs

    def clean_serves_pizzas(self):

        serves_pizzas = self.cleaned_data.get('serves_pizzas')

        if serves_pizzas == None:
            raise forms.ValidationError("Please type in serves_pizzas")

        return serves_pizzas