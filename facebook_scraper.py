from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

def facebook_login(email, password):
    driver = webdriver.Chrome() 
    driver.get("https://www.facebook.com/")
    
    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "pass")
    
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5)  

    return driver

email = ""
password = ""
driver = facebook_login(email, password)

search_keyword = "Hải Phòng"
search_url = f"https://www.facebook.com/search/top/?q={search_keyword}"
driver.get(search_url)
time.sleep(5)  

search_results_page = driver.page_source

soup = BeautifulSoup(search_results_page, 'html.parser')

posts = soup.find_all('div', class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')

for post in posts:
    try:
        user_id = post.find('a')['href'].split('/')[3]  
        print("User ID:", user_id)
    except Exception as e:
        continue

try:
    print("Chương trình đang chạy. Nhấn Ctrl+C để dừng.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Chương trình đã dừng.")
    driver.quit()
