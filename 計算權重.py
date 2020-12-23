debug = True

# 計算總時間權重
weighting_list = []

# 科目
subject_list = input().split(',')

# 上課效益(1~5)
on_class_utility_list = [int(s) for s in input().split(',')]

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

# 上課堂數
class_number = [int(s) for s in input().split(',')]

# 絕對不翹的課
never_skip_class = [int(s) for s in input().split(',')]

# 計算權重
max_credit = max(credit_list)
for i in range(len(credit_list)):
    credit_list[i] = credit_list[i] / max_credit
    weighting_list.append(credit_list[i] * exam_percentage_list[i])



'''stage 2'''

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


# 計算讀書效率及效益的函數
def efficiency_to_utility(efficiency):
    if efficiency == 'A':  # 最低
        self_studying_utility_list = efficiency_calculate(4, 0.04)

    elif efficiency == 'B':  # 低
        self_studying_utility_list = efficiency_calculate(4.5, 0.04)

    elif efficiency == 'C':  # 普通
        self_studying_utility_list = efficiency_calculate(5, 0.03)

    elif efficiency == 'D':  # 高
        self_studying_utility_list = efficiency_calculate(5.5, 0.02)

    elif efficiency == 'E':  # 最高
        self_studying_utility_list = efficiency_calculate(6, 0.02)

    return(self_studying_utility_list)



'''stage 3'''

class Subject:  # 定義subject這個type，包含上課效益、學分數、考試占比、效率、權重
    def __init__(self, on_class_utility, credit, exam_percentage, efficiency, weighting):
        self.on_class_utility = on_class_utility
        self.credit = credit
        self.efficiency = efficiency
        self.exam_percentage = exam_percentage
        self.weighting = weighting

class_subject_list = subject_list.copy()

# 將每堂課的資料丟到class_subject_list裡面
for i in range(len(class_subject_list)):
    class_subject_list[i] = Subject(on_class_utility=on_class_utility_list[i],
                                    credit=credit_list[i],
                                    exam_percentage=exam_percentage_list[i],
                                    efficiency=efficiency_list[i],
                                    weighting=weighting_list[i],)


self_studying_utility_dict = dict()
# key = subject, value = self_stydying_utility_list (each hour)

self_studying_time_dict = dict()
# key = subject, value = how much time to study that subject

for i in range(len(subject_list)):
    self_studying_utility_dict[subject_list[i]] = efficiency_to_utility(efficiency_list[i])


each_final_utility_list = []  # 記錄每科的最後效益
final_utility_list = []  # 紀錄全部的最後效益

for i in range(len(efficiency_list)):
    for j in efficiency_to_utility(efficiency_list[i]):
        j *= weighting_list[i]
        each_final_utility_list.append('{:+.5f}'.format(j))  # 記到小數點後五位
    final_utility_list.append([float(i) for i in each_final_utility_list])
    each_final_utility_list = []


temp_list = []  # temporary list
# weighting * on_class_utility
selected_hour_utility_list = [[] for i in range(len(subject_list))]

for i in range(total_time):  # 計算各科總共要上多少時間
    for j in range(len(final_utility_list)):
        temp_list.append(final_utility_list[j][0])  # 抓每科邊際效益最高者
    

    for k in range(len(final_utility_list)):
        if  final_utility_list[k][0] == max(temp_list):  # 紀錄邊際效益最高者
            if subject_list[k] in self_studying_time_dict:
                self_studying_time_dict[subject_list[k]] += 1
            else:
                self_studying_time_dict[subject_list[k]] = 1

            selected_hour_utility_list[k].append(final_utility_list[k][0])
            final_utility_list[k].pop(0)
            temp_list.clear()
            break


'''stage 4'''

for i in range(len(on_class_utility_list)):
    on_class_utility_list[i] *= weighting_list[i] 
# 上課效益＊權重

potential_class_list = []  # 可能會去上的各科堂數
for i in range(len(class_number)):
    potential_class_list.append(class_number[i] - never_skip_class[i]) 

on_class_utility_order_list = []  # 上課效益的大小順序
for i in range(len(on_class_utility_list)):
    order = on_class_utility_list.index(sorted(on_class_utility_list, reverse = True)[i])
    on_class_utility_order_list.append(order)
    order = 0


selected_hour_utility_list_cp = selected_hour_utility_list.copy()  # 複製一下不要動到原本的
temp_min_list = []  # 存邊際效益最小的暫時list
going_class_dict = dict()  # 存哪幾門課要上幾堂課的dict
minimum = 1000
minimum_place = 0
for i in on_class_utility_order_list:  # 開始計算
    if potential_class_list[i] == 0:  # 如果那一門課全部都要上就跳過
        continue
    
    for j in range(potential_class_list[i]):  # 那一門課的扣打
        for k in range(len(selected_hour_utility_list_cp)):  # 抓讀每門課最小的邊際效益
            temp_min_list.append(selected_hour_utility_list_cp[k][-1])
        
        for k in range(len(temp_min_list)):  # 找裡面的最小值跟他是哪一門課
            if temp_min_list[k] < minimum:
                minimum = temp_min_list[k]
                minimum_place = k
        
        if on_class_utility_list[i] >= minimum:  # 如果上課效益比較大就去上課
            if subject_list[i] not in going_class_dict:
                going_class_dict[subject_list[i]] = 1
            else:
                going_class_dict[subject_list[i]] += 1
            
            selected_hour_utility_list_cp[minimum_place].pop(-1)
            temp_min_list = []
            minimum = 1000
            minimum_place = 0

going_class_list = []  # 存每門課要再去上多少堂
for i in range(len(subject_list)):  # 把剛剛的dict丟進來
    if subject_list[i] not in going_class_dict:
        going_class_list.append(0)
    else:
        going_class_list.append(going_class_dict[subject_list[i]])

for i in range(len(subject_list)):
    if subject_list[i] in going_class_dict:
        less = going_class_dict[subject_list[i]]
        self_studying_time_dict[subject_list[i]] -= less
    less = 0

print(self_studying_time_dict)



