def J2_r():
    global print_list, bgr_schedule, playJ2r, origin, improve, weight
    
    # 演算法
    if playJ2r == 0:
        
        # 計算有多少讀書時間及課程時間
        study = 0
        lecture = 0
        for b1 in range(3):
            for b2 in range(8):
                for b3 in range(7):
                    if bglb_list[b1][b2][b3][1] == '讀書':
                        study += 1
                    elif bglb_list[b1][b2][b3][1] in Csort_dict:
                        lecture += 1

        # 安排讀書科目的先後順序
        compare = []
        for b4 in range(study + lecture):
            orderS = sorted(zip(Ssort_dict.values(), Ssort_dict.keys()), reverse=True)
            compare.append([Ssort_dict[orderS[0][1]][0], orderS[0][1]])
            Ssort_dict[orderS[0][1]][8] += Ssort_dict[orderS[0][1]][0] / Ssort_dict[orderS[0][1]][1]
            Ssort_dict[orderS[0][1]][0] -= (0.1 + Ssort_dict[orderS[0][1]][7] * Ssort_dict[orderS[0][1]][6]) * Ssort_dict[orderS[0][1]][1]
            Ssort_dict[orderS[0][1]][6] += 1
            if Ssort_dict[orderS[0][1]][8] >= 100 or Ssort_dict[orderS[0][1]][0] < 0:
                Ssort_dict[orderS[0][1]][0] = 0

        # 決定要去上課還是讀書
        takecourse = dict()
        for b5 in range(lecture):
            orderC = sorted(zip(Csort_dict.values(), Csort_dict.keys()), reverse=True)
            if compare[-1][0] > orderC[0][0][0]:
                break
            Ssort_dict[compare[-1][1]][8] -= compare[-1][0] / Ssort_dict[compare[-1][1]][1]
            Ssort_dict[compare[-1][1]][0] = compare[-1][0]
            Ssort_dict[compare[-1][1]][6] -= 1
            compare.remove(compare[-1])
            if orderC[0][1] not in takecourse:
                takecourse[orderC[0][1]] = [1, Csort_dict[orderC[0][1]][0] / Csort_dict[orderC[0][1]][1]]
            else:
                takecourse[orderC[0][1]][0] += 1
            Csort_dict[orderC[0][1]][6] -= 1
            if Csort_dict[orderC[0][1]][6] == 0:
                del Csort_dict[orderC[0][1]]

        # 刪除出席不滿1/2的課
        for b6 in takecourse:

            # 計算某一門課的連續課堂數
            breakP = []
            for b7 in range(7):
                accu = 0
                for b8 in range(3):
                    for b9 in range(8):
                        if bglb_list[b8][b9][b7][1] == b6:
                            accu += 1
                        elif bglb_list[b8][b9][b7][1] != b6 and accu != 0:
                            breakP.append([accu, -1 * b8, -1 * (b9 - accu), -1 * b7])
                            accu = 0
            breakP.sort()
            breakP.reverse()
            
            # 判斷出席課堂數是否小於1/2
            for b10 in breakP:
                if b10[0] < 2 * takecourse[b6][0]:
                    if b10[0] >= takecourse[b6][0]:
                        for b11 in range(takecourse[b6][0]):
                            if -8 <= -1 * b10[2] + b11 < 0:
                                print_list[-1 * b10[1] - 1][8 - b10[2] + b11][-1 * b10[3]][0] = 1
                                print_list[-1 * b10[1] - 1][8 - b10[2] + b11][-1 * b10[3]][1] = b6
                                Ssort_dict[b6][8] += takecourse[b6][1]
                            elif -1 * b10[2] + b11 < -8:
                                print_list[-1 * b10[1] - 2][16 - b10[2] + b11][-1 * b10[3]][0] = 1
                                print_list[-1 * b10[1] - 2][16 - b10[2] + b11][-1 * b10[3]][1] = b6
                                Ssort_dict[b6][8] += takecourse[b6][1]
                            else:
                                print_list[-1 * b10[1]][-1 * b10[2] + b11][-1 * b10[3]][0] = 1
                                print_list[-1 * b10[1]][-1 * b10[2] + b11][-1 * b10[3]][1] = b6
                                Ssort_dict[b6][8] += takecourse[b6][1]
                        takecourse[b6][0] = 0
                    else:
                        for b12 in range(b10[0]):
                            if -8 <= -1 * b10[2] + b12 < 0:
                                print_list[-1 * b10[1] - 1][8 - b10[2] + b12][-1 * b10[3]][0] = 1
                                print_list[-1 * b10[1] - 1][8 - b10[2] + b12][-1 * b10[3]][1] = b6
                                Ssort_dict[b6][8] += takecourse[b6][1]
                            elif -1 * b10[2] + b12 < -8:
                                print_list[-1 * b10[1] - 2][16 - b10[2] + b12][-1 * b10[3]][0] = 1
                                print_list[-1 * b10[1] - 2][16 - b10[2] + b12][-1 * b10[3]][1] = b6
                                Ssort_dict[b6][8] += takecourse[b6][1]
                            else:
                                print_list[-1 * b10[1]][-1 * b10[2] + b12][-1 * b10[3]][0] = 1
                                print_list[-1 * b10[1]][-1 * b10[2] + b12][-1 * b10[3]][1] = b6
                                Ssort_dict[b6][8] += takecourse[b6][1]
                        takecourse[b6][0] -= b10[0]
                else:
                    continue

            # 用讀書補滿不去的課
            for b13 in range(takecourse[b6][0]):
                orderS = sorted(zip(Ssort_dict.values(), Ssort_dict.keys()), reverse=True)
                compare.append([Ssort_dict[orderS[0][1]][0], orderS[0][1]])
                Ssort_dict[orderS[0][1]][8] += Ssort_dict[orderS[0][1]][0] / Ssort_dict[orderS[0][1]][1]
                Ssort_dict[orderS[0][1]][0] -= (0.1 + Ssort_dict[orderS[0][1]][7] * Ssort_dict[orderS[0][1]][6]) * Ssort_dict[orderS[0][1]][1]
                Ssort_dict[orderS[0][1]][6] += 1
                if Ssort_dict[orderS[0][1]][8] >= 100 or Ssort_dict[orderS[0][1]][0] < 0:
                    Ssort_dict[orderS[0][1]][0] = 0

        # 加入絕對不能蹺的課的上課效益
        for b14 in noskip_dict:
            Ssort_dict[b14][8] += noskip_dict[b14][0] / noskip_dict[b14][1] * noskip_dict[b14][2]

        # 判斷單一科目要讀多久才會及格，排出優先順序（最容易及格的先補）
        check = dict()
        for b15 in Ssort_dict:
            moretime = 0
            testscore = Ssort_dict[b15][8]
            testutil = Ssort_dict[b15][0]
            while True:
                if testscore < 60 and testutil >= 0:
                    print(testscore, testutil)
                    testscore += testutil / Ssort_dict[b15][1]
                    testutil -= (0.1 + Ssort_dict[b15][7] * (Ssort_dict[b15][6] + moretime)) * Ssort_dict[b15][1]
                    moretime += 1
                else:
                    break
            check[b15] = [moretime, Ssort_dict[b15][8]]

        # 判斷是否及格
        check_list = sorted(zip(check.values(), check.keys()))
        make_up = []
        for b16 in check_list:
            while Ssort_dict[b16[1]][8] < 60:
                change = -1
                while True:
                    if compare != []:
                        if Ssort_dict[compare[change][1]][8] - compare[-1][0] < 60:
                            if -1 * change == len(Ssort_dict):
                                break
                            change -= 1
                            continue
                        else:
                            if Ssort_dict[compare[change][1]][6] == 0:
                                change -= 1
                                continue
                            compare.remove(compare[change])
                            Ssort_dict[compare[change][1]][8] -= Ssort_dict[orderS[change][1]][0] / Ssort_dict[orderS[change][1]][1] - (0.1 + (Ssort_dict[orderS[change][1]][7] - 1) * Ssort_dict[orderS[change][1]][6])
                            Ssort_dict[compare[change][1]][0] = compare[change][0]
                            Ssort_dict[compare[change][1]][6] -= 1
                            compare.remove(compare[change])
                            make_up.append([Ssort_dict[b16[1]][0], b16[1]])
                            Ssort_dict[b16[1]][8] += Ssort_dict[b16[1]][0] / Ssort_dict[b16[1]][1]
                            Ssort_dict[b16[1]][0] -= (0.1 + Ssort_dict[b16[1]][7] * Ssort_dict[b16[1]][6]) * Ssort_dict[b16[1]][1]
                            Ssort_dict[b16[1]][6] += 1
                            break
                    else:
                        change = -1 * len(Ssort_dict)
                        break
                if -1 * change == len(Ssort_dict):
                    break

        # 取得裸考總分、排完後可獲得總分、每一科占比*學分數的加總
        for b17 in subj:
            origin += Ssort_dict[b17][10] * Ssort_dict[b17][1]
            improve += Ssort_dict[b17][8] * Ssort_dict[b17][1]
            weight += Ssort_dict[b17][1]
            if Ssort_dict[b17][6] == 0:
                del Ssort_dict[b17]
        
        # 未完待續
