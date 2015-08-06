from django.db import models
<<<<<<< HEAD
from django.utils import timezone
import datetime

# Create your models here.

=======
import datetime
from django.utils import timezone

# Create your models here.


>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

<<<<<<< HEAD
    def __str__(self):              # __unicode__ on Python 2
=======
    def __unicode__(self):
>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
<<<<<<< HEAD

=======
>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

<<<<<<< HEAD
=======

>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

<<<<<<< HEAD
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
=======
    def __unicode__(self):
        return self.choice_text
>>>>>>> 201094cea5538c2ff459630ce6e1396813bee7fd
