import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# page 별로 50개씩 크롤링!
def page_crawl(key, url):
    
    music={"genre" : [], 
           "song_name" : [],
           "artist" : [],
           "lyric" : [] }
    
    for i in range(1, 51):
        
        # 장르
        music["genre"].append(key)
        
        # 사이트 접속
        driver.get(url)
        time.sleep(10)
        
        # 곡 정보 클릭
        driver.find_element(By.CSS_SELECTOR, f"#frm > div > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > a").click()
        time.sleep(5)
        
        # 노래제목
        song_name = driver.find_element(By.CSS_SELECTOR, "#downloadfrm > div > div > div.entry > div.info > div.song_name").text
        print(song_name)
        music["song_name"].append(song_name)
        
        # 가수
        artist = driver.find_element(By.CSS_SELECTOR, "#downloadfrm > div > div > div.entry > div.info > div.artist").text
        music["artist"].append(artist)
        
        # 펼치기 클릭
        try:
            driver.find_element(By.CSS_SELECTOR, "#lyricArea > button").click()
            time.sleep(3)
            # 가사          
            lyric = driver.find_element(By.CSS_SELECTOR, "#d_video_summary").text
            music["lyric"].append(lyric)
            time.sleep(1)
        except:
            music["lyric"].append("가사없음")
            time.sleep(1)
        
    return music
        

# 크롬드라이버 실행
driver = webdriver.Chrome('chromedriver') 

melon_url = 'https://www.melon.com/genre/song_list.htm?gnrCode=GN0'
genre = {"발라드": "100",
        "랩/힙합": "300", 
        "R&B/Soul": "400", 
        "인디음악": "500",
        "록/메탈": "600", 
        "포크/블루스": "800"}
steady = "&steadyYn=Y"


df = pd.DataFrame()

# 장르 돌아가면서 
for key, value in genre.items():
    
    # 1번부터 50번
    first_page_url = melon_url + value + steady
    music = page_crawl(key, first_page_url)
    df1 = pd.DataFrame(music)

    # 51번부터 100번
    second_page_url = first_page_url + "#params%5BgnrCode%5D=GN0" + value + "&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=NEW&params%5BsteadyYn%5D=Y&po=pageObj&startIndex=51"
    music = page_crawl(key, second_page_url)
    df2 = pd.DataFrame(music)
    
    
    # 기존 datafraem, 1번부터50번, 51번부터 100번 전부 합쳐서 하나의 dataframe 만들기!
    df = pd.concat([df, df1, df2], ignore_index=True)

# 그냥 출력해봄
print(df)

# csv파일로 내보내기
df.to_csv('data/music.csv', index=False)