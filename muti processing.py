from queue import Queue
import threading
import time

def push(q):
    print('Thread1 Start')
    q.put('Zero')
    q.put('One')
    q.put('Two')
    q.put('Three')
    q.put('Four')
    print('Thread1 End')


def pop(q):
    print('thread2 Start')
    while True:
        test = q.get() #큐의 내용을 얻어옮
        if test:
            time.sleep(1)
            print(test)
    print('Thread2 End')

if __name__ == "__main__":
    queue = Queue() #큐 생성
    thread1 = threading.Thread(target=push, args=(queue, )) #쓰레드 생성 , 함수를 매계변수로 사용할 수도 잇다.
    thread2 = threading.Thread(target=pop, args=(queue, )) #쓰레드 생성
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("main ended")