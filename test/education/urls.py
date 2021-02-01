from django.urls import path
from education.views import skill
urlpatterns = [
    path('Skill/',skill, name="skills"),
]
