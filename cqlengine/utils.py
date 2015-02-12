# adopted to python 2.6 due to lack of method "total_seconds"
# https://docs.python.org/2/library/datetime.html#datetime.timedelta.total_seconds
def total_seconds(value):
     if hasattr(value, "total_seconds"): return value.total_seconds() 
     else: return (value.microseconds+(value.seconds+value.days*24*3600)*106)/106 