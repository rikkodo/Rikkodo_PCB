#!python3

"""
Keyboard Layout Editorの出力からLegend部分を空欄にする。
対象は stdin
Legend部分: "<"以外の文字>*", 空欄" ""
"""

import sys
import re

for ll in sys.stdin:
    ll = re.sub(r"\"[^\"]*\"", "\"\"", ll)
    print(ll, end="")
