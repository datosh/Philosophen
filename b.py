#!python3
import time
import threading
from random import uniform


lock = threading.Lock()
dict_lock = threading.Lock()
print_lock = threading.Lock()


def addToDict(id, num, numTaken):
    '''This function is used to keep the dictionary access synchronized.'''
    with dict_lock:
        numTaken[id] += num


class Philosoph(object):

    """Implements an eating philosoph"""

    def __init__(self, left, right, numTaken):
        super(Philosoph, self).__init__()
        self.left_fork = left
        self.right_fork = right
        self.numTaken = numTaken

    def run(self):
        while(True):
            # Sleep between 0 and 1 seconds
            time.sleep(uniform(0, 1))

            self.takeFork()

            time.sleep(uniform(0, 1))

            self.putbackFork()

    def takeFork(self):
        self.left_fork.take()
        addToDict(self.left_fork.id, 1, self.numTaken)
        print('Thread {} took fork: {}, next pick up fork: {}'.format(
            threading.current_thread().name,
            self.left_fork.id,
            self.right_fork.id))

        # Add this sleep so the critical error shows up more frequently
        # If the OS interrupts every thread at this position, each has its
        # left fork, but no-one can pick up the right
        time.sleep(1)

        self.right_fork.take()
        addToDict(self.right_fork.id, 1, self.numTaken)

        print('Thread {} took fork: {}'.format(
            threading.current_thread().name,
            self.right_fork.id))

    def putbackFork(self):
        print(
            'Putting back: ',
            threading.current_thread().name,
            self.left_fork.id,
            self.right_fork.id)

        self.left_fork.putback()
        addToDict(self.left_fork.id, -1, self.numTaken)

        time.sleep(1)

        self.right_fork.putback()
        addToDict(self.right_fork.id, -1, self.numTaken)


class Fork(object):

    """Implements a fork for eating"""

    def __init__(self, id):
        super(Fork, self).__init__()
        self.available = True
        self.id = id

    def take(self):
        with lock:
            while(not self.available):
                time.sleep(0)  # equivalent to Thread.yield()

            # With synchronized take and putpack methods, this no longer
            # the critical section

            self.available = False

    def putback(self):
        with lock:
            self.available = True


def main():
    # Create a list of all the forks used by the philosophers
    forks = [Fork(i) for i in range(5)]

    # Keep a dictionary of how many forks are currently used
    numTaken = {x: 0 for x in range(5)}

    # Lists for the philosophers and threads. Maybe they are needed later?
    philosophs = []
    threads = []

    # Create the philosophers and start each of them in it's own thread
    for i in range(5):
        p = Philosoph(forks[i % 5], forks[(i + 1) % 5], numTaken)
        philosophs.append(p)
        t = threading.Thread(target=p.run)
        threads.append(t)
        t.daemon = True
        t.start()

    # Keep printing the amount of used forks
    while(True):
        time.sleep(.2)
        print(numTaken)

if __name__ == '__main__':
    main()
