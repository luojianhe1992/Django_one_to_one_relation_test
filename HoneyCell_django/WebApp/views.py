from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *


@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)



# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('message'))

@login_required
def message(request):
    print("in the message function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/message.html', context)

@login_required
def upload(request):
    print("in the upload function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/upload.html', context)

@login_required
def preprocess(request):
    print("in the preprocess function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/preprocessing.html', context)

@login_required
def visualization(request):
    print("in the visualization function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/knnresult.html', context)

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def honeycell(request):
    print("in the honeycell function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycell.html', context)

@login_required
def honeycomb(request):
    print("in the honeycomb function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycomb.html', context)

@login_required
def analytics(request):
    print("in the analytics function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/analytics.html', context)

from WebApp.forms import *

@login_required
def add_waiter(request):
    print("in the add_waiter function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_waiter function.")

        form = WaiterModelForm()
        context['form'] = form

        return render(request, 'WebApp/add_waiter.html', context)

    else:
        print("in the POST method of add_waiter function.")

        form = WaiterModelForm(request.POST, request.FILES)
        context['form'] = form

        if not form.is_valid():
            print("The form is not valid.")
            errors.append("The form is not valid.")

            return render(request, 'WebApp/add_waiter.html', context)
        print("The form is valid.")

        name = form.clean_name()
        salary = form.clean_salary()
        restaurant = form.clean_restaurant()

        print("%" * 30)
        print(name)
        print(salary)
        print(restaurant)
        print("%" * 30)

        if len(Waiter.objects.filter(name=name)):
            print("The name already exist.")
            errors.append("The name already exist.")

            return render(request, 'WebApp/add_waiter.html', context)

        form.save()
        print("Already save the form.")

        return render(request, 'WebApp/add_waiter.html', {'user': request.user, 'form': WaiterModelForm()})

@login_required
def show_waiters(request):
    print("in the show_waiters function.")

    context = {}
    context['user'] = request.user

    waiters = Waiter.objects.all()
    context['waiters'] = waiters

    return render(request, 'WebApp/show_waiters.html', context)



@login_required
def add_place(request):
    print("in the add_place function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_place function.")

        form = PlaceModelForm()
        context['form'] = form

        return render(request, 'WebApp/add_place.html', context)

    else:
        print("in the POST method of add_place function.")

        print(request.POST)

        form = PlaceModelForm(request.POST, request.FILES)
        context['form'] = form

        print(form)

        if not form.is_valid():
            print("The form is not valid.")
            errors.append("The form is not valid.")

            print("%" * 30)
            print(form)
            print("%" * 30)

            return render(request, 'WebApp/add_place.html', context)
        print("The form is valid.")

        street = form.clean_street()
        city = form.clean_city()
        state = form.clean_state()

        print("%" * 30)
        print(street)
        print(city)
        print(state)
        print("%" * 30)

        if len(Place.objects.filter(street=street, city=city, state=state)):
            print("The street, city, state already exist.")
            errors.append("The street, city, state already exist.")

            return render(request, 'WebApp/add_place.html', context)

        form.save()
        print("Already save the form.")

        return render(request, 'WebApp/add_place.html', {'user': request.user, 'form': PlaceModelForm()})

@login_required
def show_places(request):
    print("in the show_places function.")

    context = {}
    context['user'] = request.user

    places = Place.objects.all()
    context['places'] = places

    return render(request, 'WebApp/show_places.html', context)




@login_required
def add_restaurant(request):
    print("in the add_restaurant function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_restaurant function.")

        form = RestaurantModelForm()
        context['form'] = form

        return render(request, 'WebApp/add_restaurant.html', context)

    else:
        print("in the POST method of add_restaurant function.")

        form = RestaurantModelForm(request.POST, request.FILES)
        context['form'] = form

        if not form.is_valid():
            print("The form is not valid.")
            errors.append("The form is not valid.")

            return render(request, 'WebApp/add_restaurant.html', context)
        print("The form is valid.")

        name = form.clean_name()
        place = form.clean_place()
        serves_hot_dogs = form.clean_serves_hot_dogs()
        serves_pizzas = form.clean_serves_pizzas()

        print("%" * 30)
        print(name)
        print(place)
        print(serves_hot_dogs)
        print(serves_pizzas)
        print("%" * 30)

        if len(Restaurant.objects.filter(name=name)):
            print("The name already exist.")
            errors.append("The name already exist.")

            return render(request, 'WebApp/add_restaurant.html', context)

        if len(Restaurant.objects.filter(place=place)):
            print("The place already exist.")
            errors.append("The place already exist.")

            return render(request, 'WebApp/add_restaurant.html', context)


        form.save()
        print("Already save the form.")

        return render(request, 'WebApp/add_restaurant.html', {'user': request.user, 'form': RestaurantModelForm()})


@login_required
def show_restaurants(request):
    print("in the show_restaurants function.")

    context = {}
    context['user'] = request.user

    restaurants = Restaurant.objects.all()
    context['restaurants'] = restaurants

    return render(request, 'WebApp/show_restaurants.html', context)




@login_required
def restaurant_detail(request, restaurant_id):
    print("in the function of restaurant_detail.")

    print(request)
    print(restaurant_id)

    context = {}
    context['user'] = request.user

    restaurant = Restaurant.objects.get(id=restaurant_id)
    context['restaurant'] = restaurant

    return render(request, 'WebApp/restaurant_detail.html', context)


@login_required
def add_waiter_restaurant(request, restaurant_id):
    print("in the function add_waiter_restaurant.")

    print(request)
    print(restaurant_id)

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    restaurant = Restaurant.objects.get(id=restaurant_id)
    context['restaurant'] = restaurant

    if request.method == "GET":

        print("in the GET method of add_waiter_restaurant.")

        return render(request, 'WebApp/add_waiter_restaurant.html', context)
    else:

        print("in the POST method of add_waiter_restaurant.")

        waiter_name = request.POST['waiter_name']
        waiter_salary = request.POST['waiter_salary']

        if not (waiter_name and waiter_salary):
            print("There are some fields which are None.")
            errors.append("There are some fields which are None.")

            context['waiter_name'] = waiter_name
            context['waiter_salary'] = waiter_salary

            return render(request, 'WebApp/add_waiter_restaurant.html', context)

        if len(Waiter.objects.filter(name=waiter_name)):
            print("The waiter name already exist.")
            errors.append("The waiter name already exist.")

            context['waiter_name'] = waiter_name
            context['waiter_salary'] = waiter_salary

            return render(request, 'WebApp/add_waiter_restaurant.html', context)

        new_waiter_instance = Waiter(name=waiter_name,
                                     salary=waiter_salary,
                                     restaurant=restaurant)
        new_waiter_instance.save()
        print("Already save new_waiter_instance.")

        return HttpResponseRedirect(reverse("show_restaurants"))





@login_required
def place_detail(request, place_id):
    print("in the place_detail function.")

    print(request)
    print(place_id)

    context = {}
    context['user'] = request.user

    place = Place.objects.get(id=place_id)
    context['place'] = place

    return render(request, 'WebApp/place_detail.html', context)



@login_required
def add_restaurant_place(request, place_id):
    print("in the add_restaurant_place function.")

    print(request)
    print(place_id)

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    place = Place.objects.get(id=place_id)
    context['place'] = place

    if request.method == "GET":
        print("in the GET method of add_restaurant_place function.")

        return render(request, 'WebApp/add_restaurant_place.html', context)

    else:
        print("in the POST method of add_restaurant_place function.")


        print(request.POST)



        print("%" * 30)
        print(request.POST.get('severs_hot_dogs'))
        print(request.POST.get('serves_pizzas'))
        print("%" * 30)


        restaurant_name = request.POST['restaurant_name']
        serves_hot_dogs = request.POST.get('severs_hot_dogs')
        serves_pizzas = request.POST.get('serves_pizzas')

        if serves_hot_dogs == True:
            print("it works.")
        else:
            print("it does not work.")

        serves_hot_dogs_value = python_switch(serves_hot_dogs)
        serves_pizzas_value = python_switch(serves_pizzas)

        context['restaurant_name'] = restaurant_name

        if len(Restaurant.objects.filter(name=restaurant_name)):
            errors.append("The restaurant name already exist.")

            return render(request, 'WebApp/add_restaurant_place.html', context)

        if serves_hot_dogs_value == None:
            errors.append("Please choose if serves hot dogs.")

            return render(request, 'WebApp/add_restaurant_place.html', context)

        if serves_pizzas_value == None:
            errors.append("Please choose if serves pizzas.")

            return render(request, 'WebApp/add_restaurant_place.html', context)


        new_restaurant_instance = Restaurant(name=restaurant_name,
                                             serves_hot_dogs=serves_hot_dogs_value,
                                             serves_pizzas=serves_pizzas_value,
                                             place=place)
        new_restaurant_instance.save()
        print("Already save the new_restaurant_instance.")

        # Pass args in the reverse function.
        return HttpResponseRedirect(reverse('place_detail', kwargs={'place_id': place.id}))



def python_switch(x):
    return {'None': None,
            'True': True,
            'False': False}[x]