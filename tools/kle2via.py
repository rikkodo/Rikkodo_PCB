#!python3

"""
[Keyboard Layout Editor]<https://www.keyboard-layout-editor.com/>
で作成したLayoutをvia用のjsonに貼り付ける形式に変換する。

([a-z]:)を"\1:"に置換

対象は sys.stdin

## 参考
[自作キーボード温泉街の歩き方 （設計者向け）VIA対応のファームウェアを作ろう](https://salicylic-acid3.hatenablog.com/entry/via-support)
"""

import sys
import re

for ll in sys.stdin:
    ll = re.sub(r"([a-z]):", "\"\\1\":", ll)
    print(ll, end="")
