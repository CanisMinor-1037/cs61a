empty = 'empty'

def link(first, rest):
    assert is_link(rest), "rest必须是一个链表"
    return [first, rest]

def first(link):
    assert is_link(link), "first只能用于链表"
    assert link != empty, "空链表没有第一个元素"
    return link[0]

def rest(link):
    assert is_link(link), "rest只能用于链表"
    assert link != empty, "空链表没有剩余元素"
    return link[1]

def is_link(link):
    if link == empty:
        return True
    if type(link) != list or len(link) != 2:
        return False
    if is_link(link[1]):
        return True
    
l = link(1, link(2, link(3, link(4, empty))))
print(first(l))
print(rest(l))
print(first(rest(l)))
print(first(rest(rest(l))))

def len_link(link):
    if link == empty:
        return 0
    else:
        return 1 + len_link(rest(link))
    
def getitem_link(link, i):
    while i > 0:
        link, i = rest(link), i - 1
    return first(link)
    
print(len_link(l))
print(getitem_link(l, 0))
print(getitem_link(l, 3))

