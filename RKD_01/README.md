# KEYBOARD

RKD01

## Ideal

* ChocV2を使用した、60%ロウスタッガードキーボード
* 2U Shiftを使用し、右下に逆T字のカーソルキーを持つ構成
* AZ1UBALLを使用したマウス機能内蔵

## FOOTPRINT

Salicylic-acid3 [KiCAD_FootPrint](https://github.com/Salicylic-acid3/KiCAD_FootPrint)

koktoh [BrownSugar_KBD_KiCad_Library](https://github.com/koktoh/BrownSugar_KBD_KiCad_Library/tree/master)

palette-system [az1uball](https://github.com/palette-system/az1uball/tree/main/kicad)

## REFS

kotoh [koktoh の雑記帳 自作キーボード用の KiCad フットプリントライブラリを作った](https://koktoh.hatenablog.com/entry/2023/08/25/195443)

kotoh [koktoh の雑記帳 【開発者向け】 TRRS ジャックの配線ってどうすればいいの？](https://koktoh.hatenablog.com/entry/2024/05/10/191926)

サリチル酸 [Zenn GL516 デザインガイド](https://zenn.dev/salicylic_acid3/books/gl516_design_guide)

サリチル酸 [booth 自作キーボード設計ガイド](https://booth.pm/ja/items/4410329)

ミクモ [NinthSky Studio ほぼゼロから始める自作キーボード設計体験記](https://ninthsky.hatenablog.com/entry/keyboard_design_zero)

いまむら [ただいま村 自作キーボードがひとまず完成してしまったがここからが沼](https://ima.hatenablog.jp/entry/2024/02/24/223000)

Yoshimasa Niwa [Zenn 自作キーボードを自作した話](https://zenn.dev/niw/articles/my_first_keyboard_60)

## 部品

|部品|数|
|:--|:---|
|Promicro|2個|
|コンスルーかピンヘッダ・ピンソケット|4個|
|chosスイッチ|x個|
|chocソケット|x個|
|ダイオード|x個|
|M2六角スペーサ 5mm|16個|
|M2丸スペーサ 9mm or 10mm|4個|
|M2低頭ネジ|36個|
|TRRSジャック|2個|
|ロータリーエンコーダ, ノブ|1個|
|ゴム足|y個|

## 配置

|フォルダ|概要|
|:--|:--|
|Common|左右共通部品 (マイコンプレート)|
|Left|左|
|Right_Id01| 右 人差し指トラックボール|
|Right_Tm01| 右 親指トラックボール|

## 備忘録

### PCBエディタの「グリッド」をユーザ定義できない

画面上グリッドセレクトボックス -> グリッドを編集

### グリッドに合わせたオブジェクト設置ができない

右クリック -> 位置決めツール -> 参照点を指定して移動 -> 基準点を選択

### 自動配線をする場合

参照先がないフットプリントがあると自動配信ができない。Markを回路図に入れ、対応させる。
