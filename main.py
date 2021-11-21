### main.py ###
# Author: Ei Miura
# Final Update: 2021/11/21
# mainモジュール
#
# LINEのテキストデータを分析する



# ライブラリ
import cgi
import codecs
import sys

# モジュール
import form as ff
import whole_calc as wc
import summary as sm
import print_html as phtml

########################################
            ### main ###
########################################



########################################
# 0  htmlからテキストデータを読みこむ
########################################
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

form = cgi.FieldStorage()

# テキストを読み込み変数へ代入
# 未入力の場合エラー表示
if "text" not in form:
    print(f'''
    <h1>Error!</h1>
    <br>
    "テキストを入力してください！"
    <a href='/'><button type='submit'>戻る</button></a>
    ''')
    sys.exit()

text = form.getfirst('text')

########################################
# 1   　　　textを整形する
########################################
# 整形
formed_text = ff.form_text(text)
# メンバーリスト、日にちリストの作成
member_list = ff.make_member_list(formed_text)
day_list = ff.make_day_list(formed_text)

########################################
# 2   　　　データを計算する
########################################
# 2-1 トーク全体に関するデータ
call_count, total_call_time = wc.total_call_time(formed_text)

# 2-2 メンバーそれぞれに関するデータ



########################################
# 3   　　　結果を要約、保存する
########################################
# 結果を辞書にまとめる
data = sm.make_dict(formed_text, member_list, day_list,
                    call_count, total_call_time)


########################################
# 4   　　　htmlで結果を表示する
########################################
phtml.print_html(data)
