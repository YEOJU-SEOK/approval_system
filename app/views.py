from django.shortcuts import render
from django.views import generic
from . import mixin

# Create your views here.


class MonthCalendar(mixin.MonthCalendarMixin, generic.TemplateView):
    template_name = 'app/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class WeekCalendar(mixin.WeekCalendarMixin, generic.TemplateView):
    template_name = 'app/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context
