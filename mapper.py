__author__ = 'madevelasco'

import sys
import calendar
import datetime
import locale

def es_zona(id):
    if (id<=50000):
        if(id % 100<=50):
            return 'SW'
        else:
            return 'SE'
    else:
        if (id % 100 <= 50):
            return 'NW'
        else:
            return 'NE'

def es_dia_laborable(tiempo_ms):
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    tiempo_ms = tiempo_ms / 1000.0
    diasLaborables = ['monday', 'tuesday', 'wednesday', 'thursday']
    dateFormat = datetime.datetime.fromtimestamp(tiempo_ms)
    day_name = calendar.day_name[dateFormat.weekday()]
    day_name = day_name.lower()
    if day_name in diasLaborables:
        return True

for line in sys.stdin:
    line.strip()
    columns = line.split('\t')
    call_out = columns[6]
    call_out = call_out.strip()
    if call_out != '':
        grid_zone = columns[0]
        country_code = columns[2]
        time_interval = columns[1]
        if country_code != '' and time_interval != '':
            time_interval = int(time_interval)
            if es_dia_laborable(time_interval):
                print '%s\t%s' % (country_code,es_zona(grid_zone), 1)