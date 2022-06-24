from datetime import datetime
from gcsa.event import Event , EmailReminder
from gcsa.recurrence import Recurrence, DAILY
from gcsa.google_calendar import GoogleCalendar
import sys

mm=int(sys.argv[1])
dd=int(sys.argv[2])
yyyy=int(sys.argv[3])

calendar = GoogleCalendar()
event = Event(
    'Expiry',
    start=datetime(yyyy, mm, dd),
    #location='Záhřebská 468/21',
    minutes_before_popup_reminder=15
)

calendar.add_event(event)