# pdf-extraction
# 成績管理ツール
PDFまたはExcelファイルから成績データを読み込み、卒業要件チェックとGPA計算を行うツールです。

## 機能

- PDFファイルからの表データ抽出
- Excelファイルからのデータ読み込み
- 科目群ごとの単位数集計
- 卒業要件との比較
- 累積GPA計算

## 環境構築
# リポジトリをクローン
git clone https://github.com/Aonosann/pdf-extraction.git
cd pdf-extraction

# 仮想環境を作成
python -m venv .venv

# 仮想環境を有効化
# Windows
.venv\Scripts\activate

# 必要なライブラリをインストール
pip install -r requirements.txt
```

## 使い方
python main.py ファイル名.xlsx
python main.py ファイル名.pdf

## 入力ファイルの形式

| 科目群 | 科目名 | 単位数 | 成績 |
|--------|--------|--------|------|
| 人文 | 日本文学 | 2 | A |
| 自然科学 | 線形代数 | 2 | S |

## 出力例
合計単位数: 24単位
累積GPA: 3.17

【卒業要件チェック】
人文: 8/10単位 [✗ あと2単位]
自然科学: 4/8単位 [✗ あと4単位]