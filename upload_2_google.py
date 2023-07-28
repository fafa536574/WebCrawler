import gspread
from oauth2client.service_account import ServiceAccountCredentials


JSON_FILE_PATH = r'C:\Users\User\我的雲端硬碟FA\資料區_Cloud\Python_FA\WebCrawler\forwebcrawler-712156a63a57.json'

def func(AllCourseData_transposed):
    # 使用的API
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    # JSON 憑證檔案
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE_PATH, scope)
    gc = gspread.authorize(credentials)

    # 開啟試算表並取得第一張工作表
    worksheet = gc.open('AllCourseData').worksheet('data')

    # Fetch all records
    records = worksheet.get_all_records()

    # Count the records. Since it's a list of dictionaries, each dictionary corresponds to a row
    row_count = len(records)

    # 盤出來的資料開始為第0列，標題為第1列，因此實際差了2列
    next_row = row_count + 2

    # 构造A1记法的范围字符串，例如 "A11"
    range_str = "A" + str(next_row)

    # 使用 gspread 更新 Google Sheets
    worksheet.update(range_str, AllCourseData_transposed)



