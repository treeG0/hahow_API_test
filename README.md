# Hahow API 自動化程式

API 自動化程式並且驗證:
1. 有多少不同種族的人出現在第六部？
2. 請依據電影集數去排序電影名字？
3. 請幫我挑出電影裡所有的車輛，馬力超過１０００的。

# 執行方法

首先，必須確認環境已安裝Python 3以上版本
```
$ python --version
Python 3.4.1
```
安裝執行必要lib
```
pip install configparser mock requests
```
clone repository至本機後，在專案根目錄底下執行下面命令
```
# 驗證三個題目
python -m unittest -v integration/api_test.py
```

```
# 執行support unit test
python3 -m unittest -v unit_test/test_swapi_request.py
```

# 專案架構
```
hahow_project
|
|-----integration # 根據需求的測試用例，藉由support裡提供的方法獲取資料
|
|-----support     # 處理API request，主要負責控制API獲取response的內容
|
|-----unit_test   # support的unit test
|
|-----config.ini  # 環境設置
```
