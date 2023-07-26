from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import os


CHROMEDRIVER_PATH = r'C:\Users\User\我的雲端硬碟FA\資料區_Cloud\Python_FA\WebCrawler\chromedriver.exe'
#存檔的path
Urls_Path = 'C:/Users/User/我的雲端硬碟FA/資料區_Cloud/Python_FA/WebCrawler/DomainPage/'
select_value = '5'  # 下拉選項值，試作先設為5

def get_links(domain, domainurl):
    # 創建一個新的 Chrome 瀏覽器實例
    driver = webdriver.Chrome(executable_path  =CHROMEDRIVER_PATH)

    # 載入該網頁
    driver.get(domainurl)

    # 找到下拉式選單元素
    select_element = driver.find_element(By.ID,'ddlPageSize')

    # 建立Select物件
    select = Select(select_element)

    # 選擇值為100的選項
    select.select_by_value(select_value)

    # 獲取頁面的HTML內容
    html = driver.page_source

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')


    # 找到所有 class 為 'text-wrap' 的 div 標籤
    divs = soup.find_all('div', class_='text-wrap')

    # 儲存所有的 href 和 title
    domains = []
    titles = []    
    hrefs = []


    for div in divs:
        # 找到每個 div 中的 a 標籤
        a = div.find('a')

        # 將 href 和 title 加到相對應的列表中
        hrefs.append(a['href'])
        titles.append(a['title'])
        domains.append(domain)

    """""DEBUG用，輸出html檔確認
    #移動到目錄
    os.chdir(Urls_Path)

    #存成html檔
    with open(domain +'.html', 'w', encoding='utf-8') as f:
        f.write(html)
    """""

    # 關閉瀏覽器視窗
    driver.quit()

    return domains, titles, hrefs


def get_nextpage_links(domain, domainurl):
    # 創建一個新的 Chrome 瀏覽器實例
    driver = webdriver.Chrome(executable_path  =CHROMEDRIVER_PATH)

    # 載入該網頁
    driver.get(domainurl)

    # 找到下拉式選單元素
    select_element = driver.find_element(By.ID,'ddlPageSize')

    # 建立Select物件
    select = Select(select_element)

    # 選擇值為100的選項
    select.select_by_value(select_value)

    # 使用JavaScript來點擊"到最後一頁"
    last_page_button = driver.find_element(By.CSS_SELECTOR, 'i.mdi.mdi-chevron-double-right')
    driver.execute_script("arguments[0].click();", last_page_button)

    # 獲取頁面的HTML內容
    html = driver.page_source

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')


    # 找到所有 class 為 'text-wrap' 的 div 標籤
    divs = soup.find_all('div', class_='text-wrap')

    # 儲存所有的 href 和 title
    domains = []
    titles = []    
    hrefs = []

    for div in divs:
        # 找到每個 div 中的 a 標籤
        a = div.find('a')

        # 將 href 和 title 加到相對應的列表中
        hrefs.append(a['href'])
        titles.append(a['title'])
        domains.append(domain)

    """""DEBUG用，輸出html檔確認
    #移動到目錄
    os.chdir(Urls_Path)

    #存成html檔
    with open(domain + '_nextpage.html', 'w', encoding='utf-8') as f:
        f.write(html)
    """""

    # 關閉瀏覽器視窗
    driver.quit()

    return domains, titles, hrefs
