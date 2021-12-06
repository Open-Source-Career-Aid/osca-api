from django.urls import path

from . import views,models,views_temp,views_user

urlpatterns = [
    path("get-all-skills/", views.get_all_skills,name="get all skills"),
    path("get-all-super-skills/", views.get_all_super_skills,name="get all super skills"),
    path("post-skill/", views.post_skill,name="add new skill"),
    path("post-super-skill/", views.post_super_skill,name="add new super skill"),
    path("get-suggestions/", views.get_suggestions,name="get suggestions"),
    path("get-super-skill/", views.get_super_skill,name="get super skill"),
    path("get-skill/", views.get_skill,name="get skill"),
    path("learn-skill/", views.learn_skill,name="learn skill"),
    path("post-skill-temp/", views_temp.post_skill_temp,name="post temp skill"),
    path("post-super-skill-temp/", views_temp.post_super_skill_temp,name="post temp super skill"),
    path("get-all-skills-temp/", views_temp.get_all_skills,name="get all skills"),
    path("get-all-super-skills-temp/", views_temp.get_all_super_skills,name="get all super skills"),
    path("post-user-message/",views_user.post_user_message, name="post user message"),
    path("post-resource-vote/",views.post_vote_resource, name="post resource vote"),
    path("post-subtopic-vote/",views.post_vote_subtopic, name="post subtopic vote"),
    path("post-topic-vote/",views.post_vote_topic, name="post topic vote"),
    path("get-all-votes/", views.get_votes, name="get all votes"),
    path("get-all-resources/", views.get_resources, name="get all resources"),

]