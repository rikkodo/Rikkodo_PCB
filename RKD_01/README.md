# KEYBOARD

RKD01-Split

## Ideal

* ChocV2を使用した、分割60%ロウスタッガードキーボード
* 2U Shiftを使用し、右下に逆T字のカーソルキーを持つ構成
* AZ1UBALLを使用したマウス機能内蔵

## FOOTPRINT

Salicylic-acid3 [KiCAD_FootPrint](https://github.com/Salicylic-acid3/KiCAD_FootPrint)

koktoh [BrownSugar_KBD_KiCad_Library](https://github.com/koktoh/BrownSugar_KBD_KiCad_Library/tree/master)

palette-system [az1uball](https://github.com/palette-system/az1uball/tree/main/kicad)

Seeed-Studio [OPL_Kicad_Library](https://github.com/Seeed-Studio/OPL_Kicad_Library)

## REFS

kotoh [koktoh の雑記帳 自作キーボード用の KiCad フットプリントライブラリを作った](https://koktoh.hatenablog.com/entry/2023/08/25/195443)

kotoh [koktoh の雑記帳 【開発者向け】 TRRS ジャックの配線ってどうすればいいの？](https://koktoh.hatenablog.com/entry/2024/05/10/191926)

サリチル酸 [Zenn GL516 デザインガイド](https://zenn.dev/salicylic_acid3/books/gl516_design_guide)

サリチル酸 [booth 自作キーボード設計ガイド](https://booth.pm/ja/items/4410329)

ミクモ [NinthSky Studio ほぼゼロから始める自作キーボード設計体験記](https://ninthsky.hatenablog.com/entry/keyboard_design_zero)

いまむら [ただいま村 自作キーボードがひとまず完成してしまったがここからが沼](https://ima.hatenablog.jp/entry/2024/02/24/223000)

Yoshimasa Niwa [Zenn 自作キーボードを自作した話](https://zenn.dev/niw/articles/my_first_keyboard_60)

@aikawa_YO [Qiita 回路図～プログラムまで自作するキーボード](https://qiita.com/aikawa_YO/items/a31353d88b8b73f51e8b)

## 部品

|部品|数|
|:--|:---|
|Promicro|2個|
|コンスルーかピンヘッダ・ピンソケット|4個|
|chosスイッチ|x個|
|chocソケット|x個|
|ダイオード|x個|
|M2六角スペーサ 5mm|10個|
|M2丸スペーサ 9mm or 10mm|4個|
|M2丸スペーサ 3.5mm|4個|
|M2低頭ネジ|36個|
|TRRSジャック|2個|
|Choc用スタビライザ|4個|
|ゴム足|y個|

## 配置

|フォルダ|概要|
|:--|:--|
|Common|左右共通部品 (マイコンプレート)|
|Left|左|
|Right|右|

## 備忘録

### PCBエディタの「グリッド」をユーザ定義できない

画面上グリッドセレクトボックス -> グリッドを編集

### グリッドに合わせたオブジェクト設置ができない

右クリック -> 位置決めツール -> 参照点を指定して移動 -> 基準点を選択

### 自動配線をする場合

* 参照先がないフットプリントがあると自動配信ができない。Markを回路図に入れ、対応させる
* デフォルトの線幅が200nmになっているので、設計入門ガイドに合わせるならば250nmに変更する

### ダイオードのフットプリント

TH_SMD (表面実装 + スルーホール) 型にすると、スルーホールをビアがわりにしてくれるので自動配線が成功しやすい

### 配線の全消去

script consoleで以下

```python
import pcbnew
b = pcbnew.GetBoard()
t = b.GetTracks()
for tt in t:
    tt.DeleteStructure()
```

あすき [試行錯誤な日々 KiCadで基板の配線とビアを全部消す方法](https://asukiaaa.blogspot.com/2019/06/kicad.html)

## 問題点

### 配置の修正

* もうちょっと支柱を立てたい。特に右手
* 右手、左下、RKD2の配置に合わせて修正
* 右手、I2Cがちゃんと動くか不安 -> 動かなかった・・・
* I2Cのコネクタの位置がモジュール部に近すぎるため、使用しにくい。
* 備忘 Chocスイッチを使う場合、トッププレートの分厚さは1.2mm。プレートマウントスタビライザーがメインプレートに干渉する。

### ロータリーエンコーダを使いたかったけどダメだった

左手側は入力が2個残っているので、ロータリーエンコーダをつけるつもりだったが、QMK側で左と右のROWの数を合わせないといけないという制約のため、つけられなかった。

### ChocV2を使うつもりなのにフットプリントがV1

** ChocV2を使うにはスタビライザーが存在しない問題を解決しなくてはいけない！！！

以下を再発注する

* Assemble_L
* Assemble_R
* Top_R (右下の配置を修正したため)
* AzFoot

### I2Cデバイスを追加で使用する場合

SDA, SCLのピンとSplitKeyboardのシリアル通信用のピンは分けないといけない？模様
先に知っていればSplit間の通信は空いているピンに割り振ったのに・・・

OLEDと共有できるのかは用検証

### promicroの場合

多少面倒でもリセットボタンはつけておくこと。
ファーム書き込みのたびにPromicroを外してRSTピンを、短絡させるのはかなりめんどい。
ボタンはなくてもピンセットでリセットできるように、引き出しておくことを推奨。

Raspberry Pi picoならBootselを選べるようにしておく。
