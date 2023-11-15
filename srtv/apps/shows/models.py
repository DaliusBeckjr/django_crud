from django.db import models
# reminder we put both classes together because of the video example

# creating the validations
# add it before the class because python isn't asynchronous
class showManager(models.Manager):
    def show_validate(self, postData):
        errors = {}
        
        # title validation
        if len(postData['title']) < 1:
            errors['title'] = 'Title is required'
        elif len(postData['title']) < 3:
            errors['title'] = 'Title must be more than 3 characters'
        # network validation
        if len(postData['network']) < 1:
            errors['network'] = 'Network is required'
        elif len(postData['network']) < 3:
            errors['network'] = 'Network must be more than 3 characters'
        # released on validation
        if len(postData['released_on']) < 1:
            errors['released_on'] = 'Released Date is required'
        elif len(postData['released_on']) < 3:
            errors['released_on'] = 'Released Date must be more than 3 characters'
        # description validation
        if len(postData['description']) < 1:
            errors['description'] = 'description is required'
        elif len(postData['description']) < 3:
            errors['description'] = 'description must be more than 3 characters'
        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # shows = [] -> reverse lookup

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    released_on = models.DateField()
    description = models.TextField()
    # one to many example (variable)
    creator = models.ForeignKey(User, related_name="shows", on_delete=models.CASCADE, null=True) # think of it as creator_id INT in flask+mySQL workbench
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = showManager() # using our val (custom manager) for the model


    def __str__(self):
        return f""" show object: ->
    id: {self.id} 
    title: {self.title} 
    network: ({self.network})
    released on: {self.released_on}
    description: {self.description}"""

