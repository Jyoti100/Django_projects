from django.db import models
from django.utils import timezone
import datetime
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse
# Create your models here.
class Poll(models.Model):
    question=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
  #  slug = models.SlugField(unique=True)

   # def get_absolute_url(self):
    #    return reverse("detail", kwargs={"slug": self.slug})


    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description ='Published Recenlty'

# def create_slug(instance, new_slug=None):
#     slug=slugify(instance.question)
#     if new_slug is not None:
#         slug=new_slug
#     qs= Poll.objects.filter(slug=slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug='%s-%s'%(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
# def pre_save_poll_receiver(sender, instance, *args, **kwargs):
#     if instance.slug:
#         instance.slug=create_slug(instance)
#
# pre_save.connect(pre_save_poll_receiver, sender =Poll )

class Choice(models.Model):
    poll =models.ForeignKey(Poll, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes =models.IntegerField(default =0)

    def __unicode__(self):
        return self.choice_text


