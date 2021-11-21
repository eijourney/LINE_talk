### form.py ###
# Author: Ei Miura
# Final Update: 2021/11/21
# 関数モジュール
# mainモジュール: main.py
#
# LINEのテキストデータを整形する
# メンバーリストと日にちリストを作成する


# ライブラリ
import re


########################################
            ### 関数定義 ###
########################################
# テキストデータを整形する  def form_text(text):
# メンバーリストを作成する  def make_member_list(formed_text):
# 日にちリストを作成する    def make_day_list(formed_text):


# テキストデータを整形する
def form_text(text):
    formed_text = []
    # テキストデータを1行ごとに分ける
    text_line = text.split('\n')

    for i, line in enumerate(text_line, 1):
        # 初めの3行（～とのトーク履歴、保存日時、空白行は無視）
        if line == "" or i < 3:
            continue
            #formed_text.append(line)

        # ['yyyy', 'mm', 'dd', '曜日', '時', '分', '名前', 'メッセージ'] のように保存したい
        # 年月日曜日を保存
        match_day = re.search(r'\d{4}/\d{2}/\d{2}\(.\)', line)
        if match_day:
            year = match_day.group()[0:4]
            month = match_day.group()[5:7]
            days = match_day.group()[8:10]
            week_day = match_day.group()[11]

        # メッセージの行ならformed_textに保存する
        s = line.split('\t')
    
        # 送信日時とメッセージを1行にまとめる
        if len(s) == 3:
            time = s[0].split(':')
            hour = time[0]
            minutes = time[1]
            name = s[1]

            # メッセージが複数行の場合、改行をはさんで一つのメッセージにする
            if ('"' in s[2]):
                j = i
                tmp_line = ''
                while(j < len(text_line)):
                    tmp_line = tmp_line + '\n' + text_line[j]
                    # 終わりの"を探す なかったら無視
                    if '"' in tmp_line:
                        s[2] = s[2] + tmp_line
                        break
                    j += 1

            message = s[2].replace('"', '')


            formed_text.append([year, month, days, week_day, hour, minutes, name, message])

        # 「メッセージの送信を取り消しました」の場合
        if len(s) == 2:
            time = s[0].split(':')
            hour = time[0]
            minutes = time[1]

            if 'メッセージの送信を取り消しました' in s[1]:
                if 'がメッセージの送信を取り消しました' in s[1]:
                    name = 'other'
                    message = s[1].split('が')[1]
                else:
                    name = 'me'
                    message = 'メッセージの送信を取り消しました'

            formed_text.append([year, month, days, week_day, hour, minutes, name, message])


    return formed_text

# メンバーリストを作成する
def make_member_list(formed_text):
    member_list = []
    for line in formed_text:
        if line[6] not in member_list and line[6] != 'other' and line[6] != 'me':
            member_list.append(line[6])
    return member_list

# 日にちリストを作成する
def make_day_list(formed_text):
    day_list = []
    for line in formed_text:
        day = line[0] + '/' + line[1] + '/' + line[2] + '(' + line[3] + ')'
        if day not in day_list:
            day_list.append(day)
    return day_list

