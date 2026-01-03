'''This problem gives you exposure to different use cases of if ... elif and else conditional structues.
Part 1 - Only if
Part 2 - if ... else
Part 3 - if ... elif
'''

# part 1 - If pattern
word = "glow"  # str
continuous_tense = True # bool

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word.endswith("ing") :
    base_word = word[:-3]
    print(base_word)
# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here
if continuous_tense:
    future = new_word + "ing"
    print(future)


# part 2 - If else pattern

age = 5 # int
is_member = True # bool

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age>=18:
    age_group = ("adult")
    
else:
    age_group ="Child"
print(age_group)

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if age_group == "Child":
    applicant_type = "Child Non-member"
else:
    applicant_type = "Adult Member"
print(applicant_type)


# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G
color_code = None # str: valid values are R-red, G-green and B-blue

if color_code =="R":
    color = "red"
elif color_code=="B":
        color = "blue"       
elif color_code=="G":
    color = "green"    
else:
    color = "black"    
print(color)

# part 4

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
hour,period = time[0:2] , time[3:len(time)]   #time.split()
hour = int(hour)
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

is_time_valid = (1<=int(time[0:2])<=12) # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 
if is_time_valid:
    True
else:
    False

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = hour+12 if period =="PM" else hour
print(time_in_hrs)
# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range
if period == "AM":
    time_of_day = "Night" if hour == 12 else "Morning" if 6 <= hour <= 11 else "Invalid"
   
else:
    time_of_day = "Afternoon" if hour==12 else "Afternoon" if 1 <= hour <= 4 else "Evening" if 5 <= hour <= 11 else "Invalid"