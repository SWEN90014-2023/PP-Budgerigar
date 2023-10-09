from django.db import models

class DailyUnlock(models.Model):
    id = models.AutoField(primary_key=True, db_column='_id')
    date = models.DateField()
    total_unlocks = models.IntegerField(default=0)
    unlocks_0_2 = models.IntegerField(default=0, db_column='0_2_unlocks')
    unlocks_3_5 = models.IntegerField(default=0, db_column='3_5_unlocks')
    unlocks_6_8 = models.IntegerField(default=0, db_column='6_8_unlocks')
    unlocks_9_11 = models.IntegerField(default=0, db_column='9_11_unlocks')
    unlocks_12_14 = models.IntegerField(default=0, db_column='12_14_unlocks')
    unlocks_15_17 = models.IntegerField(default=0, db_column='15_17_unlocks')
    unlocks_18_20 = models.IntegerField(default=0, db_column='18_20_unlocks')
    unlocks_21_23 = models.IntegerField(default=0, db_column='21_23_unlocks')

    class Meta:
        db_table = 'daily_unlock'
