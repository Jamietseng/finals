first_day_list = input().split(',')
second_day_list = input().split(',')
third_day_list = input().split(',')
fourth_day_list = input().split(',')
fifth_day_list = input().split(',')
sixth_day_list = input().split(',')
seven_day_list = input().split(',')
week_list = [first_day_list, second_day_list, third_day_list, fourth_day_list, fifth_day_list, sixth_day_list, seven_day_list]

final_week_list = []
subject_list = ['經原','西文','微積分','體育','會計','民概']  # 另一個檔案的輸入，要改
self_studying_time_dict = dict()
self_studying_time_dict['經原'] = 18
self_studying_time_dict['西文'] = 10
self_studying_time_dict['微積分'] = 16
self_studying_time_dict['體育'] = 0
self_studying_time_dict['會計'] = 13
self_studying_time_dict['民概'] = 13


def fill_in_missing_class(day_list, subject_list, self_studying_time_dict):  # 補一堂課的情況
    for i in range(len(subject_list)):
        if subject_list[i] not in day_list:
            continue
        place = -1
        for j in range(day_list.count(subject_list[i])):
            place = day_list.index(subject_list[i], place + 1)
            if place > 0:
                if (day_list[place - 1] != subject_list[i]) and (day_list[place + 1] != subject_list[i]):
                    temp_place = place - 1
                    before_place = 0
                    while True:  # 找那堂課前面空多少時間
                        if day_list[temp_place] == '3':
                            before_place += 1
                            temp_place -= 1
                            if temp_place == -1:
                                break
                        else:
                            break
                    temp_place = place + 1
                    after_place = 0
                    while True:  # 找那堂課後面空多少時間
                        if day_list[temp_place] == '3':
                            after_place += 1
                            temp_place += 1
                            if temp_place > len(day_list) - 1:
                                break
                        else:
                            break
                    if before_place > 0 or after_place > 0:  # 選擇要補哪裡
                        if before_place%2 == 0:
                            if after_place%2 != 0:  # 前偶後奇-補後面1堂
                                day_list[place + 1] = subject_list[i]    
                                self_studying_time_dict[subject_list[i]] -= 1
                            else:  # 前偶後偶
                                if before_place <= after_place:  # 前空堂<=後空堂-補後2堂
                                    day_list[place + 1] = subject_list[i]
                                    day_list[place + 2] = subject_list[i]
                                    self_studying_time_dict[subject_list[i]] -= 2
                                else: # 前空堂>後空堂-補前2堂
                                    day_list[place - 1] = subject_list[i]
                                    day_list[place - 2] = subject_list[i]
                                    self_studying_time_dict[subject_list[i]] -= 2
                        else:
                            if after_place%2 != 0:  # 前奇後奇 -前後各補1堂
                                day_list[place + 1] = subject_list[i]
                                day_list[place - 1] = subject_list[i]
                                self_studying_time_dict[subject_list[i]] -= 2
                            else:  # 前奇後偶-補前1堂
                                day_list[place - 1] = subject_list[i]
                                self_studying_time_dict[subject_list[i]] -= 1
    return day_list

for i in range(7):
    day_list = week_list[i]
    week_list[i] = fill_in_missing_class(day_list, subject_list, self_studying_time_dict)


def finishing_table(day_list, self_studying_time_dict):  #找一個間格有多少空堂
    place = day_list.index('3')  # 第一個'3'出現的位置
    at_place = 0  # 總共有多少個3
    temp_place_list = []  # 那一串3的位置順序
    for i in range(place, len(day_list)):
        if day_list[i] == '3':
            at_place += 1
            temp_place_list.append(i)
        else:
            break
    return (at_place, temp_place_list)


# main
self_studying_time_list = []
def subject_list_sort(subject_list, self_studying_time_dict, self_studying_time_list):
    self_studying_time_list = []
    for i in range(len(subject_list)):  # 把dict轉成list
        self_studying_time_list.append([subject_list[i], self_studying_time_dict[subject_list[i]]])
    self_studying_time_list.sort(key=lambda x: x[1])
    subject_list.clear()

    for i in self_studying_time_list:
        subject_list.append(i[0])
    return subject_list

