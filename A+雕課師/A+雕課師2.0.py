# -*- coding: UTF-8 -*-
# 引入pygame、tkinter、datetime、math與初始化
import pygame
import tkinter as tk
from tkinter import ttk
import datetime
import math
import copy
import os
pygame.init()
pygame.mixer.init()  # 將混音器初始化

# 設定視窗
window = pygame.display.set_mode((1360, 765))  # 輸入視窗大小（1360*765）
pygame.display.set_caption('A+雕課師')  # 為視窗命名

dir = os.path.dirname(__file__)
# 呈現loading畫面
load = pygame.image.load(os.path.join(dir, 'load.png'))  # 引入loading畫面
load.convert_alpha()  # 畫入loading圖檔
load = pygame.transform.smoothscale(load, (1360, 765))  # 長寬設成1360*765（視窗大小）
window.blit(load, (0, 0))  # 設定loading圖檔位置為(0, 0)
pygame.display.update()  # 顯示

# 載入所有圖片
bg = pygame.image.load(os.path.join(dir, 'bg.png'))  # 引入首頁背景
bg.convert_alpha()  # 畫入首頁圖檔
bg = pygame.transform.smoothscale(bg, (1360, 765))  # 長寬設成1360*765（視窗大小）

sp1 = pygame.image.load(os.path.join(dir, 'sp1.png'))  # 引入步驟一按鈕（沒陰影）
sp1.convert_alpha()  # 畫入步驟一按鈕（沒陰影）圖檔
sp1 = pygame.transform.smoothscale(sp1, (340, 425))  # 長寬設成340*425

sp1_2 = pygame.image.load(os.path.join(dir, 'sp1-2.png'))  # 引入步驟一按鈕（有陰影）
sp1_2.convert_alpha()  # 畫入步驟一按鈕（有陰影）圖檔
sp1_2 = pygame.transform.smoothscale(sp1_2, (340, 425))  # 長寬設成340*425

sp2 = pygame.image.load(os.path.join(dir, 'sp2.png'))  # 引入步驟二按鈕（沒陰影）
sp2.convert_alpha()  # 畫入步驟二按鈕（沒陰影）圖檔
sp2 = pygame.transform.smoothscale(sp2, (340, 425))  # 長寬設成340*425

sp2_2 = pygame.image.load(os.path.join(dir, 'sp2-2.png'))  # 引入步驟二按鈕（有陰影）
sp2_2.convert_alpha()  # 畫入步驟二按鈕（有陰影）圖檔
sp2_2 = pygame.transform.smoothscale(sp2_2, (340, 425))  # 長寬設成340*425

ab = pygame.image.load(os.path.join(dir, 'ab.png'))  # 引入about按鈕（白色）
ab.convert_alpha()  # 畫入about按鈕（白色）圖檔
ab = pygame.transform.smoothscale(ab, (200, 80))  # 長寬設成200*80

ab_2 = pygame.image.load(os.path.join(dir, 'ab-2.png'))  # 引入about按鈕（黑色）
ab_2.convert_alpha()  # 畫入about按鈕（黑色）圖檔
ab_2 = pygame.transform.smoothscale(ab_2, (200, 80))  # 長寬設成200*80

hm = pygame.image.load(os.path.join(dir, 'hm.png'))  # 引入home鍵（白色）（按下會回到首頁）
hm.convert_alpha()  # 畫入home鍵（白色）圖檔
hm = pygame.transform.smoothscale(hm, (200, 80))  # 長寬設成200*80

hm_2 = pygame.image.load(os.path.join(dir, 'hm-2.png'))  # 引入home鍵（黑色）（按下會回到首頁）
hm_2.convert_alpha()  # 畫入home鍵（黑色）圖檔
hm_2 = pygame.transform.smoothscale(hm_2, (200, 80))  # 長寬設成200*80

nx = pygame.image.load(os.path.join(dir, 'nx.png'))  # 引入next鍵（白色）（按下會顯示結果）
nx.convert_alpha()  # 畫入next鍵（白色）圖檔
nx = pygame.transform.smoothscale(nx, (200, 80))  # 長寬設成200*80

nx_2 = pygame.image.load(os.path.join(dir, 'nx-2.png'))  # 引入next鍵（黑色）（按下會顯示結果）
nx_2.convert_alpha()  # 畫入next鍵（黑色）圖檔
nx_2 = pygame.transform.smoothscale(nx_2, (200, 80))  # 長寬設成200*80

