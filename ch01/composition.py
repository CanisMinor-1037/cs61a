# 给定函数f(x)和g(x)
# 定义函数h(x) = f(g(x))
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h