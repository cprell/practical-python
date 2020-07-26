# bounce.py
#
# Exercise 1.5

height = 100
num_bounces = 0

while num_bounces < 10:
    height = height * 0.6
    num_bounces = num_bounces + 1
    print(num_bounces, round(height, 4))
