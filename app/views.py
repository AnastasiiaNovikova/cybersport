from django.shortcuts import render
from django.http import HttpResponse

from .models import Team, Player
from rest_framework import viewsets
from .serializers import TeamSerializer


def index(request):
    return render(request, 'app/index.html')
    # return HttpResponse("Hello! You're at the app index.")


def teams_list(request):
    all_teams_list = Team.objects.all()
    # output = ', '.join([q.question_text for q in all_teams_list])
    return HttpResponse(all_teams_list)


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()