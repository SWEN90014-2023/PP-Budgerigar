from django.db import models

class DailyUnlock(models.Model):
    date = models.DateField()
    device_id = models.CharField(max_length=150,default=0)
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
        unique_together = (('date', 'device_id'),) 

class DailyDuration(models.Model):
    date = models.DateField()
    device_id = models.CharField(max_length=150,default=0)
    total_duration = models.FloatField(default=0.0)
    duration_0_2 = models.FloatField(default=0.0, db_column='0_2_duration')
    duration_3_5 = models.FloatField(default=0.0, db_column='3_5_duration')
    duration_6_8 = models.FloatField(default=0.0, db_column='6_8_duration')
    duration_9_11 = models.FloatField(default=0.0, db_column='9_11_duration')
    duration_12_14 = models.FloatField(default=0.0, db_column='12_14_duration')
    duration_15_17 = models.FloatField(default=0.0, db_column='15_17_duration')
    duration_18_20 = models.FloatField(default=0.0, db_column='18_20_duration')
    duration_21_23 = models.FloatField(default=0.0, db_column='21_23_duration')

    class Meta:
        db_table = 'daily_durations'
        unique_together = (('date', 'device_id'),)