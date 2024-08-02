def tree(root_label, branches = []):
   # 检查分支是否是树
   for branch in branches:
       assert is_tree(branch), '分支必须是树'
   return [root_label] + branches 

def root_label(tree):
    return tree[0]
    
def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) == 0:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(root_label(t))
print(branches(t))
print(is_leaf(branches(t)[0]))
print(root_label(branches(t)[1]))