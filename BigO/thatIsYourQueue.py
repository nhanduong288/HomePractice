'''
Your government has finally solved the problem of universal health care!
There is one minor complication. All of the country's hospitals have been condensed
    down into one location, which can only take care of one person at a time.
There is a plan in place for a fair, efficient computerized to determine who will be admitted.

Every citizen in the nation will be assigned a UNIQUE number, from 1 to P 
    (P is the current population).
They will be put into a queue, with 1 in from of 2, 2 in front of 3, and so on.
The hospital will process patients one by one, in order, from this queue.
Once a citizen has been admitted, they will immediately move from the front of the queue
    to the back.
Of course, sometimes emergencies arise; if you've just been run over by a steamroller,
    you can't wait for half of the country to get a routine checkup before you can be treated!
So, for these occasions, an exedite command can be given to move one person to the 
    front of the queue. Everyone else's relative order will remain unchanged.

Given the sequence of processing and expediting commands, output the order in which
    citizens will be admitted to the hospital.    
'''

import queue

# population of the country and the number of commands to process
P, C = list(map(int, input().split()))

while P != 0 and C != 0:
