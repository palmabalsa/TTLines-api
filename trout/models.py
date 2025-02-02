from django.db import models
from django.conf import settings
from django.utils import timezone



# class FishingSession (models.Model):
#     fishing_time_start = models.DateTimeField()
#     fishing_time_end = models.DateTimeField()
#     fishing_time_duration = models.DateTimeField()


class FishingLogEntry (models.Model):

    fishSpecies = (
        ('Rainbow', 'Rainbow'),
        ('Brown', 'Brown'),
    )
    fishCondition = (
        ('Spent', 'Spent'),
        ('Average', 'Average'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent')
    )
    keptOrReleased = (
        ('Kept', 'Kept'),
        ('Released', 'Released'),
    )
    region = (
        ('Northland', 'Northland'),
        ('Auckland/Waikato', 'Auckland/Waikato'),
        ('Eastern/Rotorua', 'Eastern/Rotorua'),
        ('Hawke\'s Bay', 'Hawke\'s Bay'),
        ('Taupo/Turangi', 'Taupo/Turangi'),
        ('Taranaki', 'Taranaki'),
        ('Wellington', 'Wellington'),
        ('Nelson/Marlborough', 'Nelson/Marlborough'),
        ('North Canterbury', 'North Canterbury'),
        ('West Coast', 'West Coast'),
        ('Central South Island', 'Central South Island'),
        ('Otago', 'Otago'),
        ('Southland', 'Southland')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='firebase_user_id', default='noFirebaseUserID', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    region = models.CharField(choices=region, max_length=20, default='None', blank=True, null=True)
    river = models.CharField(verbose_name='river', max_length=30, default=None, blank=True, null=True)
    river_pool = models.CharField(verbose_name= 'what pool?', max_length=20, default=None, blank=True, null=True,)
    lat = models.DecimalField(verbose_name= 'lat', decimal_places= 16,max_digits=22, default=None, blank=True, null=True)
    lon =  models.DecimalField(verbose_name= 'lon', decimal_places= 16,max_digits=22, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=254, default=None, blank=True, null=True)
    river_level = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    air_pressure = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_species = models.CharField(choices=fishSpecies, max_length=7, default=None, blank=True, null=True,)
    fish_weight = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_length = models.DecimalField(decimal_places=2,max_digits=5, default=None, blank=True, null=True)
    fish_condition = models.CharField(choices=fishCondition, max_length=19, default=None, blank=True, null=True, )
    kept_or_released = models.CharField(choices=keptOrReleased,verbose_name='Kept for dinner?', max_length=8, default=None, blank=True, null=True,)
    fly_used = models.CharField(max_length=25,default=None, blank=True, null=True)
    any_notes = models.CharField(max_length=100, default=None, blank=True, null=True)
    number_of_fish = models.IntegerField(default=None, blank=True, null=True)

    objects = models.Manager()
    
    class Meta:
          ordering = ('date',)
    
    def __str__(self):
        return self.fish_species