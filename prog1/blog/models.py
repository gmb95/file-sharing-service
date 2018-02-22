from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
class ProfileFile(models.Model):
    image = models.FileField(upload_to='')
    text = models.TextField(max_length=256)

    def __unicode__(self):
            return unicode(self.image)