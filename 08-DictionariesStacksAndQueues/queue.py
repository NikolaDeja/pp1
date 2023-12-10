queue=[]

def push(value):
    queue.append(value)

def pop():
    if empty()==False:
        return queue.pop(0)
    else:
        return None

def empty():
    return len(queue)==0

def display():
    for i in queue:
        print(i)