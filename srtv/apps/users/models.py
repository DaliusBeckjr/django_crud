from django.db import models


import re



class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData["first_name"]) < 0:
            errors["first_name"] = "first Name field cannot be empty"
        
        
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "invalid email address"
        return errors



class User(models.Model):
    first_name = models.Charfield(max_length=45)
    last_name = models.Charfield(max_length=45)
    email = models.Emailfield(unique=True)
    password = models.Charfield(max_length = 60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""user object():
                    first_name: {first_name}
                    last_name: {last_name}
                    email: {email}   """
