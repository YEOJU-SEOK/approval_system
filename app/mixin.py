# 캘린더 뷰 생성 => 관리하기 편하게 만듬
import calendar
import datetime
import itertools

from collections import deque
from django import forms


class BaseCalenderMixin:
    first_weekday = 0
    week_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def setup_calender(self):
        """calender.Calender 클래스 기능 이용때문에 인스턴스화한다
        처음 시작이 월요일로 만약 '화요일로 시작하고 싶다'라는 케이스가 존재할 경우 일단 셋업함
        """
        self._calendar = calendar.Calendar

    def get_week_name(self):
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names
