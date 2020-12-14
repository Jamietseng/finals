debug = True
# 計算總時間權重
weighting_list = []

on_class_utility_list = input().split(',')  # 輸入上課效益(1~5)
credit_list = [int(i) for i in input().split(',')]  # 輸入各科學分數
exam_percentage_list = [int(i) / 100 for i in input().split(',')]  # 考試占比
efficiency_list = input().split(',')  # 各科讀書效率

'''stage 3'''

max_credit = max(credit_list)  # 計算權重
for i in range(len(credit_list)):
    credit_list[i] = credit_list[i] / max_credit
    weighting_list.append(credit_list[i] * exam_percentage_list[i])
    # 權重

def efficiency_calculate(initial_utility, accumulated_minus):  # 計算讀書效率函數
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


for k in range(len(efficiency_list)):
    if efficiency_list[k] == 'A':  # 最低
        initial_utility = 4
        accumulated_minus = 0.04
        utility_A_list = efficiency_calculate(initial_utility, accumulated_minus)

    elif efficiency_list[k] == 'B':  # 低
        initial_utility = 4.5
        accumulated_minus = 0.04
        utility_B_list = efficiency_calculate(initial_utility, accumulated_minus)

    elif efficiency_list[k] == 'C':  # 普通
        initial_utility = 5
        accumulated_minus = 0.03
        utility_C_list = efficiency_calculate(initial_utility, accumulated_minus)

    elif efficiency_list[k] == 'D':  # 高
        initial_utility = 5.5
        accumulated_minus = 0.02
        utility_D_list = efficiency_calculate(initial_utility, accumulated_minus)

    elif efficiency_list[k] == 'E':  # 最高
        initial_utility = 6
        accumulated_minus = 0.02
        utility_E_list = efficiency_calculate(initial_utility, accumulated_minus)

if debug:
    print(utility_B_list)
    
















