import pdfplumber
import pandas as pd

PDF_FILE = "Book1.pdf"
OUTPUT_CSV = "成績データ.csv"
OUTPUT_EXCEL = "成績データ.xlsx"

with pdfplumber.open(PDF_FILE) as pdf:
    page = pdf.pages[0]
    table = page.extract_table()
    
    # DataFrameに変換
    df = pd.DataFrame(table[1:], columns=table[0])
    
    # 単位数を数値に変換
    df['単位数'] = df['単位数'].astype(int)
    
    # 合計単位数を計算
    total_units = df['単位数'].sum()
    
    print(df)
    print(f"\n合計単位数: {total_units}単位")
    
    # 科目群ごとの集計
    print("\n【科目群ごとの単位数】")
    group_summary = df.groupby('科目群')['単位数'].sum()
    print(group_summary)
    
    # CSVに保存
    df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    print(f"\n{OUTPUT_CSV} に保存しました")
    
    # Excelに保存
    df.to_excel(OUTPUT_EXCEL, index=False)
    print(f"{OUTPUT_EXCEL} に保存しました")