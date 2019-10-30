# This is Python 2
import sys

line = sys.stdin.readline()
# print line

# Use a list stand for count of (n,e,i,g,h),
# if saw 'n', set count n increase 1
# if saw other char, for example, 'g',
# need to confirm if 'i' bigger than 1
# if so, it means one of the horses is saying till 'i'
# then the count of 'i' need to decrese 1 and 'g' count increse 1
# If count of 'i' is 0, then the recording has some problem
# in the end, 'h' count should be the number of horses
count = [0] * 5
for ch in line:
  if ch == 'n':
    if count[4] > 0:
      count[4] -= 1
    count[0] += 1
  elif ch == 'e':
    if count[0] == 0:
      print "Invalid"
    count[0] -= 1
    count[1] += 1
  elif ch == 'i':
    if count[1] == 0:
      print "Invalid"
    count[1] -= 1
    count[2] += 1
  elif ch == 'g':
    if count[2] == 0:
      print "Invalid"
    count[2] -= 1
    count[3] += 1
  elif ch == 'h':
    if count[3] == 0:
      print "Invalid"
    count[3] -= 1
    count[4] += 1
print count[4]




# This is Python 2
import sys

line = sys.stdin.readline()
# print line

# Use a stack to help calculating
# scan the line, if current char is number,
# do the calculating of numbers.
# If it's '+' or '*', it means a seperator of
# pushing to stack as well as calculating sign
# In the end, it will be seperate calculated values
# for each part of the line, so just return the sum up value
if not line:
  print 0
stack, num, sign = [], 0, "+"
for i, ch in enumerate(line):
  if ch.isdigit():
    num = num * 10 + ord(ch) - ord("0")
  if (not ch.isdigit() and not ch.isspace()) or i == len(line) - 1:
    if sign == "+":
      stack.append(num)
    elif sign == "*":
      stack.append(stack.pop() * num) 
    sign = ch
    num = 0  
print sum(stack)