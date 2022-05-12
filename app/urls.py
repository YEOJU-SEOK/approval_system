from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),

    path('week/', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>', views.WeekCalendar.as_view(), name='week'),

    path('week_sch/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
    path('week_sch/<int:year>/<int:month>/<int:day>', views.WeekWithScheduleCalendar.as_view(),
         name='week_with_schedule'),

    path('month_sch/', views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_sch/<int:year>/<int:month>/', views.MonthWithScheduleCalendar.as_view(),
         name='month_with_schedule'),

    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path('mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'),

]