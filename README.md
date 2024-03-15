# 樂樂2.0 機器人

這是一個基於Discord與rwkv架構的語言模型的AI助理機器人，擁有兩種模式：樂樂模式和AI模式。
樂樂模式扮演一個性格外向開放的虛擬助理；而AI模式則是一個傳統的問答機器人。

## 功能
- 樂樂模式：根據預設的個性設定，扮演一個開放的虛擬助理，可以回答各種話題
- AI模式：一般的問答機器人模式，回答詳細並引用相關資訊
- 關鍵字擷取：使用KeyBERT算法從使用者輸入中抽取關鍵字
- 維基百科搜尋：根據關鍵字在維基百科中搜尋相關條目，作為機器人回答的參考資訊
- 清除記憶：可以清除機器人的上下文記憶

## 安裝

1. `git clone https://github.com/samttoo22-MewCat/lala_rwkv_chatbot_2.0.git`
2. `cd lala_rwkv_chatbot_2.0`
3. 安裝所需的Python套件：`python -m pip install -r requirements.txt`
4. 下載RWKV語言模型檔案，放置在想要的路徑後自行更改路徑。</br>
   (模型可以在 https://cdn.jsdelivr.net/gh/josstorer/RWKV-Runner@master/manifest.json 尋找你需要的)
5. 創建好discord Bot後，將它加入你想加入的伺服器(網路上有很多教學)
6. 在程式碼中填入你想要啟用的頻道ID，此設定是為了避免把伺服器其他人吵死。
7. 在程式碼中填入Discord Bot Token

## 使用

1. 執行程式：`python app.py`
2. 機器人會自動加入您設定的Discord伺服器與頻道
3. 在Discord頻道中，輸入「樂樂」開頭的訊息來與機器人對話
4. 輸入「樂樂 change mode」來切換樂樂模式與AI模式
5. 輸入「樂樂 clear」來清除機器人的上下文記憶

## 注意事項
- 本程式僅供研究和娛樂用途，請勿將機器人輸出視為事實或建議
- 樂樂模式的對話內容可能涉及成人話題，請酌情使用

## 備註
- rwkv的pip套件只能選擇單一的字元讓語言模型停下，所以為了避免樂樂自我重，我強烈建議於修改rwkv套件中的generate方法
- 如果可以，請在generate方法中的 `for i in range(token_count)`迴圈中的最底部新增<br>
``
