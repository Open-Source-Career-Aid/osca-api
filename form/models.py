from django.db import DefaultConnectionProxy, models

# Create your models here.


class Tag(models.Model):
    tagName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tagName


class Prerequisite(models.Model):
    prereqName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.prereqName


class Resource(models.Model):
    link = models.TextField(blank=True)
    thumbsup = models.IntegerField(default=0)
    thumbsdown = models.IntegerField(default=0)

    def __str__(self):
        return self.link


class Subtopic(models.Model):
    value = models.TextField(blank=True)
    resources = models.ManyToManyField(
        Resource, related_name="resources_subtopic", blank=True)

    def __str__(self):
        return self.value


class Topic(models.Model):
    topicName = models.TextField(blank=True)
    resources = models.ManyToManyField(
        Resource, related_name="resources_topic", blank=True)
    topic = models.ManyToManyField(
        Subtopic, related_name="subtopics_topic", blank=True)

    def __str__(self):
        return self.topicName

class Skill(models.Model):
    contributed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=30,blank=True)
    prerequisites = models.ManyToManyField(
        Prerequisite, related_name="all_skills_with_this_prerequisite", blank=True)
    tags = models.ManyToManyField(
        Tag, related_name="all_skills_with_this_tag", blank=True)
    levels = models.ManyToManyField(
        Level, related_name="all_skills_with_this_level", blank=True)

    def __str__(self):
        return self.skill


class Super_skill(models.Model):
    contributed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(
        Tag, related_name="super_skills_with_this_tag", blank=True)
    sub_skills = models.ManyToManyField(
        Skill, related_name="super_skill", blank=True)
    prerequisites = models.ManyToManyField(
        Prerequisite, related_name="all_super_skills_with_this_prerequisite", blank=True)

    def __str__(self):
        return self.name


class Super_skill_edit(models.Model):
    on_id = models.PositiveBigIntegerField(null=False)
    contributed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    sub_skills = models.ManyToManyField(Skill, blank=True)
    prerequisites = models.ManyToManyField(Prerequisite, blank=True)

    def __str__(self):
        return self.name


class User_messages(models.Model):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
