k = int(input())


def counter_add(k):
    def add_5():
        return k + 5
    return add_5


cnt = counter_add(k)
print(cnt())

