from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
option.add_argument("start-maximized")

song = input('What song would you like to listen? ')
index_url = '+'.join(song.split())
search_url = 'https://music.youtube.com/search?q=' + index_url 
print('\nSearching for the song...')

driver = webdriver.Chrome(executable_path=r'E:\Games\FILES\chromedriver_brave.exe', options=option)    
driver.maximize_window()
driver.get(search_url)
driver.implicitly_wait(5)

driver.find_element_by_class_name('left-items').click()
print(f'\nPlaying {song}...')
 
try:
    driver.find_element_by_xpath('//*[@id="right-controls"]/div/tp-yt-paper-icon-button[1]').click()
    driver.find_element_by_class_name('ytp-ad-image')    
    time.sleep(5)   
    skip_ad = driver.find_element_by_id('ad-text:6')
    skip_ad.click()  
    driver.find_element_by_xpath('//*[@id="right-controls"]/div/tp-yt-paper-icon-button[1]').click()
except:
    driver.find_element_by_xpath('//*[@id="right-controls"]/div/tp-yt-paper-icon-button[1]').click()
    print('\nNo ads encountered.')  
else:
    print('\noops! An ad encountered. Please wait a few seconds...')    

def song_len():
    mmss = driver.find_element_by_class_name('time-info').text.split()[-1]
    a = mmss.split(':')
    m,s = a[0],a[-1]
    seconds = int(m)*60+int(s)
    return (seconds)

driver.minimize_window()
print(f'\nExiting selenium after {song_len()} seconds')
time.sleep(song_len())
# time.sleep(10)
driver.close()




