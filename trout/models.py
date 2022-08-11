from django.db import models
from django.conf import settings
from django.utils import timezone

# create a model manager????

class FishingLogEntry (models.Model):

    fishSpecies = (
        ('Rainbow', 'Rainbow'),
        ('Brown', 'Brown'),
    )
    fishCondition = (
        ('Sick/Spawning', 'Sick or spawning'),
        ('Average', 'Average'),
        ('Healthy', 'Healthy'),
        ('Sashimi', 'Sashimi')
    )
    riverName = (
        ('Tongariro', 'Tongariro'),
        ('Tauranga Taupo', 'Tauranga Taupo'),
        ('Lake O', 'Lake O'),
    )
        #  to_field='firebase_user_id'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    river = models.CharField(choices = riverName, max_length=14, default=None, blank=True, null=True,)
    river_pool = models.CharField(verbose_name= 'what pool?', max_length=20)
    river_geotag = models.CharField(verbose_name= 'geotag coordinates option here', max_length=20, default=None, blank=True, null=True)
    river_level = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True) #these 2 want to be populated w my weather data
    air_pressure = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True) #these 2 want to be populated w my weather data
    fish_species = models.CharField(choices=fishSpecies, max_length=7, default=None, blank=True, null=True,)
    fish_weight = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_length = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_condition = models.CharField(choices=fishCondition, max_length=13, default=None, blank=True, null=True, )
    kept_or_released = models.BooleanField(verbose_name='Kept for dinner?', default=None, blank=True, null=True,) #how to implemet this?
    fly_used = models.CharField(max_length=25)
    any_notes = models.CharField(max_length=100)
    # whats this ? is it necessary?
    objects = models.Manager()#default manager
    
    
    
    class Meta:
          ordering = ('date',)
    
    def __str__(self):
        return self.fish_species
    # ^this means youll be able to see this is the admin dashboard
    # what to identify your database via - good question, what would mine be? date?