from requests_html import HTMLSession
import speech_text
#span id = wob_tm
def weather():
    
    s = HTMLSession()
    query = "rongai"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'})

    r.html.render(sleep=1, keep_page=True)

    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text 
    desc = r.html.find('span#wob_dc', first=True).text
    
    return temp + " " + unit + " " + desc

