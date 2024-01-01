
# * decorator 練習
def new_decorator(original_func):
    def wrap_func():
        print("在 original function 之前的 some codes")
        original_func()
        print("在 original function 之後的 some codes")
    return wrap_func


@new_decorator
def func_needs_decorator():
    print("這是function ，而且也需要 decorators")


func_needs_decorator()

# * generator 練習


def sub_generator(x):
    for i in range(x):
        yield i**2


def gen(y):
    yield from sub_generator(y)
    # & yield from 後面接 generator


for num in gen(15):
    print(num)
