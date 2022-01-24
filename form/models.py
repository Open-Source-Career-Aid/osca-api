from django.db import models
# from django.db.models.base import _Self
from vote.models import VoteModel
from django.db.models import Sum
from ordered_model.models import OrderedModel
# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=50, blank=True)
    organization_name = models.CharField(max_length=50, blank=True)
    branch_name = models.CharField(max_length=50, blank=True)
    program_duration = models.CharField(max_length=12, blank=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.userName



class Vote(models.Model):
    # vote_id = models.AutoField(primary_key=True)
    like = models.IntegerField(blank=True, default=0)
    dislike = models.IntegerField(blank=True, default=0)
    # user = models.OneToOneField(User, blank=True, on_delete=models.PROTECT)
    
    @property
    def vote_score(self):
        return self.like - self.dislike 

    def __str__(self):
        return str(self.vote_score)

class Tag(OrderedModel):
    tagName = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return self.tagName


class Prerequisite(OrderedModel):
    prereqName = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.prereqName


class Resource(Vote):
    link = models.TextField(blank=True)
    resource_vote = models.OneToOneField(Vote,default=0, related_name="vote_resource", parent_link=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.link


class Subtopic(OrderedModel,Vote):
    value = models.TextField(blank=True)
    resources = models.ManyToManyField(
        Resource, related_name="resources_subtopic", blank=True)
    subtopic_vote = models.OneToOneField(Vote, default=0, related_name="vote_subtopic",parent_link=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.value


class Topic(OrderedModel, Vote):
    topicName = models.TextField(blank=True)
    resources = models.ManyToManyField(
        Resource, related_name="resources_topic", blank=True)
    subtopics = models.ManyToManyField(
        Subtopic, related_name="subtopics_topic", blank=True)
    topic_vote = models.OneToOneField(Vote,default=0 , related_name="vote_topic",parent_link=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.topicName


class Level(models.Model):
    levelName = models.TextField(blank=True)
    topics = models.ManyToManyField(
        Topic,related_name="topics_level", blank=True)
    
    def __str__(self):
        return self.levelName



class Skill(OrderedModel):
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


class Super_skill(OrderedModel):
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


class User_messages(OrderedModel):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
