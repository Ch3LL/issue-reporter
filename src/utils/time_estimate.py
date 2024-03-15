def convert_estimate(time_estimate):
    """
    Utility function to convert estimate to either
    days or hours. 8 hours is considered 1 day.
    If time is less than 8 hours return hours
    """
    hours = int(time_estimate / 3600)
    days = int(hours / 8)
    if days >= 1:
        estimate = f"{days}D"
    else:
        estimate = f"{hours}H"
    return estimate
