# 캘린더 뷰 생성 => 관리하기 편하게 만듬
import calendar
import itertools

from collections import deque
import datetime
from django import forms


class BaseCalendarMixin:
    first_weekday = 0
    week_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def setup_calendar(self):
        """calender.Calender 클래스 기능 이용때문에 인스턴스화한다
        처음 시작이 월요일로 만약 '화요일로 시작하고 싶다'라는 케이스가 존재할 경우 일단 셋업함
        """
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names

class MonthCalendarMixin(BaseCalendarMixin):
    def get_previous_month(self, date):
        # 전달 가져옴
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)

    def get_next_month(self, date):
        # 다음달 가져옴
        if date.month == 12:
            return date.replace(year=date.year+1, month=12, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        # 전달의 전체 날짜를 가져옴
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        # 현재 월을 가져옴
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data

