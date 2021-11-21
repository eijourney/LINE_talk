### whole_calc.py ### 
# Author: Ei Miura
# Final Update: 2021/11/21
# 関数モジュール
# mainモジュール: main.py
#
# LINEのテキストデータから
# トーク全体に関するデータを計算する


#ライブラリ
import datetime as dt# 時間の計算を行う



########################################
            ### 関数定義 ###
########################################
# 総通話時間を計算する関数  def total_call_time(formed_text):


# 総通話時間を計算する関数
def total_call_time(formed_text):
    total_call_time = dt.timedelta(0)
    call_count = 0
    for line in formed_text:
        if '通話時間' in line[7]:
            call_count += 1
            s = line[7].split(' ')[-1].split(':')
            if len(s) == 2:
                hours = 0
                minutes = int(s[0])
                seconds = int(s[1])
            elif len(s) == 3:
                hours = int(s[0])
                minutes = int(s[1])
                seconds = int(s[2])
            total_call_time +=  dt.timedelta(hours=hours, minutes=minutes, seconds=seconds)

    return call_count, total_call_time



'''
# 返信時間を計算する関数
def total_call_time(formed_text):
    total_call_time = dt.timedelta(days=0)
    print(total_call_time)
    for line in formed_text:
        string_date = line[0] + '/' + line[1] + '/' + line[2] + ' ' + line[4] + ':' + line[5] + ':' + '00'
        tmp_dt = dt.datetime.strptime(string_date, '%Y/%m/%d %H:%M:%S')
        #print(tmp_dt)
        total_call_time += tmp_dt
    print(total_call_time)
'''
