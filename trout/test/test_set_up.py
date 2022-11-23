from datetime import timezone
from rest_framework.test import APITestCase
from trout.models import FishingLogEntry

class ModelTest(APITestCase):
    # test to create fishing entry instance:
    # force authentication?
    def creates_fishinglogentry(self):
        fish = FishingLogEntry.objects.create(user='y3FE5buvuPTWUFIYOosI45IYEVp1',date=timezone.now,river='Tongariro',
            river_pool='bridge',lat=-38.993070,lon=175.818593,fish_species='Rainbow',fish_weight='5',fish_condition='Spent',fly_used='fish egg'
            any_notes='sunny day', )
    def test_create_fish_entry_returns_fish_species(self):
        fish_entry = FishingLogEntry.objects.get(user='y3FE5buvuPTWUFIYOosI45IYEVp1')
        self.assertEqual(fish_entry.__str__)