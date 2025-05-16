# Similar to the previous exercise, write a function that extracts the region code from a locale. For example:

# my solution
import re
def extract_region(locale):    
    separators = r'[_.]'
    return re.split(separators, locale)[1]  # can also do return locale[3:5]
# end of my solution

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR