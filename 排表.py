first_day_list = input().split(',')
second_day_list = input().split(',')
third_day_list = input().split(',')
fourth_day_list = input().split(',')
fifth_day_list = input().split(',')
sixth_day_list = input().split(',')
seven_day_list = input().split(',')
week_list = [first_day_list, second_day_list,third_day_list, fourth_day_list, fifth_day_list, sixth_day_list, seven_day_list]

subject_list = ['經原','西文','微積分','體育','會計','民概']  # 另一個檔案的輸入，要改
self_studying_time_dict = dict()
self_studying_time_dict['經原'] = 16
self_studying_time_dict['西文'] = 15
self_studying_time_dict['微積分'] = 15
self_studying_time_dict['體育'] = 11
self_studying_time_dict['會計'] = 13
self_studying_time_dict['民概'] = 16

def fill_in_missing_class(day_list, subject_list, self_studying_time_dict):  # 補一堂課的情況
    for i in range(len(subject_list)):
        if subject_list[i] not in day_list:
            continue
        place = -1
        for j in range(day_list.count(subject_list[i])):
            place = day_list.index(subject_list[i], place + 1)
            if place > 0:
                if (day_list[place - 1] != subject_list[i] )and (day_list[place + 1] != subject_list[i]):
                    temp_place = place - 1
                    before_place = 0
                    while True:  # 找那堂課前面空多少時間
                        if day_list[temp_place] == '0':
                            before_place += 1
                            temp_place -= 1
                            if temp_place == -1:
                                break
                        else:
                            break
                    temp_place = place + 1
                    after_place = 0
                    while True:  # 找那堂課後面空多少時間
                        if day_list[temp_place] == '0':
                            after_place += 1
                            temp_place += 1
                            if temp_place > len(day_list) - 1:
                                break
                        else:
                            break
                    if before_place > 0 or after_place > 0:  # 選擇要補哪裡(補奇數！)
                        if before_place%2 == 0:
                            if after_place%2 != 0:
                                day_list[place + 1] = subject_list[i]
                                self_studying_time_dict[subject_list[i]] -= 1
                            else:
                                if before_place <= after_place:
                                    day_list[place - 1] = subject_list[i]
                                    day_list[place - 2] = subject_list[i]
                                    self_studying_time_dict[subject_list[i]] -= 2
                                else:
                                    day_list[place + 1] = subject_list[i]
                                    day_list[place + 2] = subject_list[i]
                                    self_studying_time_dict[subject_list[i]] -= 2
                        else:
                            if after_place%2 != 0:
                                day_list[place + 1] = subject_list[i]
                                day_list[place - 1] = subject_list[i]
                                self_studying_time_dict[subject_list[i]] -= 2
                            else:
                                day_list[place - 1] = subject_list[i]
                                self_studying_time_dict[subject_list[i]] -= 1
    return day_list

for i in range(7):
    day_list = week_list[i]
    week_list[i] = fill_in_missing_class(day_list, subject_list, self_studying_time_dict)

def finishing_table(day_list, self_studying_time_dict):
    place = 0
    temp_place_list = []
    for i in range(len(day_list)):
        if day_list[i] == '0':
            place += 1
            temp_place_list.append(i)
        else:
            break
    return (place, temp_place_list)


day_list = week_list[0]
while '0' in day_list:
    if day_list.count('0') == 1:
        break
    change, place_list = finishing_table(day_list, self_studying_time_dict)

    subject_list_copy = []
    for i in range(len(subject_list)):
        if subject_list[i] not in day_list:
            subject_list_copy.append(subject_list[i])

    subject_to_study_list = []
    for i in subject_list_copy:
        subject_to_study_list.append(i)

    number = change // 2
    for i in range(number):
        print('i', i)
        day_list[place_list[0]] = subject_to_study_list[-1]
        day_list[place_list[1]] = subject_to_study_list[-1]
        subject_to_study_list.pop()
        place_list.pop(0)
        place_list.pop(0)
    change = 0
    number = 0

if '0' in day_list:
    day_list[day_list.index('0')] = day_list[day_list.index('0') - 1]

print(day_list)













