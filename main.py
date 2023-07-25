import get_all_course_link
import get_dm_content
import upload_2_google


def main():

    domains = ['ICT智慧資通訊','SMA智慧機械','BIM生技醫藥','SGE智慧電網與綠能','NZS淨零永續','TEM科技管理']
    urls = ['https://college.itri.org.tw/Home/LessonList?PSId=EFAA5C9C-1925-4F9D-AF7E-B7CDC5E9831B',
    #    'https://college.itri.org.tw/Home/LessonList?PSId=C3AB64FD-3340-4741-8BAA-73D7A98DF205',
    #    'https://college.itri.org.tw/Home/LessonList?PSId=89E8416D-B920-4D2C-A7D9-493C1042FADD',
    #    'https://college.itri.org.tw/Home/LessonList?PSId=86167EA6-7168-4B22-A9AC-9A33E4406563',
    #    'https://college.itri.org.tw/Home/LessonList?PSId=9DE28893-E25F-43B6-8C16-F50613DD592D',
    #    'https://college.itri.org.tw/Home/LessonList?PSId=40C7B6BD-5268-4AAD-BDE4-C3DD9A0FA5AF'
        ]

    for domain, url in zip(domains, urls):
        titles, hrefs = get_all_course_link.get_links(domain,url)
        upload_2_google.write_columeABC(domain, titles, hrefs)
        get_dm_content.func(titles, hrefs)
        
        #智慧機械1頁超過100個，故需要跳下一頁
        if domain == 'SMA智慧機械' :
            titles, hrefs = get_all_course_link.get_nextpage_links(domain,url)
            get_dm_content.func(titles, hrefs)



if __name__ == '__main__':
    main()
