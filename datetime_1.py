#Импорт модулей
from datetime import datetime, timedelta
from dateutil import relativedelta

dt_now = datetime.now()
dt_now_yesterday = datetime.now() - timedelta(days=1)
dt_now_month = datetime.now() + relativedelta.relativedelta(months=-1)

dt_now = dt_now.strftime('%Y-%m-%d')
dt_now_yesterday = dt_now_yesterday.strftime('%Y-%m-%d')
dt_now_month = dt_now_month.strftime('%Y-%m-%d')
print(f'Сегодня: {dt_now}')
print(f'Вчера: {dt_now_yesterday}')
print(f'Месяц назад: {dt_now_month}')


date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
