Implemented the 'Dining philosophers problem'. 

The output from exercise 2a shows that a single fork is picked up by two philosophers at the same time: 

{0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
{0: 0, 1: 0, 2: 1, 3: 0, 4: 0}
{0: 0, 1: 0, 2: 1, 3: 0, 4: 1}
{0: 1, 1: 0, 2: 1, 3: 1, 4: 1}
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
{0: 1, 1: 1, 2: 1, 3: 2, 4: 1}

Fork three was picked up twice! This can't be right!


The output from exercise 2b shows that all philosophers pick up there right fork, and then cant pick up the left one, since every fork is already used:


Thread Thread-5 took fork: 4, next pick up fork: 0
Thread Thread-1 took fork: 0, next pick up fork: 1
{0: 1, 1: 0, 2: 0, 3: 0, 4: 1}
Thread Thread-3 took fork: 2, next pick up fork: 3
Thread Thread-4 took fork: 3, next pick up fork: 4
{0: 1, 1: 0, 2: 1, 3: 1, 4: 1}
Thread Thread-2 took fork: 1, next pick up fork: 2
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}


The critical sections use a sleep (line 67 in a.py & line 50 in b.py), such that the error is triggered more frequently
