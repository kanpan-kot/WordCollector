# WordCollector
コトダマン辞書から特定のテーマのワードを収集するスクリプトです．

## 環境構築
### Python, selenium, ChromeDriverの準備
#### Python
- [ここ](https://www.python.org/)からダウンロードできます
#### selenium
- `pip install selenium`でインストールできます
#### ChromeDriver
- [ここ](https://chromedriver.chromium.org/downloads)から自分のChromeのバージョンに合わせたドライバをダウンロードしてください
- ダウンロードしたらpathを通すのをお忘れなく
- Chromeのバージョンは`ブラウザ右上の:みたいなやつ > ヘルプ > Google Chromeについて`から確認できます

## 使用方法
- `WordCollector.py`を実行することで，特定のテーマのワードをすべて収集することができます
- 26行目の数値を適当な値に変更することで任意のテーマのワードを取得できます
- 55行目の一つ目の引数の文字列を変更することで生成されるtxtファイルの名称を変更できます．
- 進捗確認がしやすいように`print`を挟んでますが，特に動作には影響がないため，不要の場合はコメントアウトか消去してください．
