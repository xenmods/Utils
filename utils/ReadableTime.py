from datetime import timedelta

def get_readable_time(seconds: int) -> str:
    """
    Returns approximate readable time.
    Smart if time is only in seconds. Might not be very accurate
    but does the job.
    Example: 
    - 6 day(s) ago.
    - 4 month(s) ago.
    
    :param seconds: Time in seconds.
    :return: Time in human-readable format.
    """
    days, seconds = divmod(seconds, 24*3600)
    months, days = divmod(days, 30)
    years, months = divmod(months, 12)
    if years:
        return f"{round(years)} year(s)"
    elif months:
        return f"{round(months)} month(s)"
    elif days:
        return f"{round(days)} day(s)"
    else:
        time = list(map(int, str(timedelta(seconds=round(seconds))).split(':')))
        final = ""
        index = 0
        for part in time:
            if part == 0:
                index += 1
            elif index == 0:
                final = f"{round(time[index])} hour(s)"
                break
            elif index == 1:
                final = f"{round(time[index])} minute(s)"
                break
            else:
                final = f"{round(time[index])} second(s)"
                break
        return final