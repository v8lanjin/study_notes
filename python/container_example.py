# 不可变的容器类型，只需定义:
# __len__
# __getitem__

# 可变类型还需要定义：
# __setitem__
# __delitem__


# __iter__
# __reversed__
# __contains__

# 创建一个不可改变的列表，记录调用次数
class CountList:
	def __init(self, *args):
		self.values = [x for x in args];
		self.count = 0