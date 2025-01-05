#! python3

import sys
import json

"""
[Convert KLE raw to QMK info.json]<https://qmk.fm/converter/>
で作成したLayoutをkeyboard.jsonに貼り付ける形式に変換する。

対象は sys.argv[1]
"""

with open(sys.argv[1], 'r') as f:
    klejson = json.load(f)

layout = klejson["layouts"]["LAYOUT"]["layout"]


xx = []
for key in layout:
    label = key.pop("label")
    la = "                {"
    lz = "}"

    aa = [f"\"matrix\": [{label}]"]
    for k in key:
        aa.append(f"\"{k}\":{key[k]}")

    xx.append(f"{la}{", ".join(aa)}{lz}")

print("            \"layout\": [")
print(",\n".join(xx))
print("            ]")
