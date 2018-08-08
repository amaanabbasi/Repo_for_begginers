Whenever, a user logs in it is redirected to this url.

# How to Use Django's built in Login system

Django comes with a lot of built in resources for the most common cases of a web app. The registration app is one of them.

We will build a basic login and logout system.

# Configure the URL routes

In `mysite/urls.py`:

```python
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
```
We have to tell django to which page should a user be redirected, when it is successfully logged in.

In the `settings.py` file, setup `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL`, to desired url paths.
In our case, we'll set them to:

```python

LOGIN_REDIRECT_URL = 'insta:userdetail'
LOGOUT_REDIRECT_URL = 'index'
```
Similarily, we'll setup , `LOGIN_URL`, `LOGOUT_URL`.

```python

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
```

There is one thing left, `@login_required` decorator. What this does is that it redirects a user to the login page, if it is not logged in. 

We will use it for our `userdetail` view:

`insta/views.py`

```
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def userdetail(request, *args, **kwargs):
    print(request)
    print(args)
    print(kwargs)
    return render(request, 'insta/dashboard.html', {})
```

We haven't made a `login` template.
By default, Django looks for a `login.html` file. We'll create that file at: `templates/registration/login.html`.

This file will contain a basic Login form.

`login.html`:

```html
    
    {% extends 'base.html' %}

    {% block body %}
      <h2>Login</h2>
      <div class="col-sm-5">
        <form method="post">
          {% csrf_token %}
          {{ form.as_p }}
          <button type="submit">Login</button>
        </form>
        <br>
        <p><strong>-- OR --</strong></p>
        <a href="{% url 'social:begin' 'github' %}">Login with GitHub</a><br>
      </div>  
    {% endblock body %}

```

Login system is now ready.









