import requests
import os
from bs4 import BeautifulSoup

#存檔的path
DMs_Path = 'C:/Users/User/我的雲端硬碟FA/資料區_Cloud/Python_FA/WebCrawler/DMs/'

def func(titles, hrefs):
    
    # DEBUG用-打印出所有的 href 和 title
    #for href, title in zip(hrefs, titles):
    #    print(f'href: {href}, title: {title}')

    #針對各個課程去撈DM內容
    for title, href in zip(titles, hrefs):

        part_titles = []
        part_contents = []

        # 進行網頁請求
        response = requests.get(href)
        response.encoding = 'utf-8'

        # 解析網頁內容
        soup = BeautifulSoup(response.text, "html.parser")

        # 抓出課程名稱
        course_name = soup.find('h2', {'id': 'h3Title'}).text
        course_name = course_name[:-15]

        # 抓出課程型態
        ActAttribute = soup.find('span', {'id': 'spanActAttribute'}).text

        # 抓出課程地址
        ActLocation = soup.find('span', {'id': 'spanActLocation'}).text

        # 抓出課程時數
        Duration = soup.find('span', {'id': 'spanDuration'}).text

        # 抓出課程起日期
        ActBeginDate = soup.find('span', {'id': 'spanActBeginDate'}).text

        # 抓出課程訖日期
        ActEndDate = soup.find('span', {'id': 'spanActEndDate'}).text

        # 抓出聯絡人
        ContectCname = soup.find('span', {'id': 'spanContectCname'}).text

        # 抓出連絡電話
        ContectTel = soup.find('span', {'id': 'spanContectTel'}).text

        # 抓出報名截止日
        ForeSignUpEndDate = soup.find('span', {'id': 'spanForeSignUpEndDate'}).text


        # 尋找 分段標題 和 分段內容
        all_part_title = soup.find_all('h3', {'class': 'title'})
        all_part_content = soup.find_all('div', {'id': 'divConBox'})

        for i in all_part_title:
            part_titles.append(i.text.strip())

        for j in all_part_content:
            part_contents.append(j.text.strip())

        # DEBUG用-印出所有的part_title和part_content
        #for k, l in zip(part_titles, part_contents):
        #    print("part_title:" + k)
        #    print("part_content:" + l)
        
        #移動到目錄
        os.chdir(DMs_Path)

        # 錯誤訊息
        error_message = "IndexError: list index out of range\n"

        #檔名
        filename = title + ".txt"

        # 開啟一個新的 .txt 檔案並進入寫入模式
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('課程名稱：' + course_name + '\n')
            f.write('課程型態：' + ActAttribute + '\n')
            f.write('課程地址：' + ActLocation + '\n')
            f.write('課程時數：' + Duration + '\n')
            f.write('課程起日期：' + ActBeginDate + '\n')
            f.write('課程訖日期：' + ActEndDate + '\n')
            f.write('連絡人：' + ContectCname + '\n')
            f.write('連絡電話：' + ContectTel + '\n')
            f.write('報名截止日：' + ForeSignUpEndDate + '\n')    

            for k, l in zip(part_titles, part_contents):
                try:
                    # 將 part title 和 part content 寫入檔案
                    f.write('\n' + '分段標題：' + k + '\n')
                    f.write('分段內容：' + l + '\n')
                except IndexError:
                    # 寫入錯誤訊息
                    f.write(error_message)

""""""


