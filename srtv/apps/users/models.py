from django.db import models


import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        if len(postData["first_name"]) < 1:
            errors["first_name"] = "first Name field is required"
        elif len(postData["first_name"]) < 3:
            errors["first_name"] = "First Name field must be more than 3 characters"

        # last name validation
        if len(postData["last_name"]) < 1:
            errors["last_name"] = "Last Name field is required"
        elif len(postData["last_name"]) < 3: 
            errors["last_name"] = "Last Name field must be more than 3 characters"

        # email validaation
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "invalid email address"
        elif len(postData['email']) < 1:
            errors['email'] = "Email field is required"

        # password validation
        if len(postData["password"]) < 1:
            errors['password'] = "Password field is required"
        elif len(postData["password"]) < 8:
            errors["password"] = "Password needs to be more than 8 characters"

        # confirm password 
        # if len(postData["confirm_pw"]) < 1:
        #     errors['confirm_pw'] = "Confirm password field is required"
        # # match passwords
        # elif postData["password"] != postData["confirm_pw"]:
        #     errors["confirm_pw"] = "Passwords have to match"
        return errors

class LoginManager(models.Manager):
    def login_validator(self, postData):
        errors = {}


        # email validaation
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "invalid email address"
        elif 'email' not in postData or not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email field is required"

        # password validation
        if len(postData["password"]) < 1:
            errors['password'] = "Password field is required"
        elif len(postData["password"]) < 8:
            errors["password"] = "Password needs to be more than 8 characters"
        elif 'password' not in postData or not postData['password']:
            errors['password'] = "password field is required"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    additional_objects = LoginManager()

    def __str__(self):
        return f"""user object():
                    first_name: {self.first_name}
                    last_name: {self.last_name}
                    email: {self.email}   """
