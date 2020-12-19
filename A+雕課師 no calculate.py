# -*- coding: UTF-8 -*-
# 引入pygame、tkinter、datetime、math與初始化
import pygame
import tkinter as tk
from tkinter import ttk
import datetime
import math
pygame.init()
pygame.mixer.init()  # 將混音器初始化

# 設定視窗
window = pygame.display.set_mode((1360, 765))  # 輸入視窗大小（1360*765）
pygame.display.set_caption('A+雕課師')  # 為視窗命名

# 呈現loading畫面
load = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\load.png')  # 引入loading畫面
load.convert_alpha()  # 畫入loading圖檔
load = pygame.transform.smoothscale(load, (1360, 765))  # 長寬設成1360*765（視窗大小）
window.blit(load, (0, 0))  # 設定loading圖檔位置為(0, 0)
pygame.display.update()  # 顯示

# 載入所有圖片
bg = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bg.png')  # 引入首頁背景
bg.convert_alpha()  # 畫入首頁圖檔
bg = pygame.transform.smoothscale(bg, (1360, 765))  # 長寬設成1360*765（視窗大小）

sp1 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\sp1.png')  # 引入步驟一按鈕（沒陰影）
sp1.convert_alpha()  # 畫入步驟一按鈕（沒陰影）圖檔
sp1 = pygame.transform.smoothscale(sp1, (340, 425))  # 長寬設成340*425

sp1_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\sp1-2.png')  # 引入步驟一按鈕（有陰影）
sp1_2.convert_alpha()  # 畫入步驟一按鈕（有陰影）圖檔
sp1_2 = pygame.transform.smoothscale(sp1_2, (340, 425))  # 長寬設成340*425

sp2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\sp2.png')  # 引入步驟二按鈕（沒陰影）
sp2.convert_alpha()  # 畫入步驟二按鈕（沒陰影）圖檔
sp2 = pygame.transform.smoothscale(sp2, (340, 425))  # 長寬設成340*425

sp2_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\sp2-2.png')  # 引入步驟二按鈕（有陰影）
sp2_2.convert_alpha()  # 畫入步驟二按鈕（有陰影）圖檔
sp2_2 = pygame.transform.smoothscale(sp2_2, (340, 425))  # 長寬設成340*425

ab = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\ab.png')  # 引入about按鈕（白色）
ab.convert_alpha()  # 畫入about按鈕（白色）圖檔
ab = pygame.transform.smoothscale(ab, (200, 80))  # 長寬設成200*80

ab_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\ab-2.png')  # 引入about按鈕（黑色）
ab_2.convert_alpha()  # 畫入about按鈕（黑色）圖檔
ab_2 = pygame.transform.smoothscale(ab_2, (200, 80))  # 長寬設成200*80

hm = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\hm.png')  # 引入home鍵（白色）（按下會回到首頁）
hm.convert_alpha()  # 畫入home鍵（白色）圖檔
hm = pygame.transform.smoothscale(hm, (200, 80))  # 長寬設成200*80

hm_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\hm-2.png')  # 引入home鍵（黑色）（按下會回到首頁）
hm_2.convert_alpha()  # 畫入home鍵（黑色）圖檔
hm_2 = pygame.transform.smoothscale(hm_2, (200, 80))  # 長寬設成200*80

