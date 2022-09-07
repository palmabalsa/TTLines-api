from django.db import models
from django.conf import settings
from django.utils import timezone

class FishingLogEntry (models.Model):

    fishSpecies = (
        ('Rainbow', 'Rainbow'),
        ('Brown', 'Brown'),
    )
    fishCondition = (
        # ('Sick/Spawning', 'Sick/Spawning'),
        ('Spent', 'Spent'),
        ('Average', 'Average'),
        ('Good', 'Good'),
        ('Sashimi(Excellent)', 'Sashimi(Excellent)')
    )
    riverName = (
        ('Tongariro', 'Tongariro'),
        ('Tauranga Taupo', 'Tauranga Taupo'),
        ('Lake O', 'Lake O'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='firebase_user_id', default='noFirebaseUserID', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    river = models.CharField(choices = riverName, max_length=14, default=None, blank=True, null=True,)
    river_pool = models.CharField(verbose_name= 'what pool?', max_length=20, default=None, blank=True, null=True,)
    lat = models.DecimalField(verbose_name= 'lat', decimal_places= 16,max_digits=22, default=None, blank=True, null=True)
    lon =  models.DecimalField(verbose_name= 'lon', decimal_places= 16,max_digits=22, default=None, blank=True, null=True)
    river_level = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    air_pressure = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_species = models.CharField(choices=fishSpecies, max_length=7, default=None, blank=True, null=True,)
    fish_weight = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_length = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_condition = models.CharField(choices=fishCondition, max_length=18, default=None, blank=True, null=True, )
    kept_or_released = models.BooleanField(verbose_name='Kept for dinner?', default=None, blank=True, null=True,)
    fly_used = models.CharField(max_length=25,default=None, blank=True, null=True)
    any_notes = models.CharField(max_length=100, default=None, blank=True, null=True)

    objects = models.Manager()
    
    class Meta:
          ordering = ('date',)
    
    def __str__(self):
        return self.fish_species