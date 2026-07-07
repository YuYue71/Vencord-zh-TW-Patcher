import os
import json

js_file = r"C:\Users\User\AppData\Roaming\Vencord\dist\renderer.js"
json_file = "zh-TW.json"

def apply_translation_pack():
    if not os.path.exists(json_file):
        print(f"[錯誤] 找不到翻譯包檔案: {json_file}")
        return
    if not os.path.exists(js_file):
        print(f"[錯誤] 找不到目標核心檔案: {js_file}")
        return

    # 讀取 JSON 字典
    with open(json_file, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # 讀取 Vencord 核心腳本
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    replace_count = 0
    
    # 執行迴圈比對與替換
    for eng, cht in translations.items():
        # 略過用來作為內部目錄與註解的自訂標籤 (以底線開頭)
        if eng.startswith("_"):
            continue
            
        # 確保只有在精準匹配到字串時才進行替換
        if eng in content:
            content = content.replace(eng, cht)
            replace_count += 1

    # 寫回覆蓋原檔
    if replace_count > 0:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[成功] 魔改完成！已成功替換了 {replace_count} 組字串。")
        print("[提示] 請回到 Discord 視窗，按下 Ctrl + R 重新載入介面即可生效。")
    else:
        print("[警告] 沒有找到任何可替換的字串。可能是 Vencord 已經更新，或是檔案已經被替換過。")

if __name__ == "__main__":
    apply_translation_pack()