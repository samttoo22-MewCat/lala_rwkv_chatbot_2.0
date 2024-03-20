# 樂樂2.0 機器人

這是一個基於 Discord 與 rwkv 架構的大型語言模型的 AI 助理機器人，擁有兩種模式：樂樂模式和 AI 模式。</br>
樂樂模式扮演一個性格外向開放的虛擬助理；而 AI 模式則是一個傳統的問答機器人。

## 功能
- 樂樂模式：根據預設的個性設定，扮演一個開放的虛擬助理，可以回答各種話題
- AI 模式：一般的問答機器人模式，回答詳細並引用相關資訊
- 關鍵字擷取：使用 jieba 台灣繁體中文版+自定義辭典準確分割中文維基百科條目名，</br>再使用 shibing624/text2vec-base-chinese 嵌入模型將使用者輸入轉換成嵌入向量，</br>最後使用餘弦相似度方法比對抽取出關鍵字
- 維基百科搜尋：根據關鍵字在維基百科中搜尋相關條目，作為機器人回答的參考資訊
- 清除記憶：可以清除機器人的上下文記憶

## 安裝

1. `git clone https://github.com/samttoo22-MewCat/lala_rwkv_chatbot_2.0.git`
2. `cd lala_rwkv_chatbot_2.0`
3. 安裝所需的 python 套件：`python -m pip install -r requirements.txt`
4. 下載 RWKV 語言模型檔案，放置在想要的路徑後自行更改路徑。</br>
   (模型可以在 https://cdn.jsdelivr.net/gh/josstorer/RWKV-Runner@master/manifest.json 尋找你需要的)
5. 創建好 discord Bot 後，將它加入你想加入的伺服器(網路上有很多教學)
6. 在程式碼中填入你想要啟用的頻道 ID ，此設定是為了避免把伺服器其他人吵死。
7. 在程式碼中填入 Discord Bot Token

## 使用

1. 執行程式：`python AI_app.py`
2. 在 Discord 頻道中，輸入「樂樂」開頭的訊息來與機器人對話
3. 輸入「樂樂 change mode」來切換樂樂模式與AI模式
4. 輸入「樂樂 clear」來清除機器人的上下文記憶

## 注意事項
- 本程式僅供研究和娛樂用途，請勿將機器人輸出視為事實或建議
- 樂樂模式的對話內容可能涉及成人話題，請酌情使用

## 備註
- rwkv 的 python 套件只能選擇單一的字元讓語言模型停下，所以為了避免樂樂自我重複的情況發生，我強烈建議修改於 rwkv.utils 中的 generate 方法
- 如果可以，請在 generate 方法中的 `for i in range(token_count)`迴圈中的最底部新增<br>
```python
if '乐乐' in out_str or '用戶' in out_str:
    break
```
