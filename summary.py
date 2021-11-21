### summary.py ### 
# Author: Ei Miura
# Final Update: 2021/11/21
# 関数モジュール
# mainモジュール: main.py
#
# 結果を辞書型配列、表、グラフにする

# ライブラリ


########################################
        ### 関数定義 ###
########################################
# 結果をまとめる辞書を初期化する関数    def make_dict():


# 結果をまとめる辞書を初期化する関数
def make_dict(formed_text, member_list, day_list, call_count, total_call_time):
    data = {
        '合計通話回数': call_count,
        '合計通話時間': total_call_time,
        '合計トーク日数': len(day_list),
        '始めて話した日': day_list[0],
        '最後に話した日': day_list[-1],
        '合計メッセージ数': len(formed_text)-call_count
    }

    return data

