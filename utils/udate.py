from datetime import datetime,timedelta
import time
from collections import namedtuple
datetime_range=namedtuple("datetime_range", ["start","end"])
def get_unix_ts_s() -> int:
    """get the unix timestamp which is accurate to second

    Returns:
        int: seconds from 1970-01-01
    """
    return int(time.time())

def get_unix_ts_ms() -> int:
    """get the unix timestamp which is accurate to milisecond

    Returns:
        int: miliseconds from 1970-01-01
    """
    return int(time.time()*1000)

def get_week_last_day(dt:datetime=None)->datetime:
    """get the last day of the week of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime: last day of the week
    """
    now=dt
    if not now:
        now=datetime.now()
    start=now - timedelta(days=now.weekday())
    end = start + timedelta(days=6)
    end-=timedelta(hours=end.hour, minutes=end.minute, seconds=end.second,microseconds=end.microsecond)
    end+=timedelta(hours=23, minutes=59, seconds=59)
    return end
    
def get_week_first_day(dt:datetime=None)->datetime:
    """get the first day of the week of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime: first day of the week
    """
    now=dt
    if not now:
        now=datetime.now()
    start=now - timedelta(days=now.weekday(),hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)
    start-=timedelta()
    return start

def get_week_last_day_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->str:
    """get the last day of the week of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: datetime str
    """
    _day=get_week_last_day(dt)
    return _day.strftime(fmt)

def get_week_first_day_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->str:
    """get the first day of the week of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: datetime str
    """
    _day=get_week_first_day(dt)
    return _day.strftime(fmt)

def get_month_first_day(dt:datetime=None)->datetime:
    """get the first day of the month of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime: first day of the month
    """
    now=dt
    if not now:
        now=datetime.now()
    start=now - timedelta(days=now.day-1,hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond)
    return start

def get_month_first_day_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->str:
    """get the first day of the month of dt

    Args:
        dt (datetime, optional): datetime object if it is None. Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: datetime str
    """
    _day=get_month_first_day(dt)
    return _day.strftime(fmt)

def get_month_last_day(dt:datetime=None)->datetime:
    """get the last day of the month of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime: last day of the month
    """
    now=dt
    if not now:
        now=datetime.now()
    next_month = now.replace(day=28) + timedelta(days=4)
    end=next_month - timedelta(days=next_month.day,hours=next_month.hour, minutes=next_month.minute, seconds=next_month.second,microseconds=next_month.microsecond)
    end+=timedelta(hours=23, minutes=59, seconds=59)
    return end

def get_month_last_day_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->str:
    """get the last day of the month of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: datetime str
    """
    _day=get_month_last_day(dt)
    return _day.strftime(fmt)

def get_current_day_range(dt:datetime=None)->datetime_range:
    """get current day range

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime_range: start  and  end
    """
    now=dt
    if not now:
        now=datetime.now()
    start=now-timedelta(hours=now.hour,minutes=now.minute, seconds=now.second,microseconds=now.microsecond)
    end=start+timedelta(hours=23, minutes=59, seconds=59)
    return datetime_range(start,end)

def get_current_day_range_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->datetime_range:
    """get current day range str

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        datetime_range: start and end
    """
    start,end=get_current_day_range(dt)
    return datetime_range(start.strftime(fmt),end.strftime(fmt))

def get_year_first_day(dt:datetime=None)->datetime:
    """get the first day of the year of dt 

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime: first day of the year
    """
    now=dt
    if not now:
        now=datetime.now()
    start=datetime(year=now.year,month=1,day=1,hour=0,minute=0,second=0)
    return start

def get_year_last_day(dt:datetime=None)->datetime:
    """get the last day of the year str of dt 

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.

    Returns:
        datetime: last day str  of the year
    """
    now=dt
    if not now:
        now=datetime.now()
    start=datetime(year=now.year,month=12,day=31,hour=23,minute=59,second=59)
    return start

def get_year_first_day_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->str:
    """get the first day of the year of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: datetime str
    """
    _day=get_year_first_day(dt)
    return _day.strftime(fmt)

def get_year_last_day_str(dt:datetime=None,fmt:str="%Y-%m-%d %H:%M:%S")->str:
    """get the last day of the year of dt

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        fmt (_type_, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: datetime str
    """
    _day=get_year_last_day(dt)
    return _day.strftime(fmt)

def unix_ts_to_datetime(unix_ts:float=None,is_second=True)->datetime:
    """unix timestamp to datetime object

    Args:
        unix_ts (float, optional): float like time.time(). Defaults to None.
        is_second (bool, optional): default True if False, unix_ts must be accurate to milisecond. Defaults to True.

    Returns:
        datetime
    """
    if not unix_ts:
        unix_ts=time.time()
    if is_second:
        return datetime.fromtimestamp(unix_ts)
    return datetime.fromtimestamp(unix_ts/1e3)

def unix_ts_to_datetime_str(unix_ts:float=None,is_second=True,fmt="%Y-%m-%d %H:%M:%S")->str:
    """unix timestamp to datetime str

    Args:
        unix_ts (float, optional): float like time.time(). Defaults to None.
        is_second (bool, optional): default True if False, unix_ts must be accurate to milisecond. Defaults to True.
        fmt (str, optional): format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str
    """
    _day=unix_ts_to_datetime(unix_ts,is_second=is_second)
    return _day.strftime(fmt)

def datetime_to_unix_ts(dt:datetime=None,is_second=True)->int:
    """datime object to unix_ts

    Args:
        dt (datetime, optional): datetime object if it is None default datetime.now(). Defaults to None.
        is_second (bool, optional):  default True if False, result should be accurate to milisecond. Defaults to True.

    Returns:
        int: timestamp
    """
    now=dt
    if not now:
        now=datetime.now()
    if is_second:
        return int(now.timestamp())
    return int(now.timestamp()*1000)
