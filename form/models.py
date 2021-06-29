from django.db import models

# Create your models here.
class Tag(models.Model):
    value = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.value

class Prerequisite(models.Model):
    value = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.value

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

class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    organization_name = models.CharField(max_length=50, blank=True)
    branch_name = models.CharField(max_length=50, blank=True)
    program_duration = models.CharField(max_length=12, blank=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    contributed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50, blank=True)
    prerequisites = models.ManyToManyField(Prerequisite, related_name="all_skills_with_this_prerequisite", blank=True)
    tags = models.ManyToManyField(Tag, related_name="all_skills_with_this_tag", blank=True)
    detail = models.ManyToManyField(Topic, related_name="all_skills_with_this_topic", blank=True)

    def __str__(self):
        return self.skill


class Super_skill(models.Model):
    contributed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True)
    tags = models.ManyToManyField(Tag, related_name="super_skills_with_this_tag", blank=True)
    sub_skills=models.ManyToManyField(Skill,related_name="super_skill", blank=True)

    def __str__(self):
        return self.name

