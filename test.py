import time


class Test:
    value = 1

    def __init__(self):
        self.value = Test.value
        print(f'{self.value} is now {Test.value}')

    def increase(self):
        self.value += 1
        return self.value


test = Test()  # INITIALIZED value = 1
x = 1
while x < 5:
    time.sleep(1)
    a = test.increase()
    print(a)
    x += 1

print(f'finally class value {Test.value}')
