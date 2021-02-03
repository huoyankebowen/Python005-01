import threading
import time
import queue

class Philosopher(threading.Thread):
    def __init__(self,philosopherid,leftfork,rightfork,actionQueue,count):
        super(Philosopher, self).__init__()
        self.philosopherid=philosopherid
        self.leftfork=leftfork
        self.rightfork=rightfork
        self.actionQueue=actionQueue
        self.count=count

    def eat(self):        
        self.actionQueue.put([self.philosopherid, 0, 3])
        time.sleep(1)

    def think(self):
        time.sleep(2)

    def run(self):
        num=0
        while True:
            leftpick=self.leftfork.acquire(blocking=False)
            rightpick=self.rightfork.acquire(blocking=False)
            if leftpick and rightpick :
                self.actionQueue.put([self.philosopherid, 1, 1])
                self.actionQueue.put([self.philosopherid, 2, 1])
                self.eat()
                num+=1
                self.leftfork.release()
                self.actionQueue.put([self.philosopherid, 1, 2])
                self.rightfork.release()
                self.actionQueue.put([self.philosopherid, 2, 2])
            elif leftpick and not rightpick:
                self.leftfork.release()
            elif rightpick and not leftpick:
                self.rightfork.release()
            else:
                self.think()

            if num==self.count:
                break



if __name__ == '__main__':
    fork1 = threading.Lock()
    fork2 = threading.Lock()
    fork3 = threading.Lock()
    fork4 = threading.Lock()
    fork5 = threading.Lock()

    actionQueue = queue.Queue()

    count=2


    philosopher1 = Philosopher(1, fork1, fork2, actionQueue, count)
    philosopher2 = Philosopher(2, fork2, fork3, actionQueue, count)
    philosopher3 = Philosopher(3, fork3, fork4, actionQueue, count)
    philosopher4 = Philosopher(4, fork4, fork5, actionQueue, count)
    philosopher5 = Philosopher(5, fork5, fork1, actionQueue, count)
    philosopher1.start()    
    philosopher2.start()    
    philosopher3.start()    
    philosopher4.start()    
    philosopher5.start()
    philosopher1.join()
    philosopher2.join()
    philosopher3.join()
    philosopher4.join()
    philosopher5.join()

    while not actionQueue.empty():
        print(actionQueue.get())


