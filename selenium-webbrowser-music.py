from selenium import webdriver
import webbrowser
webbrowser.get('windows-default')

option = webdriver.ChromeOptions()
option.binary_location = r'' # browser path
option.add_argument("start-maximized")

song = input('What song would you like to listen? ')
index_url = '+'.join(song.split())
search_url = 'https://music.youtube.com/search?q=' + index_url 
print('\nSearching for the song...')

driver = webdriver.Chrome(executable_path=r'', options=option) # driver path   
driver.maximize_window()
driver.get(search_url)
driver.implicitly_wait(5)

link = driver.find_element_by_css_selector('a[class="yt-simple-endpoint style-scope yt-formatted-string"]').get_attribute("href").split('&')[0]
driver.close()
print(f'\nPlaying {song}...')
link = list(link.partition('.'))
link[0] = 'https://'
link.remove('.')
link = ''.join(link)

webbrowser.open(link)
