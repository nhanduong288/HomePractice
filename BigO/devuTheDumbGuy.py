'''
Devu is a dumb guy, his learning curve is very slow.
You are supposed to teach him n subjects, the i-th subject has c[i] chapters,
    when you teach him, you are supposed to teach all the chapters continuously.

His initial per chapter learning power of a subject is x hours.

If you teach him a subject, then time required to teach any chapter of the next subject
    will require exactly 1 hour less than previously required.
    Note that his perchapter learning power cannot be less than 1 hour

You can teach him the n subjects in any possible order.

Find out minimum amount of time (in hours) Devu will take to understand all the subjects.
'''

# subjects, initial learning power
n, x = list(map(int, input().split()))
# number of chapters
chapters = list(map(int, input().split()))

# to save time, learn the ones with less chapters first
chapters.sort()
result = 0

for chapter in chapters:
    result += chapter * x
    # x cannot be less than 1
    if x > 1:
        x -= 1

print(result)