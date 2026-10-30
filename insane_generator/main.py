import random
vocabulary = [
    ["快乐", "愤怒", "绝望", "恐惧", "自由", "失败", "成功", "无助", "劳累", "极度兴奋", "彻底疯狂", "吃饱了撑"],
    ["小明", "老师", "僵尸", "路人", "精神病", "猫", "狗", "外星人", "纸片人", "系统管理员"],
    ["学校", "医院", "商店", "家", "公司", "大街", "厕所", "异次元空间", "赛博坦星", "代码编辑器里"],
    ["吃饭", "睡觉", "学习", "工作", "吃屎", "看片", "排泄", "尖叫", "疯狂敲代码", "背诗", "研究开源协议", "修bug", "闲逛GitHub"]
]
sentence = f"{random.choice(vocabulary[0])}的{random.choice(vocabulary[1])}和{random.choice(vocabulary[0])}的{random.choice(vocabulary[1])}一起在{random.choice(vocabulary[2])}{random.choice(vocabulary[3])}"
print(sentence)
