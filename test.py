def parent(num):
    def first_child(a):
         print("Hi, I am Emma"+a)

    def second_child():
        return "Call me Liam"

    callee(first_child)

    callya()

    if num == 1:
        return first_child
    else:
        return second_child

callcall = None

def callee(callback):
    global callcall
    callcall = callback

def callya():
    callcall("who am I?")

first = parent(1)
# second = parent(2)

print(first)
# print(first())