bgl_1 = pygame.image.load(os.path.join(dir, 'bgl-1.png'))  # 引入課表00:00-08:00
bgl_1.convert_alpha()  # 畫入課表00:00-08:00圖檔
bgl_1 = pygame.transform.smoothscale(bgl_1, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgl_2 = pygame.image.load(os.path.join(dir, 'bgl-2.png'))  # 引入課表08:00-16:00
bgl_2.convert_alpha()  # 畫入課表08:00-16:00圖檔
bgl_2 = pygame.transform.smoothscale(bgl_2, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgl_3 = pygame.image.load(os.path.join(dir, 'bgl-3.png'))  # 引入課表16:00-00:00
bgl_3.convert_alpha()  # 畫入課表16:00-00:00圖檔
bgl_3 = pygame.transform.smoothscale(bgl_3, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgr_1 = pygame.image.load(os.path.join(dir, 'bgr-1.png'))  # 引入課表結果00:00-08:00
bgr_1.convert_alpha()  # 畫入課表結果00:00-08:00圖檔
bgr_1 = pygame.transform.smoothscale(bgr_1, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgr_2 = pygame.image.load(os.path.join(dir, 'bgr-2.png'))  # 引入課表結果08:00-16:00
bgr_2.convert_alpha()  # 畫入課表結果08:00-16:00圖檔
bgr_2 = pygame.transform.smoothscale(bgr_2, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgr_3 = pygame.image.load(os.path.join(dir, 'bgr-3.png'))  # 引入課表結果16:00-00:00
bgr_3.convert_alpha()  # 畫入課表結果16:00-00:00圖檔
bgr_3 = pygame.transform.smoothscale(bgr_3, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgc_1 = pygame.image.load(os.path.join(dir, 'bgc-1.png'))  # 引入課表選擇00:00-08:00
bgc_1.convert_alpha()  # 畫入課表結果00:00-08:00圖檔
bgc_1 = pygame.transform.smoothscale(bgc_1, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgc_2 = pygame.image.load(os.path.join(dir, 'bgc-2.png'))  # 引入課表選擇08:00-16:00
bgc_2.convert_alpha()  # 畫入課表結果08:00-16:00圖檔
bgc_2 = pygame.transform.smoothscale(bgc_2, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgc_3 = pygame.image.load(os.path.join(dir, 'bgc-3.png'))  # 引入課表選擇16:00-00:00
bgc_3.convert_alpha()  # 畫入課表結果16:00-00:00圖檔
bgc_3 = pygame.transform.smoothscale(bgc_3, (1360, 765))  # 長寬設成1360*765（視窗大小）

bglb = pygame.image.load(os.path.join(dir, 'bglb.png'))  # 引入藍色方塊（點選不一定要出席的時段呈藍色）
bglb.convert_alpha()  # 畫入藍色方塊圖檔
bglb = pygame.transform.smoothscale(bglb, (85, 51))  # 長寬設成85*51

bglb_2 = pygame.image.load(os.path.join(dir, 'bglb-2.png'))  # 引入深灰色方塊（滑過的時段呈深灰色）
bglb_2.convert_alpha()  # 畫入深灰色方塊圖檔
bglb_2 = pygame.transform.smoothscale(bglb_2, (85, 51))  # 長寬設成85*51

bglb_3 = pygame.image.load(os.path.join(dir, 'bglb-3.png'))  # 引入淺灰色方塊（沒有任何指令時呈淺灰色）
bglb_3.convert_alpha()  # 畫入淺灰色方塊圖檔
bglb_3 = pygame.transform.smoothscale(bglb_3, (85, 51))  # 長寬設成85*51

bglb_4 = pygame.image.load(os.path.join(dir, 'bglb-4.png'))  # 引入綠色方塊（上課呈綠色）
bglb_4.convert_alpha()  # 畫入綠色方塊圖檔
bglb_4 = pygame.transform.smoothscale(bglb_4, (85, 51))  # 長寬設成85*51

bglb_5 = pygame.image.load(os.path.join(dir, 'bglb-5.png'))  # 引入粉紅色方塊（讀書呈粉紅色）
bglb_5.convert_alpha()  # 畫入粉紅色方塊圖檔
bglb_5 = pygame.transform.smoothscale(bglb_5, (85, 51))  # 長寬設成85*51

bglb_6 = pygame.image.load(os.path.join(dir, 'bglb-6.png'))  # 引入橘色方塊（點選一定要出席的時段呈橘色）
bglb_6.convert_alpha()  # 畫入橘色方塊圖檔
bglb_6 = pygame.transform.smoothscale(bglb_6, (85, 51))  # 長寬設成85*51

bglb_7 = pygame.image.load(os.path.join(dir, 'bglb-7.png'))  # 引入黃色方塊（一定要出席的時段呈黃色）
bglb_7.convert_alpha()  # 畫入黃色方塊圖檔
bglb_7 = pygame.transform.smoothscale(bglb_7, (85, 51))  # 長寬設成85*51

bglb_8 = pygame.image.load(os.path.join(dir, 'bglb-8.png'))  # 引入紫色方塊（選擇的時段呈紫色）
bglb_8.convert_alpha()  # 畫入紫色方塊圖檔
bglb_8 = pygame.transform.smoothscale(bglb_8, (85, 51))  # 長寬設成85*51

up = pygame.image.load(os.path.join(dir, 'up.png'))  # 引入向上按鈕（咖啡色）（可以回到上一頁課表）
up.convert_alpha()  # 畫入向上按鈕（咖啡色）圖檔
up = pygame.transform.smoothscale(up, (51, 51))  # 長寬設成51*51

up_2 = pygame.image.load(os.path.join(dir, 'up-2.png'))  # 引入向上按鈕（白色）（按下按鈕時變白色）
up_2.convert_alpha()  # 畫入向上按鈕（白色）圖檔
up_2 = pygame.transform.smoothscale(up_2, (51, 51))  # 長寬設成51*51

down = pygame.image.load(os.path.join(dir, 'down.png'))  # 引入向下按鈕（咖啡色）（可以到下一頁課表）
down.convert_alpha()  # 畫入向下按鈕（咖啡色）圖檔
down = pygame.transform.smoothscale(down, (51, 51))  # 長寬設成51*51

down_2 = pygame.image.load(os.path.join(dir, 'down-2.png'))  # 引入向下按鈕（白色）（按下按鈕時變白色）
down_2.convert_alpha()  # 畫入向下按鈕（白色）圖檔
down_2 = pygame.transform.smoothscale(down_2, (51, 51))  # 長寬設成51*51

pls = pygame.image.load(os.path.join(dir, 'pls.png'))  # 引入「標記為讀書時間」按鈕（咖啡色）
pls.convert_alpha()  # 畫入「標記為讀書時間」按鈕（咖啡色）圖檔
pls = pygame.transform.smoothscale(pls, (102, 51))  # 長寬設成102*51

pls_2 = pygame.image.load(os.path.join(dir, 'pls-2.png'))  # 引入「標記為讀書時間」按鈕（白色）
pls_2.convert_alpha()  # 畫入「標記為讀書時間」按鈕（白色）圖檔
pls_2 = pygame.transform.smoothscale(pls_2, (102, 51))  # 長寬設成102*51

plc = pygame.image.load(os.path.join(dir, 'plc.png'))  # 引入「加入課程」按鈕（咖啡色）
plc.convert_alpha()  # 畫入「加入課程」按鈕（咖啡色）圖檔
plc = pygame.transform.smoothscale(plc, (102, 51))  # 長寬設成102*51

plc_2 = pygame.image.load(os.path.join(dir, 'plc-2.png'))  # 引入「加入課程」按鈕（白色）
plc_2.convert_alpha()  # 畫入「加入課程」按鈕（白色）圖檔
plc_2 = pygame.transform.smoothscale(plc_2, (102, 51))  # 長寬設成102*51

show = pygame.image.load(os.path.join(dir, 'show.png'))  # 引入課程資訊顯示框
show.convert_alpha()  # 畫入課程資訊顯示框圖檔
show = pygame.transform.smoothscale(show, (221, 340))  # 長寬設成221*340

left = pygame.image.load(os.path.join(dir, 'left.png'))  # 引入向左按鈕（咖啡色）（可以回到上一頁課程資訊）
left.convert_alpha()  # 畫入向左按鈕（咖啡色）圖檔
left = pygame.transform.smoothscale(left, (17, 17))  # 長寬設成17*17

left_2 = pygame.image.load(os.path.join(dir, 'left-2.png'))  # 引入向左按鈕（白色）（按下按鈕時變白色）
left_2.convert_alpha()  # 畫入向左按鈕（白色）圖檔
left_2 = pygame.transform.smoothscale(left_2, (17, 17))  # 長寬設成17*17

right = pygame.image.load(os.path.join(dir, 'right.png'))  # 引入向右按鈕（咖啡色）（可以到下一頁課程資訊）
right.convert_alpha()  # 畫入向右按鈕（咖啡色）圖檔
right = pygame.transform.smoothscale(right, (17, 17))  # 長寬設成17*17

right_2 = pygame.image.load(os.path.join(dir, 'right-2.png'))  # 引入向右按鈕（白色）（按下按鈕時變白色）
right_2.convert_alpha()  # 畫入向右按鈕（白色）圖檔
right_2 = pygame.transform.smoothscale(right_2, (17, 17))  # 長寬設成17*17

# 定義函數
def J1():
    """首頁"""
    global page, subj
    
    # 滑鼠事件
    mouses = pygame.mouse.get_pos()  # 追蹤滑鼠位置
    buttons = pygame.mouse.get_pressed()  # 偵測滑鼠有沒有被按下及如何被按下
    
    # 置入背景
    window.blit(bg, (0, 0))
    
    # 步驟一
    if 313 <= mouses[0] <= 595 and 300 <= mouses[1] <= 625:  # 滑鼠在步驟一的位置
        if buttons[0]:  # 按下滑鼠左鍵
            pygame.time.wait(75)  # 程式暫停75毫秒(防止程式在按下滑鼠的過程中跑了好幾次迴圈)
            if start == None:
                winD()  # 第一次按下步驟一會彈出輸入起始日期的視窗
            else:
                page = 2  # 直接切換到輸入課表的頁面
        else:
            window.blit(sp1_2, (283, 250))  # 滑鼠在步驟一的位置但沒按下滑鼠，視窗蓋上步驟一（有陰影）
    else:
        window.blit(sp1, (283, 250))  # 滑鼠不在步驟一的位置，視窗蓋上步驟一
    
    # 步驟二
    if 767 <= mouses[0] <= 977 and 300 <= mouses[1] <= 625:  # 滑鼠在步驟二的位置
        if buttons[0]:
            pygame.time.wait(75)
            if subject != {}:
                page = 3
                for p1 in subject:
                    Ssort_dict[p1] = [float(efficiency[p1][0]) * percentage[p1] * classcredit[p1], percentage[p1] * classcredit[p1], percentage[p1], classcredit[p1], 0, float(efficiency[p1][1])]
                    if chooseclass[p1] != 0:
                        Csort_dict[p1] = [float(classutility[p1][0]) * percentage[p1] * classcredit[p1], percentage[p1] * classcredit[p1], percentage[p1], classcredit[p1], chooseclass[p1]]
            else:
                error('尚未輸入資料')
        else:
            window.blit(sp2_2, (737, 250))
    else:
        window.blit(sp2, (737, 250))
    
    # about
    if 1148 <= mouses[0] <= 1347 and 30 <= mouses[1] <= 110:  # 滑鼠在about的位置
        window.blit(ab_2, (1148, 30))
    else:
        window.blit(ab, (1148, 30))
    
    # 顯示
    pygame.display.update()


def J2_l():
    """輸入資料"""
    global page, bgl_schedule, bglb_list, start, which, subj
    mouses = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    
    # 判斷要顯示表的第幾頁
    if bgl_schedule == 1:
        window.blit(bgl_1, (0, 0))  # 視窗蓋上表的第一頁（00:00-08:00）
    elif bgl_schedule == 2:
        window.blit(bgl_2, (0, 0))  # 視窗蓋上表的第二頁（08:00-16:00）
    elif bgl_schedule == 3:
        window.blit(bgl_3, (0, 0))  # 視窗蓋上表的第三頁（16:00-00:00）
    window.blit(show, (34, 153))

    # 判斷現在有沒有格子被點選（變成藍色）
    hcc = 0
    for a1 in range(3):
        for a2 in range(8):
            for a3 in range(7):
                if bglb_list[a1][a2][a3][0] == 2 or bglb_list[a1][a2][a3][0] == 2.5:
                    hcc += 1
    
    # 如果現在所在資訊頁面超過頁面數（因為刪除了原本加入的課程，以至於最後一頁不見），就會退到上一頁
    if which > (len(subject) - 1) // 4 :
        which = (len(subject) - 1) // 4 if (len(subject) - 1) // 4 >= 0 else 0
    
    # 課程資訊呈現
    presubj = list(subject.values())  # 先把所有課程資訊（字典subj的值）提出來成為一個清單
    if subject != {}:
        a = len(subject) - ((len(subject) - 1) // 4) * 4  # 一個頁面通常有4堂課的課程資訊，但最後一頁可能不足4個
        for a4 in range(4 if which != ((len(subject) - 1) // 4) else a):
            if len(presubj[which * 4 + a4][0]) > 9:
                info1 = fontObjS.render('課程名稱：%s' % (presubj[which * 4 + a4][0:8] + '…'), True, (0, 0, 0))  # 課程名稱超過8個字會被省略
            else:
                info1 = fontObjS.render('課程名稱：%s' % (presubj[which * 4 + a4]), True, (0, 0, 0))
            info2 = fontObjS.render('學分數：%s' % str(classcredit[presubj[which * 4 + a4]]), True, (0, 0, 0)) 
            info3 = fontObjS.render('本次考試占總成績比例：%s %s' % (str(percentage[presubj[which * 4 + a4]]), '%'), True, (0, 0, 0))
            info4 = fontObjS.render('上課效益：%s' % str(classutility[presubj[which * 4 + a4]][2]), True, (0, 0, 0))
            info5 = fontObjS.render('自己讀的吸收度：%s' % str(efficiency[presubj[which * 4 + a4]][2]), True, (0, 0, 0))
            window.blit(info1, (40, 158 + a4 * 85))  # 將資訊置於正確的位置
            window.blit(info2, (40, 173 + a4 * 85))
            window.blit(info3, (40, 188 + a4 * 85))
            window.blit(info4, (40, 203 + a4 * 85))
            window.blit(info5, (40, 218 + a4 * 85))
            # 判斷該課程資訊有無被點擊，若有（且沒有點選任何新的時段）則跳出修改課程的視窗
            if 34 <= mouses[0] <= 255 and 153 + a4 * 85 <= mouses[1] <= 238 + a4 * 85 and buttons[0]:
                if hcc == 0:
                    pygame.time.wait(100)
                    correct(presubj[which * 4 + a4])
                else:
                    pygame.time.wait(100)
                    for a14 in range(3):
                        for a15 in range(8):
                            for a16 in range(7):
                                if bglb_list[a14][a15][a16][0] == 2:
                                    bglb_list[a14][a15][a16] = [3, presubj[which * 4 + a4]]
                                    chooseclass[presubj[which * 4 + a4]] += 1
                                elif bglb_list[a14][a15][a16][0] == 2.5:
                                    bglb_list[a14][a15][a16] = [3.5, presubj[which * 4 + a4]]
                                    neverskipclass[presubj[which * 4 + a4]] += 1

    # 顯示日期
    orid = start  # 起始日期
    for a5 in range(7):
        pred = fontObj.render('{:^5s}'.format(str(orid.month) + '/' + str(orid.day)), True, (0, 0, 0))  # 日期
        prew = fontObj.render('{:^5s}'.format('（' + week[orid.weekday()] + '）'), True, (0, 0, 0))  # 星期幾
        x = datetime.timedelta(days=a5 + 1)
        orid = start + x  # 加一天
        window.blit(pred, (482 + 113 * a5, 81))
        window.blit(prew, (468 + 113 * a5, 110))
    
    # 切換表的頁面（上）
    if 1286 <= mouses[0] <= 1337 and 605 <= mouses[1] <= 656:
        if buttons[0]:
            if bgl_schedule == 2:
                pygame.time.wait(100)
                bgl_schedule = 1                
            elif bgl_schedule == 3:
                pygame.time.wait(100)
                bgl_schedule = 2
        else:
            window.blit(up_2, (1286, 605))
    else:
        window.blit(up, (1286, 605))
    
    # 切換表的頁面（下）
    if 1286 <= mouses[0] <= 1337 and 666 <= mouses[1] <= 717:
        if buttons[0]:
            if bgl_schedule == 1:
                pygame.time.wait(100)
                bgl_schedule = 2
            elif bgl_schedule == 2:
                pygame.time.wait(100)
                bgl_schedule = 3
        else:
            window.blit(down_2, (1286, 666))
    else:
        window.blit(down, (1286, 666))
    
    bglb_x = 0  # 第一格的x座標 - 465
    bglb_y = 0  # 第一格的y座標 - 145
    # 判斷格子狀態
    for a6 in range(8):
        for a7 in range(7):
            if 465 + bglb_x <= mouses[0] <= 550 + bglb_x and 145 + bglb_y <= mouses[1] <= 196 + bglb_y:
                if bglb_list[bgl_schedule - 1][a6][a7][0] != 2 and bglb_list[bgl_schedule - 1][a6][a7][0] != 2.5 and bglb_list[bgl_schedule - 1][a6][a7][0] != 3 and bglb_list[bgl_schedule - 1][a6][a7][0] != 3.5:
                    if buttons[0]:  # 滑鼠在格子上、原本沒被點選、現在按滑鼠左鍵
                        pygame.time.wait(100)
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 2  # 狀態二為變藍色
                    elif buttons[2]:  # 滑鼠在格子上、原本沒被點選、現在按滑鼠右鍵
                        pygame.time.wait(100)
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 2.5  # 狀態二點五為變橘色
                    else:  # 滑鼠在格子上、原本沒被點選、現在沒按滑鼠
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 1  # 狀態一為變深灰色
                elif bglb_list[bgl_schedule - 1][a6][a7][0] == 2 or bglb_list[bgl_schedule - 1][a6][a7][0] == 2.5:
                    if buttons[0]:  # 滑鼠在格子上、原本被點選（沒課程）、現在按滑鼠
                        pygame.time.wait(100)
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 1
                elif bglb_list[bgl_schedule - 1][a6][a7][0] == 3 or bglb_list[bgl_schedule - 1][a6][a7][0] == 3.5:
                    if buttons[0]:  # 滑鼠在格子上、原本被點選（有課程）、現在按滑鼠
                        pygame.time.wait(100)
                        if bglb_list[bgl_schedule - 1][a6][a7][1] != '讀書':  # 若不是讀書，要將該課程的總堂數減一，該課程的格子已經被刪光時要將該課程從字典中移除
                            if bglb_list[bgl_schedule - 1][a6][a7][0] == 3:
                                chooseclass[bglb_list[bgl_schedule - 1][a6][a7][1]] -= 1
                            else:
                                neverskipclass[bglb_list[bgl_schedule - 1][a6][a7][1]] -= 1
                            if chooseclass[bglb_list[bgl_schedule - 1][a6][a7][1]] + neverskipclass[bglb_list[bgl_schedule - 1][a6][a7][1]] == 0:
                                del subject[bglb_list[bgl_schedule - 1][a6][a7][1]]
                                del classcredit[bglb_list[bgl_schedule - 1][a6][a7][1]]
                                del percentage[bglb_list[bgl_schedule - 1][a6][a7][1]]
                                del classutility[bglb_list[bgl_schedule - 1][a6][a7][1]]
                                del efficiency[bglb_list[bgl_schedule - 1][a6][a7][1]]
                                del chooseclass[bglb_list[bgl_schedule - 1][a6][a7][1]]
                                del neverskipclass[bglb_list[bgl_schedule - 1][a6][a7][1]]
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 1
                        bglb_list[bgl_schedule - 1][a6][a7][1] = -1
            if bglb_list[bgl_schedule - 1][a6][a7][0] == 1:  # 狀態一為變深灰色
                window.blit(bglb_2, (465 + bglb_x, 145 + bglb_y))
                bglb_list[bgl_schedule - 1][a6][a7][0] = 0  # 狀態零為變淺灰色
            elif bglb_list[bgl_schedule - 1][a6][a7][0] == 2:  # 狀態二為變藍色
                window.blit(bglb, (465 + bglb_x, 145 + bglb_y))
            elif bglb_list[bgl_schedule - 1][a6][a7][0] == 2.5:
                window.blit(bglb_6, (465 + bglb_x, 145 + bglb_y))
            elif bglb_list[bgl_schedule - 1][a6][a7][0] == 0:  # 狀態零為變淺灰色
                window.blit(bglb_3, (465 + bglb_x, 145 + bglb_y))
            elif bglb_list[bgl_schedule - 1][a6][a7][0] == 3:  # 狀態三為變藍色+顯示課程名稱
                window.blit(bglb, (465 + bglb_x, 145 + bglb_y))
                prename = fontObj.render(bglb_list[bgl_schedule - 1][a6][a7][1] if len(bglb_list[bgl_schedule - 1][a6][a7][1]) <= 3 else bglb_list[bgl_schedule - 1][a6][a7][1][0:2] + '…', True, (0, 0, 0))
                window.blit(prename, (475 + bglb_x, 160 + bglb_y))
            else:  # 狀態三點五為變橘色+顯示課程名稱
                window.blit(bglb_6, (465 + bglb_x, 145 + bglb_y))
                prename = fontObj.render(bglb_list[bgl_schedule - 1][a6][a7][1] if len(bglb_list[bgl_schedule - 1][a6][a7][1]) <= 3 else bglb_list[bgl_schedule - 1][a6][a7][1][0:2] + '…', True, (0, 0, 0))
                window.blit(prename, (475 + bglb_x, 160 + bglb_y))
            bglb_x += 113  # x座標向右位移113
        bglb_x = 0  # 一排7個畫滿後，x座標的位移量歸零
        bglb_y += 72  # 下移72，開始畫新的一排
    
    # 切換課程資訊頁面（左）
    if 221 <= mouses[0] <= 238 and 119 <= mouses[1] <= 136:
        if buttons[0]:
            if which != 0:    # 如果不在第一頁
                pygame.time.wait(100)
                which -= 1
        else:
            window.blit(left_2, (221, 119))
    else:
        window.blit(left, (221, 119))
    
    # 切換課程資訊頁面（右）
    if 246 <= mouses[0] <= 263 and 119 <= mouses[1] <= 136:
        if buttons[0]:
            if which != ((len(subject) - 1) // 4) if (len(subject) - 1) // 4 >= 0 else 0:  # 如果不在最後一頁
                pygame.time.wait(100)
                which += 1
        else:
            window.blit(right_2, (246, 119))
    else:
        window.blit(right, (246, 119))
    
    # 讀書時間標記
    if 33 <= mouses[0] <= 135 and 43 <= mouses[1] <= 94:
        if buttons[0]:
            pygame.time.wait(100)
            clickerror = 0
            for a8 in range(3):
                for a9 in range(8):
                    for a10 in range(7):
                        if bglb_list[a8][a9][a10][0] == 2.5:
                            clickerror = 1
            if clickerror == 1:
                error('請按左鍵選取讀書時間')
            else:
                for a11 in range(3):
                    for a12 in range(8):
                        for a13 in range(7):
                            if bglb_list[a11][a12][a13][0] == 2:
                                bglb_list[a11][a12][a13] = [3, '讀書']
                            
        else:
            window.blit(pls_2, (33, 43))
    else:
        window.blit(pls, (33, 43))
    
    # 輸入課程資訊
    if 161 <= mouses[0] <= 263 and 43 <= mouses[1] <= 94:
        if buttons[0]:
            pygame.time.wait(100)
            if hcc != 0:  # 現在有格子被點選（變成藍色）
                pygame.time.wait(100)
                winC()  # 彈出輸入視窗
            else:
                error('尚未點選課程時間')
        else:
            window.blit(plc_2, (161, 43))
    else:
        window.blit(plc, (161, 43))
    
    # Home
    if 53 <= mouses[0] <= 252 and 655 <= mouses[1] <= 735:
        if buttons[0]:
            pygame.time.wait(100)
            page = 1  # 回到首頁
        else:
            window.blit(hm_2, (53, 655))
    else:
        window.blit(hm, (53, 655))
    
    # 顯示
    pygame.display.update()


def J2_r():
    """運算+結果"""
    global bglb_list, print_list, bgr_schedule, page, takecourse, compare, Csort_dict, Ssort_dict
    
    # 前置運算（演算法）
    if page == 3:  
        # 計算有多少讀書時間及課程時間
        study = 0                                                                                                                           # 計算使用者選多少讀書時間
        lecture = 0                                                                                                                         # 計算使用者選多少可選可不選的課（total）
        for b1 in range(3):
            for b2 in range(8):
                for b3 in range(7):
                    if bglb_list[b1][b2][b3][1] == '讀書':                                                                                  # 如果這一格名稱屬性是讀書，study+1
                        study += 1
                    elif bglb_list[b1][b2][b3][1] in Csort_dict and bglb_list[b1][b2][b3][0] == 3:                                          # 如果這一格名稱屬性是某個課程，且性質屬性是3（可選可不選的課），lecture+1
                        lecture += 1

        # 安排讀書科目的先後順序
        for b4 in range(study + lecture):                                                                                                   # 跑讀書和課程數加總次，每次都把存有全部課程效益的字典（Ssort_dict）由大到小排序
            orderS = sorted(zip(Ssort_dict.values(), Ssort_dict.keys()), reverse=True)
            compare.append([Ssort_dict[orderS[0][1]][0], orderS[0][1]])                                                                     # 選效益最大的課程（orderS的第一項）丟入compare清單中，包含目前效益和課程名稱
            Ssort_dict[orderS[0][1]][0] -= (0.1 + Ssort_dict[orderS[0][1]][5] * Ssort_dict[orderS[0][1]][4]) * Ssort_dict[orderS[0][1]][1]  # 把該課程對應的效益減去0.1+0.0※ * 已經讀的小時
            Ssort_dict[orderS[0][1]][4] += 1                                                                                                # 該課程讀的時間+1
            if Ssort_dict[orderS[0][1]][0] < 0:                                                                                             # 效益遞減後可能變負，變負要改成0
                Ssort_dict[orderS[0][1]][0] = 0

        # 決定要去上課還是讀書
        for b5 in subject:
            takecourse[b5] = 0                                                                                                              # 為每一個課程紀錄上了多少堂可選可不選的課，因為現在都還沒選，所以設0

        for b6 in range(lecture):                                                                                                           # 跑課程總數次，決定要去上課還是讀書
            orderC = sorted(zip(Csort_dict.values(), Csort_dict.keys()), reverse=True)                                                      # 把存有所有課程效益的字典（Csort_dict）由大到小排序
            if compare[-1][0] > orderC[0][0][0]:                                                                                            # compare的最後一項一定是效益最低的讀書，如果它還比效益最高的課堂大，就不用再比了（因為倒數第二的讀書又比最後一項優，第二大的課堂又比第一項差）
                break
            Ssort_dict[compare[-1][1]][0] = compare[-1][0]                                                                                  # 如果不讀這一科了，就要將效益改回提出時的效益（有種加回去的意味）
            Ssort_dict[compare[-1][1]][4] -= 1                                                                                              # 該課程少讀一小時，要將該課程讀書時數-1
            compare.remove(compare[-1])                                                                                                     # 將該課程（一定是compare的最後一項）從要讀的課程中移除
            takecourse[orderC[0][1]] += 1                                                                                                   #  上課效益最高的課+1，代表選了這堂課來上
            Csort_dict[orderC[0][1]][4] -= 1                                                                                                # 原先放上課效益的字典中有存該課可選可不選的課數，如果選了該課就把課數-1，以判斷該課是不是已經挑盡了
            if Csort_dict[orderC[0][1]][4] == 0:                                                                                            # 如果該課已被挑盡，就從字典中移除，下次排序時才不會有它
                del Csort_dict[orderC[0][1]]
        
        print_list = copy.deepcopy(bglb_list)
        for b7 in range(3):                                                                                                                 # 一格一格跑（168格total）
            for b8 in range(8):
                for b9 in range(7):
                    for b10 in takecourse:                                                                                                  # 每一格都去判斷是不是要上的課，如果是而且要上的課就是使用者選的數量（可選可不選的課全要上）那就改成一定要上（3:可上可不上，3.5:一定要上）
                        if bglb_list[b7][b8][b9][1] == b10 and takecourse[b10] == chooseclass[b10] and bglb_list[b7][b8][b9][0] == 3:
                            print_list[b7][b8][b9] = [3.5, b10]
                            break

        for b11 in takecourse:                                                                                                              # 同樣判斷要上的課就是使用者選的數量（可選可不選的課全要上），若是，剛剛就已經將它改成必上的課了，不用交由使用者裁決，所以把紀錄上幾堂的地方改成0
            if takecourse[b11] == chooseclass[b11]:
                takecourse[b11] = 0
        
        ok = 0                                                                                                                              # 是不是不用交由使用者裁決的變數
        for b12 in Csort_dict:
            if Csort_dict[b12][4] == chooseclass[b12]:                                                                                      # 若該課剩多少堂沒選=使用者當時選的可選可不選堂數，那就是一堂都不用上，所以ok+1，代表距離不用交由使用者裁決又更進一步囉
                ok += 1
        if ok != len(Csort_dict):                                                                                                           # 如果每一門課都是不用上or全都要上，就會直接跳到第5頁（結果頁），不然就要交給使用者決定要上的課放哪裡
            page = 4
        else:
            page = 5

    # 決定要讀課程的正確位置
    elif page == 5:
        breakP = []                                                                                                                         # 放入讀書時段長度的清單（包含時段起始位置）
        acc = 0                                                                                                                             # 記錄每個讀書時段的長度，不連續時就會歸0
        for b13 in range(7):                                                                                                                # 一格一格跑（168格total）
            for b14 in range(3):
                for b15 in range(8):
                    if b14 == 2 and b15 == 7 and print_list[b14][b15][b13][0] == 3:                                                         # 為避免換行仍連續計算時段，一行的最後如果有讀書時段就要自動切斷
                        acc += 1
                        breakP.append([acc, -1 * b14, -1 * (b15 - acc + 1), -1 * b13])
                        acc = 0                                                                                                             # 讀書時段歸0，重新計算
                    elif print_list[b14][b15][b13][0] == 3:                                                                                 # 3代表使用者當時選'讀書'or可選可不選最後確定不上的，可以讀書!小時數開始累積
                        acc += 1
                    elif print_list[b14][b15][b13][0] != 3 and acc != 0:                                                                    # 如果不是3那就要看剛剛有沒有累積讀書時段數，如果不為0就將累積結果放入breakP，為0則表示剛剛經過的都只是空格子
                        breakP.append([acc, -1 * b14, -1 * (b15 - acc), -1 * b13])
                        acc = 0                                                                                                             # 讀書時段歸0，重新計算
        breakP.sort()
        breakP.reverse()                                                                                                                    # 時段由長到短排序

        put_in = dict()                                                                                                                     # 要讀的科目最後確定讀多少小時的字典（記數用）
        for b16 in compare:                                                                                                                 # 把compare裡面所有科目分門別類當成keys（例如:可能跑演算法時第1、3、6、7、20高的效益都屬會計，那put_in[會計] = 4(hr)），
            if b16[1] not in put_in:
                put_in[b16[1]] = 1
            else:
                put_in[b16[1]] += 1
        put_list = []                                                                                                                       # put_in清單版
        for b17 in put_in:
            put_list.append([put_in[b17], b17])  # 把put_in放入put_lis中（小時數, 名稱）
        put_list.sort()
        put_list.reverse()                                                                                                                  # 各門課小時數由大到小排序
        
        # 將要讀課程放入正確位置
        for b18 in breakP:
            nextS = 0                                                                                                                       # 如果不合放入規則就換下一個（+1）
            def putclass(time):
                """放入讀書時間的函數"""
                if -8 <= -1 * b18[2] + time < 0:                                                                                            # 這是在處理跨頁的問題
                    print_list[-1 * b18[1] - 1][8 - b18[2] + time][-1 * b18[3]][0] = 5
                    print_list[-1 * b18[1] - 1][8 - b18[2] + tme][-1 * b18[3]][1] = put_list[nextS % len(put_list)][1]
                elif -1 * b18[2] + time < -8:                                                                                               # 這是在處理跨頁的問題
                    print_list[-1 * b18[1] - 2][16 - b18[2] + time][-1 * b18[3]][0] = 5
                    print_list[-1 * b18[1] - 2][16 - b18[2] + time][-1 * b18[3]][1] = put_list[nextS % len(put_list)][1]
                else:                                                                                                                       # 這是在處理跨頁的問題
                    print_list[-1 * b18[1]][-1 * b18[2] + time][-1 * b18[3]][0] = 5
                    print_list[-1 * b18[1]][-1 * b18[2] + time][-1 * b18[3]][1] = put_list[nextS % len(put_list)][1]

            while b18[0] != 0:                                                                                                              # 一個時段必須補到滿方能換下一個時段
                iftwo = 0                                                                                                                   # 判斷現在有沒有課程還要讀兩堂的變數，初設0
                ifthree = 0                                                                                                                 # 判斷現在有沒有課程還要讀大於等於三堂的變數，初設0
                for b19 in put_list:                                                                                                        # 每門課都去檢視是否有等於2or大於等於3小時要讀
                    if b19[0] == 2:
                        iftwo += 1
                    elif b19[0] >= 3:
                        ifthree += 1
                if b18[0] > 3:
                    if iftwo + ifthree != 0:                                                                                                # 時段大於3小時，有2or大於等於3小時的科目要讀，放2小時該科目給它
                        if put_list[nextS % len(put_list)][0] >= 2:
                            for b20 in range(2):
                                putclass(b20)
                            b18[0] -= 2                                                                                                     # 時段已經被填補兩堂，故減2
                            b18[2] -= 2                                                                                                     # 位置減2
                            put_list[nextS % len(put_list)][0] -= 2                                                                         # 相應的讀書科目已經讀了2小時，故減2
                    else:                                                                                                                   # 時段大於3小時，沒有2or大於等於3小時的科目要讀，放1小時科目給它
                        if put_list[nextS % len(put_list)][0] != 0:
                            putclass(0)
                            b18[0] -= 1                                                                                                     # 時段已經被填補一堂，故減1
                            b18[2] -= 1                                                                                                     # 位置減1
                            put_list[nextS % len(put_list)][0] -= 1                                                                         # 相應的讀書科目已經讀了1小時，故減1
                elif b18[0] == 3:
                    if ifthree != 0:                                                                                                        # 時段等於3小時，有大於等於3小時的科目要讀，放3小時該科目給它
                        if put_list[nextS % len(put_list)][0] >= 3:
                            for b21 in range(3):
                                putclass(b21)
                            b18[0] -= 3                                                                                                     # 時段已經被填補三堂，故減3
                            b18[2] -= 3                                                                                                     # 位置減3
                            put_list[nextS % len(put_list)][0] -= 3                                                                         # 相應的讀書科目已經讀了3小時，故減3
                    elif iftwo != 0:                                                                                                        # 時段等於3小時，要讀的科目最長只有2小時，放2小時該科目給它
                        if put_list[nextS % len(put_list)][0] == 2:
                            for b22 in range(2):
                                putclass(b22)
                            b18[0] -= 2                                                                                                     # 時段已經被填補兩堂，故減2
                            b18[2] -= 2                                                                                                     # 位置減2
                            put_list[nextS % len(put_list)][0] -= 2                                                                         # 相應的讀書科目已經讀了2小時，故減2
                    else:                                                                                                                   # 時段等於3小時，沒有2or大於等於3小時的科目要讀，放1小時科目給它
                        if put_list[nextS % len(put_list)][0] != 0:
                            putclass(0)
                            b18[0] -= 1                                                                                                     # 時段已經被填補一堂，故減1
                            b18[2] -= 1                                                                                                     # 位置減1
                            put_list[nextS % len(put_list)][0] -= 1                                                                         # 相應的讀書科目已經讀了1小時，故減1
                elif b18[0] == 2:
                    if iftwo + ifthree != 0:                                                                                                # 時段等於2小時，有2or大於等於3小時的科目要讀，放2小時該科目給它
                        if put_list[nextS % len(put_list)][0] >= 2:
                            for b23 in range(2):
                                putclass(b23)
                            b18[0] -= 2                                                                                                     # 時段已經被填補兩堂，故減2
                            b18[2] -= 2                                                                                                     # 位置減2
                            put_list[nextS % len(put_list)][0] -= 2                                                                         # 相應的讀書科目已經讀了2小時，故減2
                    else:                                                                                                                   # 時段等於2小時，沒有2or大於等於3小時的科目要讀，放1小時科目給它
                        if put_list[nextS % len(put_list)][0] != 0:
                            putclass(0)
                            b18[0] -= 1                                                                                                     # 時段已經被填補一堂，故減1
                            b18[2] -= 1                                                                                                     # 位置減1
                            put_list[nextS % len(put_list)][0] -= 1                                                                         # 相應的讀書科目已經讀了1小時，故減1
                elif b18[0] == 1:                                                                                                           # 時段等於1小時，放1小時科目給它
                    if put_list[nextS % len(put_list)][0] != 0:
                        putclass(0)
                        b18[0] -= 1                                                                                                         # 時段已經被填補一堂，故減1
                        b18[2] -= 1                                                                                                         # 位置減1
                        put_list[nextS % len(put_list)][0] -= 1                                                                             # 相應的讀書科目已經讀了1小時，故減1
                nextS += 1                                                                                                                  # 換下一門課程放，避免連續讀同一堂太久
        page = 6                                                                                                                            # 放完之後進入呈現結果頁面
    
    # 呈現結果頁面
    elif page == 6:
        # 滑鼠事件
        mouses = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()
        
        # 判斷要顯示表的第幾頁
        if bgr_schedule == 1:
            window.blit(bgr_1, (0, 0))  # 視窗蓋上表的第一頁（00:00-08:00）
        elif bgr_schedule == 2:
            window.blit(bgr_2, (0, 0))  # 視窗蓋上表的第二頁（08:00-16:00）
        elif bgr_schedule == 3:
            window.blit(bgr_3, (0, 0))  # 視窗蓋上表的第三頁（16:00-00:00）
        
        # 顯示日期
        orid = start  # 起始日期
        for b24 in range(7):
            pred = fontObj.render('{:^5s}'.format(str(orid.month) + '/' + str(orid.day)), True, (0, 0, 0))  # 日期
            prew = fontObj.render('{:^5s}'.format('（' + week[orid.weekday()] + '）'), True, (0, 0, 0))  # 星期幾
            x = datetime.timedelta(days=b24 + 1)
            orid = start + x  # 加一天
            window.blit(pred, (482 + 113 * b24, 81))
            window.blit(prew, (468 + 113 * b24, 110))
        
        # 切換表的頁面（上）
        if 1286 <= mouses[0] <= 1337 and 605 <= mouses[1] <= 656:
            if buttons[0]:
                if bgr_schedule == 2:
                    pygame.time.wait(100)
                    bgr_schedule = 1                
                elif bgr_schedule == 3:
                    pygame.time.wait(100)
                    bgr_schedule = 2
            else:
                window.blit(up_2, (1286, 605))
        else:
            window.blit(up, (1286, 605))
        
        # 切換表的頁面（下）
        if 1286 <= mouses[0] <= 1337 and 666 <= mouses[1] <= 717:
            if buttons[0]:
                if bgr_schedule == 1:
                    pygame.time.wait(100)
                    bgr_schedule = 2
                elif bgr_schedule == 2:
                    pygame.time.wait(100)
                    bgr_schedule = 3
            else:
                window.blit(down_2, (1286, 666))
        else:
            window.blit(down, (1286, 666))
        
        print_x = 0  # 第一格的x座標 - 465
        print_y = 0  # 第一格的y座標 - 145
        # 判斷格子狀態
        for b25 in range(8):
            for b26 in range(7):
                if print_list[bgr_schedule - 1][b25][b26][0] == 0:  # 狀態零為變淺灰色
                    window.blit(bglb_3, (465 + print_x, 145 + print_y))
                elif print_list[bgr_schedule - 1][b25][b26][0] == 3.5 or print_list[bgr_schedule - 1][b25][b26][0] == 4:  # 狀態三點五和四為變綠色+顯示課程名稱
                    window.blit(bglb_4, (465 + print_x, 145 + print_y))
                    prename = fontObj.render(print_list[bgr_schedule - 1][b25][b26][1] if len(print_list[bgr_schedule - 1][b25][b26][1]) <= 3 else print_list[bgr_schedule - 1][b25][b26][1][0:2] + '…', True, (0, 0, 0))
                    window.blit(prename, (475 + print_x, 160 + print_y))
                else:  # 狀態五為變粉紅色+顯示讀書科目名稱
                    window.blit(bglb_5, (465 + print_x, 145 + print_y))
                    prename = fontObj.render(print_list[bgr_schedule - 1][b25][b26][1] if len(print_list[bgr_schedule - 1][b25][b26][1]) <= 3 else print_list[bgr_schedule - 1][b25][b26][1][0:2] + '…', True, (0, 0, 0))
                    window.blit(prename, (475 + print_x, 160 + print_y))
                print_x += 113  # x座標向右位移113
            print_x = 0  # 一排7個畫滿後，x座標的位移量歸零
            print_y += 72  # 下移72，開始畫新的一排
        
        # Home
        if 53 <= mouses[0] <= 252 and 655 <= mouses[1] <= 735:
            if buttons[0]:
                pygame.time.wait(100)
                print_list = []
                compare = []
                takecourse = dict()
                Ssort_dict = dict()
                Csort_dict = dict()
                page = 1  # 回到首頁
            else:
                window.blit(hm_2, (53, 655))
        else:
            window.blit(hm, (53, 655))

        # 顯示
        pygame.display.update()
   
   
def J2_c():
    """選擇要出席的課"""
    global bgc_schedule, whichC, takecourse, print_list, subject, page
    mouses = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    # 判斷要顯示表的第幾頁
    if bgc_schedule == 1:
        window.blit(bgc_1, (0, 0))  # 視窗蓋上表的第一頁（00:00-08:00）
    elif bgc_schedule == 2:
        window.blit(bgc_2, (0, 0))  # 視窗蓋上表的第二頁（08:00-16:00）
    elif bgc_schedule == 3:
        window.blit(bgc_3, (0, 0))  # 視窗蓋上表的第三頁（16:00-00:00）
    window.blit(show, (34, 68))

    # 顯示日期
    orid = start  # 起始日期
    for d1 in range(7):
        pred = fontObj.render('{:^5s}'.format(str(orid.month) + '/' + str(orid.day)), True, (0, 0, 0))  # 日期
        prew = fontObj.render('{:^5s}'.format('（' + week[orid.weekday()] + '）'), True, (0, 0, 0))  # 星期幾
        x = datetime.timedelta(days=d1 + 1)
        orid = start + x  # 加一天
        window.blit(pred, (482 + 113 * d1, 81))
        window.blit(prew, (468 + 113 * d1, 110))
        
    # 切換表的頁面（上）
    if 1286 <= mouses[0] <= 1337 and 605 <= mouses[1] <= 656:
        if buttons[0]:
            if bgc_schedule == 2:
                pygame.time.wait(100)
                bgc_schedule = 1                
            elif bgc_schedule == 3:
                pygame.time.wait(100)
                bgc_schedule = 2
        else:
            window.blit(up_2, (1286, 605))
    else:
        window.blit(up, (1286, 605))
        
    # 切換表的頁面（下）
    if 1286 <= mouses[0] <= 1337 and 666 <= mouses[1] <= 717:
        if buttons[0]:
            if bgc_schedule == 1:
                pygame.time.wait(100)
                bgc_schedule = 2
            elif bgc_schedule == 2:
                pygame.time.wait(100)
                bgc_schedule = 3
        else:
            window.blit(down_2, (1286, 666))
    else:
        window.blit(down, (1286, 666))

    bglb_x = 0  # 第一格的x座標 - 465
    bglb_y = 0  # 第一格的y座標 - 145
    # 判斷格子狀態
    for d2 in range(8):
        for d3 in range(7):
            if 465 + bglb_x <= mouses[0] <= 550 + bglb_x and 145 + bglb_y <= mouses[1] <= 196 + bglb_y:
                if print_list[bgc_schedule - 1][d2][d3][0] != 3.5 and print_list[bgc_schedule - 1][d2][d3][0] != 4 and print_list[bgc_schedule - 1][d2][d3][1] != -1 and print_list[bgc_schedule - 1][d2][d3][1] != '讀書':
                    if buttons[0] and takecourse[print_list[bgc_schedule - 1][d2][d3][1]] != 0:  # 滑鼠在格子上、原本沒被點選、現在按滑鼠左鍵
                        pygame.time.wait(100)
                        print_list[bgc_schedule - 1][d2][d3][0] = 4  # 狀態四為變紫色
                        takecourse[print_list[bgc_schedule - 1][d2][d3][1]] -= 1
                    else:  # 滑鼠在格子上、原本沒被點選、現在沒按滑鼠
                        print_list[bgc_schedule - 1][d2][d3][0] = 1  # 狀態三點二五為變深灰色
                elif print_list[bgc_schedule - 1][d2][d3][0] == 4:
                    if buttons[0]:  # 滑鼠在格子上、原本被點選（沒課程）、現在按滑鼠
                        pygame.time.wait(100)
                        print_list[bgc_schedule - 1][d2][d3][0] = 3
                        takecourse[print_list[bgc_schedule - 1][d2][d3][1]] += 1
            if print_list[bgc_schedule - 1][d2][d3][0] == 1:  # 狀態一為變深灰色
                window.blit(bglb_2, (465 + bglb_x, 145 + bglb_y))
                print_list[bgc_schedule - 1][d2][d3][0] = 3  # 狀態零為變淺灰色
                prename = fontObj.render(print_list[bgc_schedule - 1][d2][d3][1] if len(print_list[bgc_schedule - 1][d2][d3][1]) <= 3 else print_list[bgc_schedule - 1][d2][d3][1][0:2] + '…', True, (0, 0, 0))
                window.blit(prename, (475 + bglb_x, 160 + bglb_y))
            elif print_list[bgc_schedule - 1][d2][d3][0] == 4:
                window.blit(bglb_8, (465 + bglb_x, 145 + bglb_y))
                prename = fontObj.render(print_list[bgc_schedule - 1][d2][d3][1] if len(print_list[bgc_schedule - 1][d2][d3][1]) <= 3 else print_list[bgc_schedule - 1][d2][d3][1][0:2] + '…', True, (0, 0, 0))
                window.blit(prename, (475 + bglb_x, 160 + bglb_y))
            elif print_list[bgc_schedule - 1][d2][d3][0] == 0:  # 狀態零為變淺灰色
                window.blit(bglb_3, (465 + bglb_x, 145 + bglb_y))
            elif print_list[bgc_schedule - 1][d2][d3][0] == 3 and print_list[bgc_schedule - 1][d2][d3][1] != '讀書':  # 狀態三為變藍色+顯示課程名稱
                window.blit(bglb_3, (465 + bglb_x, 145 + bglb_y))
                prename = fontObj.render(print_list[bgc_schedule - 1][d2][d3][1] if len(print_list[bgc_schedule - 1][d2][d3][1]) <= 3 else print_list[bgc_schedule - 1][d2][d3][1][0:2] + '…', True, (0, 0, 0))
                window.blit(prename, (475 + bglb_x, 160 + bglb_y))
            elif print_list[bgc_schedule - 1][d2][d3][1] == '讀書' or print_list[bgc_schedule - 1][d2][d3][0] == 3.5:  # 狀態三為變藍色+顯示課程名稱
                window.blit(bglb_7, (465 + bglb_x, 145 + bglb_y))
                prename = fontObj.render(print_list[bgc_schedule - 1][d2][d3][1] if len(print_list[bgc_schedule - 1][d2][d3][1]) <= 3 else print_list[bgc_schedule - 1][d2][d3][1][0:2] + '…', True, (0, 0, 0))
                window.blit(prename, (475 + bglb_x, 160 + bglb_y))
            bglb_x += 113  # x座標向右位移113
        bglb_x = 0  # 一排7個畫滿後，x座標的位移量歸零
        bglb_y += 72  # 下移72，開始畫新的一排

    # 切換課程資訊頁面（左）
    if 221 <= mouses[0] <= 238 and 34 <= mouses[1] <= 51:
        if buttons[0]:
            if whichC != 0:    # 如果不在第一頁
                pygame.time.wait(100)
                whichC -= 1
        else:
            window.blit(left_2, (221, 34))
    else:
        window.blit(left, (221, 34))
    
    # 切換課程資訊頁面（右）
    if 246 <= mouses[0] <= 263 and 34 <= mouses[1] <= 51:
        if buttons[0]:
            if whichC != ((len(subject) - 1) // 4) if (len(subject) - 1) // 4 >= 0 else 0:  # 如果不在最後一頁
                pygame.time.wait(100)
                whichC += 1
        else:
            window.blit(right_2, (246, 34))
    else:
        window.blit(right, (246, 34))

    # 課程資訊呈現
    presubj = list(subject.values())
    a = len(subject) - ((len(subject) - 1) // 4) * 4  # 一個頁面通常有4堂課的課程資訊，但最後一頁可能不足4個
    for d4 in range(4 if whichC != ((len(subject) - 1) // 4) else a):
        if len(presubj[whichC * 4 + d4]) > 9:
            info1 = fontObjS.render('課程名稱：%s' % (presubj[whichC * 4 + d4][0:8] + '…'), True, (0, 0, 0))  # 課程名稱超過8個字會被省略
        else:
            info1 = fontObjS.render('課程名稱：%s' % (presubj[whichC * 4 + d4]), True, (0, 0, 0))
        info2 = fontObjS.render('尚有 %s 節課要選' % str(takecourse[presubj[whichC * 4 + d4]]), True, (0, 0, 0)) 
        window.blit(info1, (40, 96 + d4 * 85))  # 將資訊置於正確的位置
        window.blit(info2, (40, 111 + d4 * 85))
    
    # Home
    if 53 <= mouses[0] <= 252 and 655 <= mouses[1] <= 735:
        if buttons[0]:
            pygame.time.wait(100)
            print_list = []
            compare = []
            takecourse = dict()
            Ssort_dict = dict()
            Csort_dict = dict()
            page = 1  # 回到首頁
        else:
            window.blit(hm_2, (53, 655))
    else:
        window.blit(hm, (53, 655))

    # Next
    if 53 <= mouses[0] <= 252 and 575 <= mouses[1] <= 655:
        if buttons[0]:
            pygame.time.wait(100)
            page = 5  # 顯示結果頁面
        else:
            window.blit(nx_2, (53, 575))
    else:
        window.blit(nx, (53, 575))

    # 顯示
    pygame.display.update()


def error(what):
    """錯誤警告視窗"""
    windowE = tk.Tk()
    windowE.wm_attributes('-topmost',1)  # 視窗移至最上層
    windowE.title('Error')
    windowE.grid()
    er = tk.Label(windowE, text=what, anchor='w')
    er.grid(row=0, column=0, padx=40, pady=20)
    windowE.mainloop()


def winC():
    """輸入課程資訊視窗"""
    
    def winC_get():
        """取得輸入資訊"""
        rename = nameE.get()
        try:
            recredit = int(creditE.get())
            repercent = percentE.get()
            if 0 <= float(repercent) <= 100:  # 判斷考試成績占總成績百分比有無介於0到100之間
                repercent = float(repercent)
            else:
                repercent = int('None')
            reutil = utilv.get()
            reutil = reutil.strip('()')
            reutil = reutil.replace("'", '')
            reutil = reutil.split(', ')
            reutils = utilsv.get()
            reutils = reutils.strip('()')
            reutils = reutils.replace("'", '')
            reutils = reutils.split(', ')
            if rename not in subject:
                subject[rename] = rename
                classcredit[rename] = recredit
                percentage[rename] = repercent
                classutility[rename] = reutil
                efficiency[rename] = reutils
                chooseclass[rename] = 0
                neverskipclass[rename] = 0
            else:
                classcredit[rename] = recredit
                percentage[rename] = repercent
                classutility[rename] = reutil
                efficiency[rename] = reutils
            for c1 in range(3):
                for c2 in range(8):
                    for c3 in range(7):
                        if bglb_list[c1][c2][c3][0] == 2:
                            bglb_list[c1][c2][c3] = [3, rename]
                            chooseclass[rename] += 1
                        elif bglb_list[c1][c2][c3][0] == 2.5:
                            bglb_list[c1][c2][c3] = [3.5, rename]
                            neverskipclass[rename] += 1
            windowC.destroy()
        except:
            error('輸入錯誤')

    windowC = tk.Tk()
    windowC.wm_attributes('-topmost',1)
    windowC.title('課程輸入')
    windowC.grid()
    name = tk.Label(windowC, text='課程名稱', anchor='w')
    name.grid(row=0, column=0, sticky='w')
    nameE = tk.Entry(windowC, bd =5)
    nameE.grid(row=0, column=1, sticky='w', columnspan=5)
    credit = tk.Label(windowC, text='學分數', anchor='w')
    credit.grid(row=1, column=0, sticky='w')
    creditE = tk.Entry(windowC, bd =5)
    creditE.grid(row=1, column=1, sticky='w', columnspan=5)
    percent = tk.Label(windowC, text='本次考試占學期成績比例（％）', anchor='w')
    percent.grid(row=2, column=0, sticky='w')
    percentE = tk.Entry(windowC, bd =5)
    percentE.grid(row=2, column=1, sticky='w', columnspan=5)
    util = tk.Label(windowC, text='上課效益', anchor='w')
    util.grid(row=3, column=0, sticky='w')
    utilv = tk.StringVar()
    utilv.set([4, 0.04, '很低'])
    tk.Radiobutton(windowC, variable=utilv, text='很低', value=[4, 0.04, '很低']).grid(row=3, column=1, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='低', value=[4.5, 0.04, '低']).grid(row=3, column=2, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='中', value=[5, 0.03, '中']).grid(row=3, column=3, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='高', value=[5.5, 0.02, '高']).grid(row=3, column=4, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='很高', value=[6, 0.02, '很高']).grid(row=3, column=5, sticky='w')
    utils = tk.Label(windowC, text='自己讀的吸收度', anchor='w')
    utils.grid(row=4, column=0, sticky='w')    
    utilsv = tk.StringVar()
    utilsv.set([4, 0.04, '很低'])
    tk.Radiobutton(windowC, variable=utilsv, text='很低', value=[4, 0.04, '很低']).grid(row=4, column=1, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='低', value=[4.5, 0.04, '低']).grid(row=4, column=2, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='中', value=[5, 0.03, '中']).grid(row=4, column=3, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='高', value=[5.5, 0.02, '高']).grid(row=4, column=4, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='很高', value=[6, 0.02, '很高']).grid(row=4, column=5, sticky='w')
    sentb = tk.Button(windowC, text='確定送出', command=winC_get)
    sentb.grid(row=5, column=0, pady = 20, columnspan=6)
    windowC.mainloop()


def winD():
    """輸入起始日期視窗"""
    
    def winD_get():
        """取得輸入資訊"""
        global page, start
        reyear = yearE.get()
        remonth = monthE.get()
        reday = dayE.get()
        try:  # 判斷是否為有效日期
            start = datetime.datetime(int(reyear), int(remonth), int(reday))
            page = 2
            windowD.destroy()
        except:
            error('此日期無效')

    windowD = tk.Tk()
    windowD.wm_attributes('-topmost',1)
    windowD.title('輸入起始日期')
    windowD.grid()
    date = tk.Label(windowD, text='請輸入週計畫的起始日期', anchor='w')
    date.grid(row=0, column=0, columnspan=7)
    ad = tk.Label(windowD, text='西元', anchor='w')
    ad.grid(row=1, column=0, sticky='w')
    yearE = tk.Entry(windowD, bd =5, width=6)
    yearE.grid(row=1, column=1, sticky='w')
    year = tk.Label(windowD, text='年', anchor='w')
    year.grid(row=1, column=2, sticky='w')
    monthE = tk.Entry(windowD, bd =5, width=6)
    monthE.grid(row=1, column=3, sticky='w')
    month = tk.Label(windowD, text='月', anchor='w')
    month.grid(row=1, column=4, sticky='w')
    dayE = tk.Entry(windowD, bd =5, width=6)
    dayE.grid(row=1, column=5, sticky='w')
    day = tk.Label(windowD, text='日', anchor='w')
    day.grid(row=1, column=6, sticky='w')
    sentb = tk.Button(windowD, text='確定送出', command=winD_get)
    sentb.grid(row=7, column=0, columnspan=7, pady=20)
    windowD.mainloop()


def correct(rename01):
    """修改課程資訊視窗"""
    
    def correct_get():
        """取得輸入資訊"""
        try:
            recredit = int(creditE.get())
            repercent = percentE.get()
            if 0 <= float(repercent) <= 100:  # 判斷考試成績占總成績百分比有無介於0到100之間
                repercent = float(repercent)
            else:
                repercent = int('None')
            reutil = utilv.get()
            reutil = reutil.strip('()')
            reutil = reutil.replace("'", '')
            reutil = reutil.split(', ')
            reutils = utilsv.get()
            reutils = reutils.strip('()')
            reutils = reutils.replace("'", '')
            reutils = reutils.split(', ')
            classcredit[rename01] = recredit
            percentage[rename01] = repercent
            classutility[rename01] = reutil
            efficiency[rename01] = reutils
            windowR.destroy()
        except:
            error('輸入無效')

    windowR = tk.Tk()
    windowR.wm_attributes('-topmost',1)
    windowR.title('課程修正')
    windowR.grid()
    name = tk.Label(windowR, text='課程名稱', anchor='w')
    name.grid(row=0, column=0, sticky='w')
    nameE = tk.Label(windowR, text=rename01, anchor='w')
    nameE.grid(row=0, column=1, columnspan=5, sticky='w')
    credit = tk.Label(windowR, text='學分數', anchor='w')
    credit.grid(row=1, column=0, sticky='w')
    creditE = tk.Entry(windowR, bd =5)
    creditE.grid(row=1, column=1, columnspan=5, sticky='w')
    percent = tk.Label(windowR, text='本次考試占學期成績比例（％）', anchor='w')
    percent.grid(row=2, column=0, sticky='w')
    percentE = tk.Entry(windowR, bd =5)
    percentE.grid(row=2, column=1, columnspan=5, sticky='w')
    util = tk.Label(windowR, text='上課效益', anchor='w')
    util.grid(row=3, column=0, sticky='w')    
    utilv = tk.StringVar()
    utilv.set([4, 0.04, '很低'])
    tk.Radiobutton(windowR, variable=utilv, text='很低', value=[4, 0.04, '很低']).grid(row=3, column=1, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='低', value=[4.5, 0.04, '低']).grid(row=3, column=2, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='中', value=[5, 0.03, '中']).grid(row=3, column=3, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='高', value=[5.5, 0.02, '高']).grid(row=3, column=4, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='很高', value=[6, 0.02, '很高']).grid(row=3, column=5, sticky='w')
    utils = tk.Label(windowR, text='自己讀的吸收度', anchor='w')
    utils.grid(row=4, column=0, sticky='w')    
    utilsv = tk.StringVar()
    utilsv.set([4, 0.04, '很低'])
    tk.Radiobutton(windowR, variable=utilsv, text='很低', value=[4, 0.04, '很低']).grid(row=4, column=1, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='低', value=[4.5, 0.04, '低']).grid(row=4, column=2, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='中', value=[5, 0.03, '中']).grid(row=4, column=3, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='高', value=[5.5, 0.02, '高']).grid(row=4, column=4, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='很高', value=[6, 0.02, '很高']).grid(row=4, column=5, sticky='w')
    sentb = tk.Button(windowR, text='確定送出', command=correct_get)
    sentb.grid(row=5, column=0, pady = 20, columnspan=6)
    windowR.mainloop()


"""主程式"""
week = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日'}  # 星期幾對照表
fontObj = pygame.font.Font('C:\\Users\\User\\AppData\\Local\\Microsoft\\Windows\\Fonts\\setofont.ttf', 21)  # 字體（大）
fontObjS = pygame.font.Font('C:\\Users\\User\\AppData\\Local\\Microsoft\\Windows\\Fonts\\setofont.ttf', 14)  # 字體（小）
# 格子資訊（狀態 + 應該顯示的字）
bglb_list = [[[[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]],\
[[[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]],\
[[[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]]]
page = 1  # 起始為首頁
bgl_schedule = 1  # 表格一開始呈現第一頁
bgr_schedule = 1
bgc_schedule = 1
which = 0  # 課程資訊一開始呈現第一頁
whichC = 0
start = None  # 起始日期
operate = True
subject = dict()
classcredit = dict()
percentage = dict()
classutility = dict()
efficiency = dict()
chooseclass = dict()
neverskipclass = dict()
preference = dict()
Ssort_dict = dict()
Csort_dict = dict()
compare = []
takecourse = dict()
improve = 0
print_list = []
while operate:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            operate = False
    if page == 1:
        J1()
    elif page == 2:
        J2_l()
    elif page == 3 or page == 5 or page == 6:
        J2_r()
    elif page == 4:
        J2_c()
pygame.quit()  # 關閉視窗