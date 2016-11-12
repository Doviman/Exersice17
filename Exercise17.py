# Rewrite time_to_int (from Section 16.4) as a method.
# It is probably not appropriate to rewrite int_to_time as a method;
# what object you would invoke it on?
# I don't think it matters how u write the method as long as the code works.



class Time(object):
    def time_to_int(self):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print time.time_to_int()
