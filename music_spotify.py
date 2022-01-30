from selenium import webdriver
from selenium.webdriver import ActionChains
import pyperclip as pc
import webbrowser
import pyautogui as pygui
import time
webbrowser.get('windows-default')

option = webdriver.ChromeOptions()
option.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
option.add_argument("start-maximized")

song = input('What song would you like to listen? ')
index_url = '%20'.join(song.split())
search_url = 'https://open.spotify.com/search/' + index_url 

print('\nSearching for the song...')

driver = webdriver.Chrome(executable_path=r'E:\Games\FILES\chromedriver_brave.exe', options=option) 

driver.get(search_url)
driver.implicitly_wait(5)
actionChains = ActionChains(driver)
actionChains.context_click(driver.find_element_by_class_name('_gB1lxCfXeR8_Wze5Cx9')).perform()
driver.implicitly_wait(5)

old_copy = pc.paste()
driver.find_element_by_xpath("//span[contains(text(), 'Share')]").click()

try:
    driver.find_element_by_xpath("//span[contains(text(), 'Copy Song Link')]").click()
    driver.close()
except:
    driver.find_element_by_xpath("//span[contains(text(), 'Copy link to artist')]").click()
    driver.close()
   
song_url = pc.paste()
webbrowser.open(song_url)
print(f'\nPlaying {song}...')
pc.copy(old_copy)
time.sleep(5)
pygui.leftClick(315,711)
 
        
