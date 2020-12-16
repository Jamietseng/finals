debug = True

# 計算總時間權重
weighting_list = []

# 科目
subject_list = input().split(',')

# 上課效益(1~5)
on_class_utility_list = input().split(',')

# 各科學分數
credit_list = [int(i) for i in input().split(',')]

# 考試占比
exam_percentage_list = [int(i) / 100 for i in input().split(',')]

# 各科讀書效率
efficiency_list = input().split(',')

# type 為 Subject
class_subject_list = []

# 上課＋讀書＝一週總時間（不包含絕不能翹的課）
total_time = int(input())


# 計算權重
max_credit = max(credit_list)
for i in range(len(credit_list)):
    credit_list[i] = credit_list[i] / max_credit
    weighting_list.append(credit_list[i] * exam_percentage_list[i])


# 計算讀書效率函數
def efficiency_calculate(initial_utility, accumulated_minus):
    utility_list = []
    utility_list.append(initial_utility)  # 初始值
    utility_list.append(initial_utility - 0.1)  # 第一個遞減
    previous_utility = initial_utility - 0.1
    previous_minus = 0.1

    for i in range(169):  # 遞減
        previous_minus += accumulated_minus
        temp = '{:+.2f}'.format(previous_utility - previous_minus)
        utility_list.append(float(temp))
        previous_utility -= previous_minus

    return(utility_list)


def efficiency_to_utility(efficiency):
    if efficiency == 'A':  # 最低
        self_stydying_utility_list = efficiency_calculate(4, 0.04)

    elif efficiency == 'B':  # 低
        self_stydying_utility_list = efficiency_calculate(4.5, 0.04)

    elif efficiency == 'C':  # 普通
        self_stydying_utility_list = efficiency_calculate(5, 0.03)

    elif efficiency == 'D':  # 高
        self_stydying_utility_list = efficiency_calculate(5.5, 0.02)

    elif efficiency == 'E':  # 最高
        self_stydying_utility_list = efficiency_calculate(6, 0.02)

    return(self_stydying_utility_list)


class Subject:  # 定義subject這個type，包含上課效益、學分數、考試占比、效率、權重
    def __init__(self, on_class_utility, credit, exam_percentage, efficiency, weighting):
        self.on_class_utility = on_class_utility
        self.credit = credit
        self.efficiency = efficiency
        self.exam_percentage = exam_percentage
        self.weighting = weighting

class_subject_list = subject_list.copy()

for i in range(len(class_subject_list)):
    class_subject_list[i] = Subject(self=class_subject_list[i],
                                    on_class_utility=on_class_utility_list[i],
                                    credit=credit_list[i],
                                    exam_percentage=exam_percentage_list[i],
                                    efficiency=efficiency_list[i],
                                    weighting=weighting_list[i],)


self_stydying_utility_dict = dict()
# key = subject, value = self_stydying_utility_list (each hour)

self_stydying_time_dict = dict()
# key = subject, value = how much time to study that subject

for i in range(len(subject_list)):
    self_stydying_utility_dict[subject_list[i]] = efficiency_to_utility(efficiency_list[i])


for i in range(total_time):
    for k in range(len(class_subject_list)):
        if class_subject_list[k].























