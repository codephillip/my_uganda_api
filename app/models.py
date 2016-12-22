from django.db import models


class Ministry(models.Model):
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=250)
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=250)
    story = models.TextField()
    image = models.CharField(max_length=250, default='http://mstensaasfamily.com/wp-content/uploads/2015/10/uganda_grunge_flag_by_syndikata_np-d5oxmmv.jpg')
    ministry = models.ForeignKey(Ministry)
    district = models.ForeignKey(District)

    def __str__(self):
        return self.title


class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=250)
    story = models.TextField()
    ministry = models.ForeignKey(Ministry)
    location = models.CharField(max_length=250)
    image = models.CharField(max_length=250, default='http://mstensaasfamily.com/wp-content/uploads/2015/10/uganda_grunge_flag_by_syndikata_np-d5oxmmv.jpg')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
