from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

class Family(models.Model):
    name = models.CharField(max_length=45)
    owner = models.ForeignKey('auth.User', related_name='families')  
    def __unicode__(self):
        return self.name

class Baby(models.Model):
    name = models.CharField(max_length=45)
    date_of_birth = models.DateTimeField('date of birth')
    family = models.ForeignKey(Family)
    def __unicode__(self):
        return self.name
    
class Activity(models.Model):
    name = models.CharField(max_length=64)
    family = models.ForeignKey(Family)
    def __unicode__(self):
        return self.name
    
class BabyEvent(models.Model):
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    baby = models.ForeignKey(Baby)
    activity = models.ForeignKey(Activity)
    def __unicode__(self):
        return self.baby + ':' + self.activity.name
    
class ActivityParameter(models.Model):
    description = models.CharField(max_length=256)
    datatype = models.CharField(max_length=16)    
    activity = models.ForeignKey(Activity)
    def __unicode__(self):
        return self.activity.name + ':' + self.description
    
class EventData(models.Model):
    data = models.CharField(max_length=512)
    baby_event = models.ForeignKey(BabyEvent)
    activity_parameters = models.ForeignKey(ActivityParameter)
    def __unicode__(self):
        return self.baby_event.__unicode__ + ':' + self.data            
