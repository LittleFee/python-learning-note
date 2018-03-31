from copy import deepcopy
# copy
dicts={'kiwi':123,'timo':234,'mimi':[12,'kiwi']}
dicts_copy=dicts.copy()
dicts_deep=deepcopy(dicts)
print(dicts_copy)
print(dicts_deep)
dicts_copy['timo']=876
dicts_copy['mimi'].remove(12)
print(dicts_copy)
print(dicts)
print(dicts_deep)
# 如你所见，当替换副本中的值(timo)时，原件不受影响。然而，如果修改副本中的值（就地修改而
# 不是替换），原件也将发生变化，因为原件指向的也是被修改的值（如这个示例中的'mimi'
# 列表所示）。
#
# 为避免这种问题，一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此，
# 可使用模块copy中的函数deepcopy。

