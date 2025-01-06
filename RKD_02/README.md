# KEYBOARD

RKD02-Single

## Ideal

* ChocV2を使用した、一体型60%ロウスタッガードキーボード
* 2U Shiftを使用し、右下に逆T字のカーソルキーを持つ構成
* AZ1UBALLを使用したマウス機能内蔵

## FOOTPRINT

[Raspberry Pi Datasheets](https://datasheets.raspberrypi.com)

<https://datasheets.raspberrypi.com/rp2040/VGA-KiCAD.zip>

## REF

MachiaWorks [zenn Raspberry Pi Picoでキーボードを自作してみた。](https://zenn.dev/machiaworks/articles/22ec62466bf37c)

kamuycikap [Kamuycikap - SentenceDataBase KiCAD 5.1.10(Windows)にRaspberryPI Picoのシンボルを登録](https://kamuycikap.hatenablog.com/entry/2021/11/04/110027)

yyoshisaur [よしざうるすのブログ QMK FirmwareをRaspberry Pi Picoで使ってみる](https://yyoshisaur.hatenablog.com/entry/2022/07/24/120000)

Yuta [zenn KiCADでよく使う部品](https://zenn.dev/yuta_enginner/articles/a5d53eaf02bcb1)

Atsushi Morimoto [zenn QMK Firmware、REMAP(VIA)の対応手順](https://zenn.dev/74th/articles/7efc788a31d06f)

Yoichiro [天使やカイザーと呼ばれて Lunakey Mini/Pico/Macroの設計をオープンにしました](https://www.eisbahn.jp/yoichiro/2021/10/open_lunakey_design_docs.html#gsc.tab=0)

## 問題点

### I2CのVCC

I2Cの電源電圧としてどれを使えば良いかがよくわかっていない。今作はLEDを使わないので3.3Vで良いのか？

* OLED: 5V(VBUS)を繋ぐ例も、3.3Vを繋ぐ例も両方見つけられた。
  * 5Vでの動作例: [SunFounder Universal Maker Sensor Kit ドキュメント レッスン27: OLEDディスプレイモジュール (SSD1306)](https://docs.sunfounder.com/projects/umsk/ja/latest/04_pi_pico/pico_lesson27_oled.html)
  * 3.3Vでの動作例: [ロジカラブログ ラズパイPicoでSSD1306有機ELディスプレイの使い方 MicroPython編](https://logikara.blog/raspi_pico_oled_micropy/)
* AZ1UBALL ([BOOTH](https://booth.pm/ja/items/4202085), [GitHub](https://github.com/palette-system/az1uball)): 5Vでも3.3Vでも動作するとの記載あり。ただVCCが5Vで、SDA/SCLが3.3V(GPIO)で動作するか不明。
* StickPointV ([BOOTH](https://74th.booth.pm/items/5404009), [GitHub](https://github.com/74th/stickpoint-firmware)): 3.3V推奨だが、5Vでも動作すると記載あり。VCCが5Vで、SDA/SCLが3.3V(GPIO)で動作するか不明。

I2CはハイインピーダンスとLowで動いているので、回路側がやられない限り、VCC側が何Vでも動くということだろうか。

なお、LEDを使う場合、電源は5Vを降圧して使う必要があるらしい。

### 分割する場合のVCC

※今回は一体型なので対象外

Rasbperry Pi Picoで分割キーボードを作る場合の左右接続はどうするべきか？スレーブ側の電源入力になるのでVSYSを使うべきである模様。
(Lunakey Picoも左右接続にはVSYSを使用している模様)

※1 VBUSに電源供給するのは勧められない模様。VBSUはUSBの電源と直結しているためUSBとVBUS両方に電源供給するとショートする。
VSYSはUSBとの間にダイオードがあるためショートしない。
([yahoo知恵袋 【電子工作初心者】RaspberryPi Picoの電源について](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13269871068))

※2 3.3Vに電源供給してはいけない。
