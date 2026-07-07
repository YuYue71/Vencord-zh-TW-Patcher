# Vencord zh-TW Patch (Vencord 繁體中文補丁)

此 Repository (版本庫) 提供已預先修改之 `renderer.js` (渲染引擎腳本), 用於為 Vencord (Vencord 客戶端模組) 啟用完整的 Traditional Chinese (繁體中文) 本地化支援.

* Vencord Official Website (Vencord 官方網站): https://vencord.dev/
* Vencord GitHub Repository (Vencord 官方版本庫): https://github.com/Vendicated/Vencord

## 1. Architecture Overview (架構概述)
* Methodology (實作方法): 直接替換已編譯之 `renderer.js` (渲染引擎腳本).
* Deployment (部署): 終端使用者無需依賴 Python (Python 執行環境), 透過 Zip Archive (壓縮檔案) 覆寫即可生效.
* Coverage (覆蓋率): 包含 Core UI (核心使用者介面), Settings (設定面板) 以及 100+ Plugin (外掛模組) 說明.

## 2. Repository Structure (版本庫結構)
* `README.md`: Core documentation (核心文件).
* `LICENSE`: MIT License (MIT 授權條款).
* `renderer.js`: Modified translation file (已注入翻譯之檔案), 供終端使用者直接替換.
* `renderer_original.js`: Original backup file (原始備份檔案), 嚴格對齊當前版本.
* `tools/`: Development directory (開發目錄), 存放 Translation Iteration (翻譯迭代) 工具.
  * `patcher.py`: Injection script (注入腳本).
  * `zh-TW.json`: Modular dictionary (模組化字典檔).

## 3. Deployment Protocol (部署流程 - 終端使用者)
1. 前往本 Repository (版本庫) 的 Releases (發布頁面), 下載最新版本的 `.zip` Zip Archive (壓縮檔案).
2. 定位 Vencord (Vencord 客戶端模組) 的 Output Directory (輸出目錄). Windows (Windows 作業系統) 預設路徑為: `%appdata%\Vencord\dist`.
3. 將下載的 `.zip` 檔案移動至該目錄下.
4. 解壓縮該檔案, 並選擇 Overwrite (覆寫) 目錄下現有的 `renderer.js` (渲染引擎腳本) 等檔案.
5. 聚焦 Discord (Discord 通訊軟體) 視窗並執行 `Ctrl + R` (重新載入快捷鍵) 以觸發 UI Reload (使用者介面重新載入).

## 4. Iteration Protocol (迭代流程 - 開發者)
若需擴充或修改 Translation Strings (翻譯字串), 請遵循以下 Pipeline (管線):
1. 進入 `tools/` (開發目錄).
2. 編輯 `zh-TW.json` (模組化字典檔), 確保 JSON (JavaScript 物件表示法) 語法合法, 嚴禁遺漏 Comma (逗號).
3. 執行 `patcher.py` (注入腳本).
4. 腳本將自動讀取上一層目錄的 `renderer_original.js` (原始備份檔案), 執行精準 String Replacement (字串替換), 並將全新的 `renderer.js` (渲染引擎腳本) 輸出至根目錄.

## 5. Maintenance Cycle (維護週期)
* Update Override (更新覆蓋): 當 Vencord (Vencord 客戶端模組) 觸發 Auto-Update (自動更新) 時, 系統的 `renderer.js` (渲染引擎腳本) 將被上游覆蓋.
* Restoration (還原): 需重新自 Releases (發布頁面) 獲取最新 `.zip` 檔案並重複 Deployment Protocol (部署流程).

## 6. Security & Risk Mapping (安全性與風險映射)
* Terms of Service (服務條款): 修改客戶端違反 Discord (Discord 通訊軟體) ToS (服務條款). 部署風險由使用者自負.
* Render Deadlock (渲染死鎖): 若啟用 Window Transparency (視窗透明度) 且同時運行 Wallpaper Engine (動態桌布軟體), 將引發 Electron (Electron 框架) 渲染死鎖. 遇 UI (使用者介面) 凍結時, 請關閉動態桌布後重啟.
* DOM Limitations (文件物件模型限制): 受限於 React (React 前端框架) 渲染規則, 帶有 `\n` (換行符號) 的字串在特定 Component (元件) 中僅會渲染為 Whitespace (空白字元).