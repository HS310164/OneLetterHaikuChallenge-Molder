# OneLetterHaikuChallenge-Molder

## これは何？
音民鯖が誇る文化の1つである1文字俳句のデータベース化作業~~で楽をしたい~~を効率化することを目的として作成しているものです。

## 検証環境
- Windows 11
- Python  3.11.2

## 機能
1. 本アプリケーションを実行
    - 参加者:その1文字俳句の参加者リストをクリップボードに含めます 
1. Discord で [なんでもフォーラムチャンネル] - [壁たちの、1文字俳句] を開き、俳句の1文字目のポストから最後の文字のポストまでをクリップボードにコピー
1. 本アプリケーションのボタンをクリックすると成形された俳句がクリップボードに保存される
1. 適当な場所に張り付けてください

## 制限事項
- 成形する1文字俳句は各ポストかな1文字、字余り・字足らずがないことを想定しています。
- 


## Compile

Install required packages
```
pip install -r requirements.txt
```

Create execute file from the source
```
pyinstaller clipboard.py --onefile --noconsole
```

## ToDo
- もっと楽がしたい
- 字余り・字足らずの対応
- 1つの投稿に複数の文字がある場合の対応
- 漢字が含まれている場合の対応