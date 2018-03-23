# 8-15 打印模型：将示例print_models.py 中的函数放在另一个名为printing_
# functions.py 的文件中；在print_models.py 的开头编写一条import 语句，并修改这个文
# 件以使用导入的函数。
import printing_functions as pf

unprinted_designs=['people','republic','of','china']
completed_models=[]
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
print(unprinted_designs)
