from django.db import models

# Create your models here.

class Resource(models.Model):
    value = models.TextField(blank=True);

    def __str__(self):
        return self.value
    

class Subtopic(models.Model):
    value = models.TextField(blank=True);
    resources = models.ManyToManyField(Resource, related_name="resources_subtopic", blank=True);

    def __str__(self):
        return self.value

class Topic(models.Model):
    value = models.TextField(blank=True)
    resources = models.ManyToManyField(Resource,related_name="resources_topic", blank=True)
    subtopics = models.ManyToManyField(Subtopic, related_name="subtopics_topic",blank=True)

    def __str__(self):
        return self.value

class Tag(models.Model):
    value = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.value

class Prerequisite(models.Model):
    value = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.value

class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    organizationName = models.CharField(max_length=50, blank=True)
    branchName = models.CharField(max_length=50, blank=True)
    skill = models.CharField(max_length=50, blank=True)
    graduatingYear = models.CharField(max_length=12, blank=True)
    prerequisites = models.ManyToManyField(Prerequisite, related_name="prerequisites", blank=True)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    detail = models.ManyToManyField(Topic, related_name="topics_skill", blank=True)

    def __str__(self):
        return self.name
