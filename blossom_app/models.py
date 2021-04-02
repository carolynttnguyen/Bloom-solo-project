from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def LoginValidator(self, LogData):
        errors={}
        # Login Error Messages
        if len(LogData['log_username']) < 5:
            errors['log_username'] = 'Please input a valid Username.'
        # if LogData['log_username'] != 
        if len(LogData['log_password']) < 8:
            errors['log_password'] = 'Please input a valid Password.'
        return errors
    
    def RegistrationValidator(self, RegData):
        errors = {}
        EMAIL_REGEX = re.compile( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Registration error messages
        # first name
        if len(RegData['first_name']) < 2:
            errors['first_name']= 'First Name must be at least 2 characters.'
        # last name
        if len(RegData['last_name']) < 2:
            errors['last_name']= 'Last Name must be at least 2 characters.'
        # email
        if not EMAIL_REGEX.match(RegData['email']):
            errors['email'] = 'Email format is incorrect.'
        # username
        if len(RegData['username']) < 5:
            errors['username']= 'Username must be at least 5 characters.'
        # password
        if len(RegData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        # confirm pw
        if RegData['password'] != RegData['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match!!!'
        # quote
        if len(RegData['personal_quote']) < 1:
            errors['personal_quote'] = 'A quote must be provided to register.'
        # reason
        if len(RegData['reasons']) < 1:
            errors['reasons'] = 'Your reason for joining must be provided for in order to register.'
        return errors


class Users (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password =  models.CharField(max_length=70)
    reasons = models.TextField()
    personal_quote = models.TextField()
    # avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    #friends = list of friends user has
    #regulators


class Chat_rules(models.Model):
    rulecreator = models.ForeignKey(Users, related_name='chat_rules', on_delete=models.CASCADE)
    rule = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    

# class Friends(models.Model):
#     user = models.ForeignKey(Users, related_name='friends', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)


# class Regulators(models.Model):
#     user = models.ForeignKey(Users, related_name='regulators', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)


class Journal_Entires(models.Model):
    entry = models.TextField()
    user = models.ForeignKey(Users, related_name='journal_entry', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

# class Pictures(models.Model):
#     picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
#     user = models.ForeignKey(Users, related_name='picture', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)

class Quotes(models.Model):
    the_quote = models.TextField(null=True)
    quote_author = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(Users, related_name='quote', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Goals (models.Model):
    goal = models.TextField()
    user = models.ForeignKey(Users, related_name='goal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Intentions (models.Model):
    intention = models.TextField()
    user = models.ForeignKey(Users, related_name='intention', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

# class Comments(models.Model):
#     user = models.ForeignKey(Users, related_name='comment', on_delete=models.CASCADE)
#     picture = models.ForeignKey(Users, related_name='picture_comment', on_delete=models.CASCADE)
#     quote = models.ForeignKey(Users, related_name='quote_comment', on_delete=models.CASCADE)
#     journal_entry = models.ForeignKey(Users, related_name='entry_comment', on_delete=models.CASCADE)
#     comment = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)
