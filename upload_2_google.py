import gspread
from oauth2client.service_account import ServiceAccountCredentials

JSON_FILE_PATH = r'C:\Users\User\我的雲端硬碟FA\資料區_Cloud\Python_FA\WebCrawler\forwebcrawler-712156a63a57.json'

def write_columeABC(domain, titles, hrefs):
    # 使用的API
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    # JSON 憑證檔案
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE_PATH, scope)
    gc = gspread.authorize(credentials)

    # 開啟試算表並取得第一張工作表
    worksheet = gc.open('AllCourseData').sheet1

    # 陣列資料
    data = [1, 2, 3, 4, 5]

    # 將資料寫入 Google Sheets
    worksheet.append_row(data)