print(self_studying_time_dict)
for i in range(7):  # 7天填空
    day_list = week_list[i]
    subject_list = subject_list_sort(subject_list, self_studying_time_dict, self_studying_time_list)
    while '3' in day_list:
        if day_list.count('3') == 0:
            break
        
        elif day_list.count('3') == len(day_list):  #  如果是周末都沒課的話，暫時先不處理
            subject_to_study_list = []
            for i in range(len(subject_list)):  # 如果當天有上課，就不讀那一科
                subject_to_study_list.append(subject_list[i])

            while True:
                if day_list.count('3') == 0:
                    break
                change, place_list = finishing_table(day_list, self_studying_time_dict)
                #change % 2 == 0
                number = change // 2
                for i in range(number):  # 一組一組換掉
                    if subject_to_study_list == []:
                        for n in range(len(subject_list)):
                            subject_to_study_list.append(subject_list[n])

                    if self_studying_time_dict[subject_to_study_list[-1]] - 2 < 0:
                        subject_to_study_list.pop()
                    
                    elif self_studying_time_dict[subject_to_study_list[-1]] - 2 >= 0:
                        while True:
                            if day_list[place_list[0] - 1] != subject_to_study_list[-1]:
                                break
                            subject_to_study_list.pop()
                        
                        while True:
                            if place_list[1] == len(day_list) - 1:
                                break
                            elif day_list[place_list[1] + 1] != subject_to_study_list[-1]:
                                break
                            subject_to_study_list.pop()
                        
                        day_list[place_list[0]] = subject_to_study_list[-1]
                        day_list[place_list[1]] = subject_to_study_list[-1]
                        self_studying_time_dict[subject_to_study_list[-1]] -= 2
                        subject_to_study_list.pop()
                        place_list.pop(0)
                        place_list.pop(0)

                        if subject_to_study_list == []:
                            break
                            
        
        else:  # 周間(要上課的時候)的作法
            subject_to_study_list = []
            for i in range(len(subject_list)):  # 如果當天有上課，就不讀那一科
                subject_to_study_list.append(subject_list[i])
            
            if self_studying_time_dict[subject_to_study_list[-1]] - 2 < 0:
                subject_to_study_list.pop()
            
            while True:  # 各組
                change, place_list = finishing_table(day_list, self_studying_time_dict)  # 一個間隔一個間隔看

                if change % 2 == 0:  # 堂數為偶數
                    number = change // 2  # 組數
                    for i in range(number):  # 一組一組換掉
                        if subject_to_study_list == []:
                            for n in range(len(subject_list)):
                                subject_to_study_list.append(subject_list[n])

                        if self_studying_time_dict[subject_to_study_list[-1]] - 2 < 0:  # 避免剩餘讀書時間小於零
                            subject_to_study_list.pop()

                        elif self_studying_time_dict[subject_to_study_list[-1]] - 2 >= 0:
                            # 避免與前一堂科目相同
                            while True:
                                if day_list[place_list[0] - 1] != subject_to_study_list[-1]:
                                    if self_studying_time_dict[subject_to_study_list[-1]] - 2 < 0:
                                        subject_to_study_list.pop()
                                    break
                                subject_to_study_list.pop()
                            
                            # 避免與後一堂科目相同
                            while True:
                                if place_list[1] == len(day_list) - 1:
                                    break
                                elif day_list[place_list[1] + 1] != subject_to_study_list[-1]:
                                    if self_studying_time_dict[subject_to_study_list[-1]] - 2 < 0:
                                        subject_to_study_list.pop()
                                    break
                                subject_to_study_list.pop()

                            day_list[place_list[0]] = subject_to_study_list[-1]
                            day_list[place_list[1]] = subject_to_study_list[-1]
                            self_studying_time_dict[subject_to_study_list[-1]] -= 2
                            subject_to_study_list.pop()
                            place_list.pop(0)
                            place_list.pop(0)

                            if subject_to_study_list == []:
                                break

                
                else:  # 堂數為基數
                    number = change // 2 - 1  # 組數
                    for i in range(number):  # 一組一組換掉
                        while True:
                            if subject_to_study_list == []:
                                break
                            
                            elif len(place_list) == 3:
                                break
                            
                            elif self_studying_time_dict[subject_to_study_list[-1]] - 2 < 0:  # 避免剩餘讀書時間小於零
                                    subject_to_study_list.pop()
                            
                            elif self_studying_time_dict[subject_to_study_list[-1]] - 2 >= 0:

                                # 避免與前一堂科目相同
                                while True:
                                    if day_list[place_list[0] - 1] != subject_to_study_list[-1]:
                                        break
                                    subject_to_study_list.pop()

                                # 避免與後一堂科目相同
                                while True:
                                    if place_list[1] == len(day_list) - 1:
                                        break
                                    elif day_list[place_list[1] + 1] != subject_to_study_list[-1]:
                                        break
                                    subject_to_study_list.pop()

                                day_list[place_list[0]] = subject_to_study_list[-1]
                                day_list[place_list[1]] = subject_to_study_list[-1]
                                self_studying_time_dict[subject_to_study_list[-1]] -= 2
                                subject_to_study_list.pop()
                                place_list.pop(0)
                                place_list.pop(0)

                    subject_to_study_list = []  # 若可排進讀書時間的科目被清空，則重新加入（從day_list的第一局開始）
                    for n in range(len(subject_list)):
                        if self_studying_time_dict[subject_list[n]] % 2 == 1:
                            subject_to_study_list.append(subject_list[n])
                            subject_to_study_list.reverse()

                    for k in range(len(subject_to_study_list)):  # 排最後剩下三堂的（基數優先）
                        if self_studying_time_dict[subject_to_study_list[k]] != 1 and self_studying_time_dict[subject_to_study_list[k]] % 2 != 0:
                            # 避免與前一堂科目相同
                            while True:
                                if day_list[place_list[0] - 1] != subject_to_study_list[k]:
                                    if self_studying_time_dict[subject_to_study_list[k]] - 3 < 0:
                                        subject_to_study_list.pop(k)
                                    break
                                subject_to_study_list.pop(k)
                            
                            # 避免與後一堂科目相同
                            while True:
                                if place_list[-1] == len(day_list) - 1:
                                    break
                                elif day_list[place_list[-1] + 1] != subject_to_study_list[k]:
                                    if self_studying_time_dict[subject_to_study_list[k]] - 3 < 0:
                                        subject_to_study_list.pop(k)
                                    break
                                subject_to_study_list.pop(k)

                            day_list[place_list[0]] = subject_to_study_list[k]
                            day_list[place_list[1]] = subject_to_study_list[k]
                            day_list[place_list[2]] = subject_to_study_list[k]
                            self_studying_time_dict[subject_to_study_list[k]] -= 3
                            subject_to_study_list.pop(k)
                            place_list.pop(0)
                            place_list.pop(0)
                            place_list.pop(0)
                            break

                    if place_list != []:
                        if subject_to_study_list == []:
                            for n in range(len(day_list)):
                                if day_list[n] == '3':
                                    continue
                                if day_list[n] not in subject_to_study_list and self_studying_time_dict[day_list[n]] % 2 == 0:
                                    subject_to_study_list.append(day_list[n])


                        for k in range(len(subject_to_study_list)):
                            if self_studying_time_dict[subject_to_study_list[k]] > 2:  # 排最後剩下三堂的（無基數的情況）
                                # 避免與前一堂科目相同
                                while True:
                                    if day_list[place_list[0] - 1] != subject_to_study_list[k]:
                                        if self_studying_time_dict[subject_to_study_list[k]] - 3 < 0:
                                            subject_to_study_list.pop(k)
                                        break
                                    subject_to_study_list.pop(k)
                                
                                # 避免與後一堂科目相同
                                while True:
                                    if place_list[-1] == len(day_list) - 1:
                                        break
                                    elif day_list[place_list[-1] + 1] != subject_to_study_list[k]:
                                        if self_studying_time_dict[subject_to_study_list[k]] - 3 < 0:
                                            subject_to_study_list.pop(k)
                                        break
                                    subject_to_study_list.pop(k)

                                day_list[place_list[0]] = subject_to_study_list[k]
                                day_list[place_list[1]] = subject_to_study_list[k]
                                day_list[place_list[2]] = subject_to_study_list[k]
                                self_studying_time_dict[subject_to_study_list[k]] -= 3
                                subject_to_study_list.pop(k)
                                place_list.pop(0)
                                place_list.pop(0)
                                place_list.pop(0)
                                break

                if day_list.count('3') == 0:
                    break

    final_week_list.append(day_list)
    print(day_list)
print(final_week_list)
print(self_studying_time_dict)







