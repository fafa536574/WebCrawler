import gspread
from oauth2client.service_account import ServiceAccountCredentials


JSON_FILE_PATH = r'C:\Users\User\我的雲端硬碟FA\資料區_Cloud\Python_FA\WebCrawler\forwebcrawler-712156a63a57.json'

#
def func(AllCourseData_transposed):
    # 使用的API
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    # JSON 憑證檔案
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE_PATH, scope)
    gc = gspread.authorize(credentials)

    # 開啟試算表並取得第一張工作表
    worksheet = gc.open('AllCourseData').sheet1

    # 使用 gspread 更新 Google Sheets
    worksheet.update('A2', AllCourseData_transposed)

    """" 
    # 陣列資料
    data = [
        {'domain': 'example1.com', 'title': 'Example 1', 'url': 'http://example1.com'},
        {'domain': 'example2.com', 'title': 'Example 2', 'url': 'http://example2.com'},
        # 等等...
    ]
    # 将数据转换为一个二维列表。
    data_as_list = [[entry['domain'], entry['title'], entry['url']] for entry in data]

    # 一次性写入所有数据。注意 'A2' 是起始单元格的地址。
    worksheet.update('A2', data_as_list)

    # 陣列資料
    data = [1, 2, 3, 4, 5]

    # 将数据插入 Google Sheets 的第二行
    worksheet.insert_row(data, 2)
   """""


