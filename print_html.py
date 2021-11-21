### print_htmlc.py ###
# Author: Ei Miura
# Final Update: 2021/11/21
# 関数モジュール
# mainモジュール: main.py
#
# LINEのテキストデータから分析した結果を
# htmlで表示する


########################################
        ### 関数定義 ###
########################################
# 辞書にまとめられた結果をhtmlで表示する
def print_html(data):
    print(f'''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
    <meta charset="UTF-8">
    <title>Result</title>
    </head>
    <body>
    <div>''')

    for key, value in data.items():
        print(f'''{key}: {value}<br>''')

    print(f'''
    </div>
    </body>
    </html>
    ''')


