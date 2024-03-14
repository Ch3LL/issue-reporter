def convert_estimate(time_estimate):
    """
    Utility function to convert estimate to either
    days or hours. 8 hours is considered 1 day.
    If time is less than 8 hours return hours
    """
    hours = time_estimate / 3600
    days = hours / 8
    if days >= 1:
        estimate = f"{days}d"
    else:
        estimate = f"{hours}h"
    return estimate
