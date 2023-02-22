import random

# 定义多个列表，存储不同类型的赞美语句
adjectives = ["美丽的", "聪明的", "有才华的", "勇敢的", "善良的"]
people = ["你", "他", "她", "我们", "他们"]
verbs = ["做得很好", "非常出色", "很有创意", "非常专业", "非常有天赋"]

# 随机选择一个赞美语句
adjective = random.choice(adjectives)
person = random.choice(people)
verb = random.choice(verbs)

# 输出赞美语句
print(f"{adjective}{person}{verb}！")
