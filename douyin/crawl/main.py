from selenium.webdriver import Chrome
import os, sys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
url = "https://www.douyin.com/search/{}?aid=9d40feab-4eb2-4977-86f7-ab523d593d65&publish_time=0&sort_type=0&source=search_sug&type=video"
url2 = "https://www.douyin.com/search/{}?publish_time=7&sort_type=0&source=search_sug&type=video"
driver = Chrome(executable_path='../pack/chromedriver.exe', chrome_options=chrome_options)

keywords = ['狗子',"帽子","猫子",'足球']

import time
from otils import sscroll, sfindes, sget_attr, sfinde, stext, Writer


def get_video_list():
    login = False
    scroll_num = 4
    video_page = []
    for word in keywords:
        driver.get(url2.format(word))
        cnt = 0
        if not login:
            input("登录后ENTER")
            login = True

        driver.refresh()
        dis = 5000
        while cnt < scroll_num:
            sscroll(driver, dis)
            time.sleep(2)
            cnt += 1
            dis *= cnt

        elems = sfindes(driver, '//a')
        f = open("result.txt", "w")
        for e in elems:
            href = sget_attr(e, 'href')

            print("href", e)
            if href:
                f.write(f"{href},{word}\n")
                if 'www.douyin.com/video' in href:
                    host = href.split("?")[0]
                    video_page.append((host, word))
        f.close()
    return video_page


video_tags = {
    'video_date_x': '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/span',
    'video_title_x': '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/h1/span[2]',
    'video_awesome_x': "/html/body/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[1]/span",
    'video_comment_x': "/html/body/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span",
    'video_fans_x': "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/p/span[2]",
    'video_all_awesome_x': "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/p/span[4]",
    'video_name_x': "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/a/div/span/span/span/span/span",
    'video_dy_link_x': ["/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/a"],
}


def video_info(video_data):
    """

    :param video_data: [(url,word)]
    :return: [{**video_tags}]
    """
    res = []
    for url, word in video_data:
        driver.get(url)
        item = {'video_url': url.split('?')[0], 'keyword': word}
        for name, xpath in video_tags.items():
            if isinstance(xpath, list):
                text = sget_attr(sfinde(driver, xpath[0]), 'href')
            else:
                text = stext(sfinde(driver, xpath))

            print(name, xpath, text)
            item[name] = text or ''
        print(item)
        res.append(item)
        time.sleep(3)
    if res:
        with open("video_result.txt", 'a', encoding='utf8') as f:
            f.write('\n'.join([str(i) for i in res]))
            f.write("\n")

    return res


user_tags = {
    'user_name_x': '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[2]/h1/span/span/span/span/span',
    'user_code_x': '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/p[1]',
    'user_desc_x': '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/p[2]/span',
    'user_fans_x': '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]',
    'user_care_x': '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]',
    'user_awesome_x': '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]',
    'user_piece_x': '//*[@id="root"]/div/div[2]/div/div[4]/div[1]/div[1]/div[1]/span',
}


def user_info(user_urls):
    done = {}
    res = []
    for url in user_urls:
        if url in done:
            print("跳过")
            print(url)
            print("="*100)
            res.append(done[url])
            continue

        driver.get(url)
        item = {}
        for name, xpath in user_tags.items():
            if isinstance(xpath, list):
                text = sget_attr(sfinde(driver, xpath[0]), 'href')
            else:
                text = stext(sfinde(driver, xpath))

            print(name, xpath, text)
            item[name] = text or ''

        print(item)
        res.append(item)
        done[url]=item
        time.sleep(3)
    if res:
        with open("user_result.txt", 'a', encoding='utf8') as f:
            f.write('\n'.join(str(i) for i in res))
            f.write("\n")

    return res

import json

title_map = {
    'video_url':'视频URL',
    'keyword':'关键词',
    'video_date_x':'日期',
    'video_title_x':'标题',
    'video_awesome_x':'视频点赞数',
    'video_comment_x':'视频评论数',
    'video_fans_x':'视频页粉丝数',
    'video_all_awesome_x':'视频页获赞总数',
    'video_name_x':'视频页作者名称',
    'video_dy_link_x':'视频页URL',
    'user_name_x':'用户名称',
    'user_code_x':'用户页-抖音号',
    'user_desc_x':'用户页-描述',
    'user_fans_x':'用户页-粉丝数',
    'user_care_x':'用户页-关注数',
    'user_awesome_x':'用户页-点赞数',
    'user_piece_x':'用户页作品数',
}

def main():
    video_page = get_video_list()
    video_page = set(video_page)
    video_data = video_info(video_page)
    user_urls = [i['video_dy_link_x'] for i in video_data if 'video_dy_link_x' in i]
    user_data = user_info(user_urls)
    data = [{**v, **u} for v, u in zip(video_data, user_data)]
    if data:
        with open('final.txt', 'a', encoding='utf8') as f:
            f.write('\n'.join(json.dumps(i) for i in data))
            f.write("\n")

        keys = list(data[0].keys())
        xlsx_data = [[item.get(k, '') for k in keys] for item in data]
        xlsx_data.insert(0, [title_map[i] for i in keys])
        try:
            w = Writer(f"douyin_{int(time.time())}", 'xlsx')
            w.write(xlsx_data)
        except Exception as ee:
            print(ee)
    driver.close()


if __name__ == '__main__':
    main()

# user_urls = ['https://www.douyin.com/user/MS4wLjABAAAAc1YsdbTrE2SZfusNBxDaSkwymER3iK8dDen4n8wmZWM?enter_method=video_title&author_id=62736935305&group_id=6982525283433860386&log_pb=%7B%22impr_id%22%3A%22021625765827216fdbd400a040000000a7040920000016df075e4%22%7D&enter_from=video_detail']
# user_info(user_urls)
# video_urls=["https://www.douyin.com/video/6982525283433860386?previous_page=search_result&extra_params=%7B%22search_id%22%3A%222021070901100801021206814350269ACE%22%2C%22search_result_id%22%3A%226982525283433860386%22%2C%22search_type%22%3A%22video%22%2C%22search_keyword%22%3A%22%E5%AE%A0%E7%89%A9%E7%8C%AB%22%7D","https://www.douyin.com/video/6982525283433860386?previous_page=search_result&extra_params=%7B%22search_id%22%3A%222021070901100801021206814350269ACE%22%2C%22search_result_id%22%3A%226982525283433860386%22%2C%22search_type%22%3A%22video%22%2C%22search_keyword%22%3A%22%E5%AE%A0%E7%89%A9%E7%8C%AB%22%7D"]
# video_info(video_urls)
## 时间 关键词 链接 点赞 评论 转发 抖音号 抖音号名称 标题
#
# # 视频链接内
# video_url = ''
# video_date = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/span'
# video_title = '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/h1/span[2]'
# video_awesome = "/html/body/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[1]/span"
# video_comment = "/html/body/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span"
# video_fans = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/p/span[2]"
# video_all_awesome = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/p/span[4]"
# video_name = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/a/div/span/span/span/span/span"
# video_dy_link = "/html/body/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/a"
#
# # 个人抖音内
# user_name = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[2]/h1/span/span/span/span/span'
# user_code = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/p[1]'
# user_desc = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/p[2]/span'
# user_fans = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]'
# user_care = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]'
# user_awesome = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]'
# user_piece = '//*[@id="root"]/div/div[2]/div/div[4]/div[1]/div[1]/div[1]/span'
