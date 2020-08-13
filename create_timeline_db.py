from reto_sqllite import sqllite_operator, sqllite_selector
import arrow
from tqdm import tqdm

ubtime = arrow.get('2020-08-13 09:00:00', 'YYYY-MM-DD HH:mm:ss', tzinfo='local')
for i in tqdm(range(99999)):
    ctime = ubtime.shift(hours=0.5 * i)
    if ctime.hour < 9:
        continue
    if ctime.hour > 18:
        continue
    if ctime.hour == 18 and ctime.minute > 0:
        continue
    ctime = ctime.format('YYYY-MM-DD HH:mm:ss')
    sqllite_operator('insert into basic_timeline(half_hour_time) values (?)', [ctime])
