# minutes in 7 weeks
print 7 * 7 * 24 * 60

# speed of light in CM in one nanosecond
print 299792458 * 100 * (1.0 / 1000000000)

# -//- with variables
speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
distance = speed_of_light / cycles_per_second
print distance

# age in days
age = 18
age = age * 365
print age

# string
name = "Georg"

# print Udacity
s = 'audacity'
print "U" + s[2:8]

# find beginning of the link
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find("<a href=")

# find full link
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1:end_quote]

# distance in meters that light travels in one nanosecond
speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000.
nanodistance = speed_of_light / nano_per_sec

print nanodistance

# print out udacious
s = 'udacity'
t = 'bodacious'

print s[0:3] + t[4:]

# find hoo
text = "first hoo"

print text.find("hoo")

# find second zip
text = "all zip files are zipped"

print text.find("zip", text.find("zip") + 1)

# print out nearest whole number
x = 3.14159
x = x + .5

print str(x)[:str(x).find(".")]

# text replacement
# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

replaced = line[:line.find(marker)] + replacement + line[line.find(marker) + len(marker):]

print replaced

# palindrome 
word = "madam"
 
is_palindrome = word.find(word[::-1])

print is_palindrome
