from django.contrib import admin

from .models import Team
from .models import Player
from .models import Game
from .models import Match
from .models import Tournament

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Match)
admin.site.register(Tournament)
