# __author: "QiuJunan"
# date: 2018/2/24

# 三级菜单
# 1、打印省、市、县三级菜单
# 2、额可以返回上一级
# 3、可以随时退出程序。
# 比较混乱。。。。。

# 先是存储数据
menu = {
	"北京": {
		"朝阳": {
			"国贸": {
				"CICC": {},
				"CCTV": {}
			},
			"望京": {
				"陌陌": {},
				"360": {}
			},
		},
		"昌平": {
			"沙河": {
				"老男孩": {},
				"阿泰包子": {}
			},
			"天通苑": {
				"链家": {},
				"我爱我家": {}
			},
			"回龙观": {}
		}
	},
	"上海": {
		"浦东": {
			"陆家嘴": {
				"CICC": {},
				"高盛": {},
				"摩根": {}
			},
			"外滩": {}
		},
		"静安": {}
	}
}

current_layer = menu
# 上一层，初始值为None
# 实现保存父亲所在层
parent_layer = []

while True:
	for key in current_layer:
		print(key)
	choice = input(">>>[退出:q]").strip()
	if len(choice) == 0:
		continue
	# 	如果存在下一层，就输出下一层
	if choice in current_layer:
		parent_layer.append(current_layer)
		current_layer = current_layer[choice]
	elif choice in ['b','B']:
		if len(parent_layer):
			current_layer = parent_layer.pop()
		else:
			print("已经是顶层")
	elif choice in ['q','Q']:
		break
	else:
		print("无此项")