bgl_1 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bgl-1.png')  # 引入課表00:00-08:00
bgl_1.convert_alpha()  # 畫入課表00:00-08:00圖檔
bgl_1 = pygame.transform.smoothscale(bgl_1, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgl_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bgl-2.png')  # 引入課表08:00-16:00
bgl_2.convert_alpha()  # 畫入課表08:00-16:00圖檔
bgl_2 = pygame.transform.smoothscale(bgl_2, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgl_3 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bgl-3.png')  # 引入課表16:00-00:00
bgl_3.convert_alpha()  # 畫入課表16:00-00:00圖檔
bgl_3 = pygame.transform.smoothscale(bgl_3, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgr_1 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bgr-1.png')  # 引入課表結果00:00-08:00
bgr_1.convert_alpha()  # 畫入課表結果00:00-08:00圖檔
bgr_1 = pygame.transform.smoothscale(bgr_1, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgr_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bgr-2.png')  # 引入課表結果08:00-16:00
bgr_2.convert_alpha()  # 畫入課表結果08:00-16:00圖檔
bgr_2 = pygame.transform.smoothscale(bgr_2, (1360, 765))  # 長寬設成1360*765（視窗大小）

bgr_3 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bgr-3.png')  # 引入課表結果16:00-00:00
bgr_3.convert_alpha()  # 畫入課表結果16:00-00:00圖檔
bgr_3 = pygame.transform.smoothscale(bgr_3, (1360, 765))  # 長寬設成1360*765（視窗大小）

bglb = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bglb.png')  # 引入藍色方塊（點選的時段呈藍色）
bglb.convert_alpha()  # 畫入藍色方塊圖檔
bglb = pygame.transform.smoothscale(bglb, (85, 51))  # 長寬設成85*51

bglb_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bglb-2.png')  # 引入深灰色方塊（滑過的時段呈深灰色）
bglb_2.convert_alpha()  # 畫入深灰色方塊圖檔
bglb_2 = pygame.transform.smoothscale(bglb_2, (85, 51))  # 長寬設成85*51

bglb_3 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bglb-3.png')  # 引入淺灰色方塊（沒有任何指令時呈淺灰色）
bglb_3.convert_alpha()  # 畫入淺灰色方塊圖檔
bglb_3 = pygame.transform.smoothscale(bglb_3, (85, 51))  # 長寬設成85*51

bglb_4 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bglb-4.png')  # 引入綠色方塊（上課呈綠色）
bglb_4.convert_alpha()  # 畫入綠色方塊圖檔
bglb_4 = pygame.transform.smoothscale(bglb_4, (85, 51))  # 長寬設成85*51

bglb_5 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\bglb-5.png')  # 引入粉紅色方塊（讀書呈粉紅色）
bglb_5.convert_alpha()  # 畫入粉紅色方塊圖檔
bglb_5 = pygame.transform.smoothscale(bglb_5, (85, 51))  # 長寬設成85*51

up = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\up.png')  # 引入向上按鈕（咖啡色）（可以回到上一頁課表）
up.convert_alpha()  # 畫入向上按鈕（咖啡色）圖檔
up = pygame.transform.smoothscale(up, (51, 51))  # 長寬設成51*51

up_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\up-2.png')  # 引入向上按鈕（白色）（按下按鈕時變白色）
up_2.convert_alpha()  # 畫入向上按鈕（白色）圖檔
up_2 = pygame.transform.smoothscale(up_2, (51, 51))  # 長寬設成51*51

down = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\down.png')  # 引入向下按鈕（咖啡色）（可以到下一頁課表）
down.convert_alpha()  # 畫入向下按鈕（咖啡色）圖檔
down = pygame.transform.smoothscale(down, (51, 51))  # 長寬設成51*51

down_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\down-2.png')  # 引入向下按鈕（白色）（按下按鈕時變白色）
down_2.convert_alpha()  # 畫入向下按鈕（白色）圖檔
down_2 = pygame.transform.smoothscale(down_2, (51, 51))  # 長寬設成51*51

pls = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\pls.png')  # 引入「標記為讀書時間」按鈕（咖啡色）
pls.convert_alpha()  # 畫入「標記為讀書時間」按鈕（咖啡色）圖檔
pls = pygame.transform.smoothscale(pls, (102, 51))  # 長寬設成102*51

pls_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\pls-2.png')  # 引入「標記為讀書時間」按鈕（白色）
pls_2.convert_alpha()  # 畫入「標記為讀書時間」按鈕（白色）圖檔
pls_2 = pygame.transform.smoothscale(pls_2, (102, 51))  # 長寬設成102*51

plc = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\plc.png')  # 引入「加入課程」按鈕（咖啡色）
plc.convert_alpha()  # 畫入「加入課程」按鈕（咖啡色）圖檔
plc = pygame.transform.smoothscale(plc, (102, 51))  # 長寬設成102*51

plc_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\plc-2.png')  # 引入「加入課程」按鈕（白色）
plc_2.convert_alpha()  # 畫入「加入課程」按鈕（白色）圖檔
plc_2 = pygame.transform.smoothscale(plc_2, (102, 51))  # 長寬設成102*51

show = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\show.png')  # 引入課程資訊顯示框
show.convert_alpha()  # 畫入課程資訊顯示框圖檔
show = pygame.transform.smoothscale(show, (221, 476))  # 長寬設成221*476

left = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\left.png')  # 引入向左按鈕（咖啡色）（可以回到上一頁課程資訊）
left.convert_alpha()  # 畫入向左按鈕（咖啡色）圖檔
left = pygame.transform.smoothscale(left, (17, 17))  # 長寬設成17*17

left_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\left-2.png')  # 引入向左按鈕（白色）（按下按鈕時變白色）
left_2.convert_alpha()  # 畫入向左按鈕（白色）圖檔
left_2 = pygame.transform.smoothscale(left_2, (17, 17))  # 長寬設成17*17

right = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\right.png')  # 引入向右按鈕（咖啡色）（可以到下一頁課程資訊）
right.convert_alpha()  # 畫入向右按鈕（咖啡色）圖檔
right = pygame.transform.smoothscale(right, (17, 17))  # 長寬設成17*17

right_2 = pygame.image.load('C:\\Users\\User\\Desktop\\A+雕課師\\right-2.png')  # 引入向右按鈕（白色）（按下按鈕時變白色）
right_2.convert_alpha()  # 畫入向右按鈕（白色）圖檔
right_2 = pygame.transform.smoothscale(right_2, (17, 17))  # 長寬設成17*17

# 定義函數
def J1():
    """首頁"""
    global page, subj
    mouses = pygame.mouse.get_pos()  # 追蹤滑鼠位置
    buttons = pygame.mouse.get_pressed()  # 偵測滑鼠有沒有被按下及如何被按下
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
            if subj != {}:
                winP()
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
                if bglb_list[a1][a2][a3][0] == 2:
                    hcc += 1
    
    # 如果現在所在資訊頁面超過頁面數（因為刪除了原本加入的課程，以至於最後一頁不見），就會退到上一頁
    if which > (len(subj) - 1) // 4 :
        which = (len(subj) - 1) // 4 if (len(subj) - 1) // 4 >= 0 else 0
    
    # 課程資訊呈現
    presubj = list(subj.values())  # 先把所有課程資訊（字典subj的值）提出來成為一個清單
    if subj != {}:
        a = len(subj) - ((len(subj) - 1) // 4) * 4  # 一個頁面通常有4堂課的課程資訊，但最後一頁可能不足4個
        for a4 in range(4 if which != ((len(subj) - 1) // 4) else a):
            if len(presubj[which * 4 + a4][0]) > 9:
                info1 = fontObjS.render('課程名稱：%s' % (presubj[which * 4 + a4][0][0:8] + '…'), True, (0, 0, 0))  # 課程名稱超過8個字會被省略
            else:
                info1 = fontObjS.render('課程名稱：%s' % (presubj[which * 4 + a4][0]), True, (0, 0, 0))
            info2 = fontObjS.render('學分數：%s' % str(presubj[which * 4 + a4][1]), True, (0, 0, 0)) 
            info3 = fontObjS.render('本次考試占總成績比例：%s %s' % (str(presubj[which * 4 + a4][2]), '%'), True, (0, 0, 0))
            info4 = fontObjS.render('裸考預期分數：%s' % str(presubj[which * 4 + a4][3]), True, (0, 0, 0))
            info5 = fontObjS.render('上課效益：%s' % str(presubj[which * 4 + a4][4][2]), True, (0, 0, 0))
            info6 = fontObjS.render('自己讀的吸收度：%s' % str(presubj[which * 4 + a4][5][2]), True, (0, 0, 0))
            info7 = fontObjS.render('一定要出席：%s' % (presubj[which * 4 + a4][6]), True, (0, 0, 0))
            window.blit(info1, (40, 160 + a4 * 119))  # 將資訊置於正確的位置
            window.blit(info2, (40, 175 + a4 * 119))
            window.blit(info3, (40, 190 + a4 * 119))
            window.blit(info4, (40, 205 + a4 * 119))
            window.blit(info5, (40, 220 + a4 * 119))
            window.blit(info6, (40, 235 + a4 * 119))
            window.blit(info7, (40, 250 + a4 * 119))
            # 判斷該課程資訊有無被點擊，若有（且沒有點選任何新的時段）則跳出修改課程的視窗
            if 34 <= mouses[0] <= 255 and 153 + a4 * 119 <= mouses[1] <= 272 + a4 * 119 and buttons[0]:
                if hcc == 0:
                    pygame.time.wait(100)
                    correct(presubj[which * 4 + a4][0])
                else:
                    error('尚有格子被點選')  # 彈出錯誤警告視窗
    
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
                if bglb_list[bgl_schedule - 1][a6][a7][0] != 2 and bglb_list[bgl_schedule - 1][a6][a7][0] != 3:
                    if buttons[0]:  # 滑鼠在格子上、原本沒被點選、現在按滑鼠
                        pygame.time.wait(100)
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 2  # 狀態二為變藍色
                    else:  # 滑鼠在格子上、原本沒被點選、現在沒按滑鼠
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 1  # 狀態一為變深灰色
                elif bglb_list[bgl_schedule - 1][a6][a7][0] == 2:
                    if buttons[0]:  # 滑鼠在格子上、原本被點選（沒課程）、現在按滑鼠
                        pygame.time.wait(100)
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 1
                elif bglb_list[bgl_schedule - 1][a6][a7][0] == 3:
                    if buttons[0]:  # 滑鼠在格子上、原本被點選（有課程）、現在按滑鼠
                        pygame.time.wait(100)
                        bglb_list[bgl_schedule - 1][a6][a7][0] = 1
                        if bglb_list[bgl_schedule - 1][a6][a7][1] != '讀書':  # 若不是讀書，要將該課程的總堂數減一，該課程的格子已經被刪光時要將該課程從字典中移除
                            subj[bglb_list[bgl_schedule - 1][a6][a7][1]][7] -= 1
                            if subj[bglb_list[bgl_schedule - 1][a6][a7][1]][7] == 0:
                                del subj[bglb_list[bgl_schedule - 1][a6][a7][1]]
                        bglb_list[bgl_schedule - 1][a6][a7][1] = -1
            if bglb_list[bgl_schedule - 1][a6][a7][0] == 1:  # 狀態一為變深灰色
                window.blit(bglb_2, (465 + bglb_x, 145 + bglb_y))
                bglb_list[bgl_schedule - 1][a6][a7][0] = 0  # 狀態零為變淺灰色
            elif bglb_list[bgl_schedule - 1][a6][a7][0] == 2:  # 狀態二為變藍色
                window.blit(bglb, (465 + bglb_x, 145 + bglb_y))
            elif bglb_list[bgl_schedule - 1][a6][a7][0] == 0:  # 狀態零為變淺灰色
                window.blit(bglb_3, (465 + bglb_x, 145 + bglb_y))
            else:  # 狀態三為變藍色+顯示課程名稱
                window.blit(bglb, (465 + bglb_x, 145 + bglb_y))
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
            if which != ((len(subj) - 1) // 4) if (len(subj) - 1) // 4 >= 0 else 0:  # 如果不在最後一頁
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
            for a8 in range(3):
                for a9 in range(8):
                    for a10 in range(7):
                        if bglb_list[a8][a9][a10][0] == 2:
                            bglb_list[a8][a9][a10] = [3, '讀書']
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

    # 運算

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
            reblind = blindE.get()
            if 0 < float(repercent) <= 100:  # 判斷考試成績占總成績百分比有無介於0到100之間
                repercent = float(repercent)
            else:
                repercent = int('None')
            reblind = float(reblind)
            reutil = utilv.get()
            reutil = reutil.strip('()')
            reutil = reutil.replace("'", '')
            reutil = reutil.split(', ')
            reutils = utilsv.get()
            reutils = reutils.strip('()')
            reutils = reutils.replace("'", '')
            reutils = reutils.split(', ')
            reskip = skipv.get()
            if rename not in subj:
                subj[rename] = [rename, recredit, repercent, reblind, reutil, reutils, reskip, 0]  # 最後一項為屬於這門課的格子數
            else:
                subj[rename][1:7] = [recredit, repercent, reblind, reutil, reutils, reskip]
            for c1 in range(3):
                for c2 in range(8):
                    for c3 in range(7):
                        if bglb_list[c1][c2][c3][0] == 2:
                            bglb_list[c1][c2][c3] = [3, rename]
                            subj[rename][7] += 1
            windowC.destroy()
        except:
            error('輸入無效')

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
    blind = tk.Label(windowC, text='裸考預期分數', anchor='w')
    blind.grid(row=3, column=0, sticky='w')
    blindE = tk.Entry(windowC, bd =5)
    blindE.grid(row=3, column=1, sticky='w', columnspan=5)
    util = tk.Label(windowC, text='上課效益', anchor='w')
    util.grid(row=4, column=0, sticky='w')
    utilv = tk.StringVar()
    utilv.set('很低')
    tk.Radiobutton(windowC, variable=utilv, text='很低', value=[4, 0.04, '很低']).grid(row=4, column=1, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='低', value=[4.5, 0.04, '低']).grid(row=4, column=2, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='中', value=[5, 0.03, '中']).grid(row=4, column=3, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='高', value=[5.5, 0.02, '高']).grid(row=4, column=4, sticky='w')
    tk.Radiobutton(windowC, variable=utilv, text='很高', value=[6, 0.02, '很高']).grid(row=4, column=5, sticky='w')
    utils = tk.Label(windowC, text='自己讀的吸收度', anchor='w')
    utils.grid(row=5, column=0, sticky='w')    
    utilsv = tk.StringVar()
    utilsv.set('很低')
    tk.Radiobutton(windowC, variable=utilsv, text='很低', value=[4, 0.04, '很低']).grid(row=5, column=1, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='低', value=[4.5, 0.04, '低']).grid(row=5, column=2, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='中', value=[5, 0.03, '中']).grid(row=5, column=3, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='高', value=[5.5, 0.02, '高']).grid(row=5, column=4, sticky='w')
    tk.Radiobutton(windowC, variable=utilsv, text='很高', value=[6, 0.02, '很高']).grid(row=5, column=5, sticky='w')
    skip = tk.Label(windowC, text='一定要出席', anchor='w')
    skip.grid(row=6, column=0, sticky='w')
    skipv = tk.StringVar()
    skipv.set('是')
    tk.Radiobutton(windowC, variable=skipv, text='是', value='是').grid(row=6, column=1, sticky='w')
    tk.Radiobutton(windowC, variable=skipv, text='否', value='否').grid(row=6, column=2, sticky='w')
    sentb = tk.Button(windowC, text='確定送出', command=winC_get)
    sentb.grid(row=7, column=0, pady = 20, columnspan=6)
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
            reblind = blindE.get()
            if 0 < float(repercent) <= 100:  # 判斷考試成績占總成績百分比有無介於0到100之間
                repercent = float(repercent)
            else:
                repercent = int('None')
            reblind = float(reblind)
            reutil = utilv.get()
            reutil = reutil.strip('()')
            reutil = reutil.replace("'", '')
            reutil = reutil.split(', ')
            reutils = utilsv.get()
            reutils = reutils.strip('()')
            reutils = reutils.replace("'", '')
            reutils = reutils.split(', ')
            reskip = skipv.get()
            subj[rename01][1:7] = [recredit, repercent, reblind, reutil, reutils, reskip]
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
    blind = tk.Label(windowR, text='裸考預期分數', anchor='w')
    blind.grid(row=3, column=0, sticky='w')
    blindE = tk.Entry(windowR, bd =5)
    blindE.grid(row=3, column=1, columnspan=5, sticky='w')
    util = tk.Label(windowR, text='上課效益', anchor='w')
    util.grid(row=4, column=0, sticky='w')    
    utilv = tk.StringVar()
    utilv.set('很低')
    tk.Radiobutton(windowR, variable=utilv, text='很低', value=[4, 0.04, '很低']).grid(row=4, column=1, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='低', value=[4.5, 0.04, '低']).grid(row=4, column=2, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='中', value=[5, 0.03, '中']).grid(row=4, column=3, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='高', value=[5.5, 0.02, '高']).grid(row=4, column=4, sticky='w')
    tk.Radiobutton(windowR, variable=utilv, text='很高', value=[6, 0.02, '很高']).grid(row=4, column=5, sticky='w')
    utils = tk.Label(windowR, text='自己讀的吸收度', anchor='w')
    utils.grid(row=5, column=0, sticky='w')    
    utilsv = tk.StringVar()
    utilsv.set('很低')
    tk.Radiobutton(windowR, variable=utilsv, text='很低', value=[4, 0.04, '很低']).grid(row=5, column=1, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='低', value=[4.5, 0.04, '低']).grid(row=5, column=2, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='中', value=[5, 0.03, '中']).grid(row=5, column=3, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='高', value=[5.5, 0.02, '高']).grid(row=5, column=4, sticky='w')
    tk.Radiobutton(windowR, variable=utilsv, text='很高', value=[6, 0.02, '很高']).grid(row=5, column=5, sticky='w')
    skip = tk.Label(windowR, text='一定要出席', anchor='w')
    skip.grid(row=6, column=0, sticky='w')
    skipv = tk.StringVar()
    skipv.set('是')
    tk.Radiobutton(windowR, variable=skipv, text='是', value='是').grid(row=6, column=1, sticky='w')
    tk.Radiobutton(windowR, variable=skipv, text='否', value='否').grid(row=6, column=2, sticky='w')
    sentb = tk.Button(windowR, text='確定送出', command=correct_get)
    sentb.grid(row=7, column=0, pady = 20, columnspan=6)
    windowR.mainloop()


def winP():
    """輸入偏好視窗"""
    global preference

    def winP_get():
        """取得輸入資訊"""
        global page, subj, Ssort_dict, preference, Csort_dict
        overlap = []
        e = 0
        for p1 in preference:
            repreference = preference[p1][2].get()
            if repreference not in overlap and repreference != '-':
                overlap.append(repreference)
                Ssort_dict[p1] = [float(subj[p1][5][0]) * subj[p1][1] * subj[p1][2], subj[p1][1] * subj[p1][2], subj[p1][2], subj[p1][1], 100 - subj[p1][3], -1 * int(repreference), 0, float(subj[p1][5][1]), subj[p1][3], float(subj[p1][5][0]), subj[p1][3]]
                if subj[p1][6] == '否':
                    Csort_dict[p1] = [float(subj[p1][4][0]) * subj[p1][1] * subj[p1][2], subj[p1][1] * subj[p1][2], subj[p1][2], subj[p1][1], 100 - subj[p1][3], -1 * int(repreference), subj[p1][7], float(subj[p1][4][1])]
                else:
                    noskip_dict[p1] = [float(subj[p1][4][0]) * subj[p1][1] * subj[p1][2], subj[p1][1] * subj[p1][2], subj[p1][7]]
            else:
                error('排序錯誤')
                e = 1
        if e == 0:
            page = 3
            windowP.destroy()

    windowP = tk.Tk()
    windowP.wm_attributes('-topmost',1)
    windowP.title('偏好排序')
    windowP.grid()
    for p2 in subj:
        cNlabal = tk.Label(windowP, text='%8s' %(subj[p2][0] + '        志願'), anchor='w')
        preferenceN = []
        for a in range(len(subj) + 1):
            if a == 0:
                preferenceN.append('-')
            else:
                preferenceN.append(a)
        preference[p2] = [cNlabal, preferenceN]
        cPCombobox = ttk.Combobox(windowP, values=preference[p2][1])
        preference[p2].append(cPCombobox)
    nextC = 0
    for p3 in preference:
        preference[p3][0].grid(row=nextC, column=0, sticky='e', pady = 10, padx = 15)
        preference[p3][2].grid(row=nextC, column=1, sticky='e', pady = 10, padx = 15)
        preference[p3][2].current(0)
        nextC += 1
    sentb = tk.Button(windowP, text='確定送出', command=winP_get)
    sentb.grid(row=nextC, column=0, pady = 20, columnspan=2)
    windowP.mainloop()


"""主程式"""
subj = dict()  # 課程資訊
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
which = 0  # 課程資訊一開始呈現第一頁
start = None  # 起始日期
operate = True
preference = dict()
Ssort_dict = dict()
Csort_dict = dict()
noskip_dict = dict()
origin = 0
improve = 0
weight = 0
print_list = [[[[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]],\
[[[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]],\
[[[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]], [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]]]
playJ2r = 0
while operate:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            operate = False
    if page == 1:
        J1()
    elif page == 2:
        J2_l()
    elif page == 3:
        J2_r()
pygame.quit()  # 關閉視窗