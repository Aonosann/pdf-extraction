import sys
import pdfplumber
import pandas as pd

# 架空の大学の卒業要件（サンプル）
requirements = {
    '人文': 10,
    '自然科学': 8,
    '外国語': 4,
    '学部専攻': 20
}

# 成績→GPA変換
grade_to_gpa = {
    'S': 4.0,
    'A': 3.0,
    'B': 2.0,
    'C': 1.0,
    'D': 0.0
}

# コマンドライン引数からファイル名を取得
if len(sys.argv) < 2:
    print("使い方: python main.py ファイル名")
    exit()

INPUT_FILE = sys.argv[1]

# 拡張子をチェック
if INPUT_FILE.endswith('.pdf'):
    with pdfplumber.open(INPUT_FILE) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
        df = pd.DataFrame(table[1:], columns=table[0])
        
elif INPUT_FILE.endswith('.xlsx'):
    df = pd.read_excel(INPUT_FILE, header=0)
    
else:
    print("対応していないファイル形式です（.pdfまたは.xlsxのみ）")
    exit()

# 共通処理
df['単位数'] = df['単位数'].astype(int)

# GPA計算
df['GPA'] = df['成績'].map(grade_to_gpa)
df['加重GPA'] = df['GPA'] * df['単位数']

print(df)
print(f"\n合計単位数: {df['単位数'].sum()}単位")

# 累積GPA
total_gpa = df['加重GPA'].sum() / df['単位数'].sum()
print(f"累積GPA: {total_gpa:.2f}")

# 科目群ごとの集計
print("\n【科目群ごとの単位数】")
group_summary = df.groupby('科目群')['単位数'].sum()
print(group_summary)

# 卒業要件チェック
print("\n【卒業要件チェック】")
total_shortage = 0
for group, required in requirements.items():
    earned = group_summary.get(group, 0)
    shortage = max(0, required - earned)
    total_shortage += shortage
    
    status = "✓ 達成" if shortage == 0 else f"✗ あと{shortage}単位"
    print(f"{group}: {earned}/{required}単位 [{status}]")

print(f"\n卒業まであと {total_shortage}単位 必要")
if total_shortage == 0:
    print("🎉 卒業要件を満たしています！")