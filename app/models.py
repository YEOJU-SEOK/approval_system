import datetime
from django.db import models
from django.utils import timezone


class Schedule(models.Model):
    summary = models.CharField('요약', max_length=50)
    description = models.TextField('상세설명', blank=True)
    start_time = models.TimeField('시작시간', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('완료시간', default=datetime.time(7, 0, 0))
    date = models.DateField('일자')
    created_at = models.DateTimeField('작성일', default=timezone.now)

    def __str__(self):
        return self.summary
