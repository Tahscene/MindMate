from requests_html import HTMLSession

def weather():
    s = HTMLSession()
    query="dhaka"
    url = f'https://www.google.com/search?q=weather+{query}'
    
    try:
        r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'})
        
       
        temp = r.html.find('span#wob_tm', first=True)
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc = r.html.find('span#wob_dc', first=True)

        if temp and unit and desc:
            return temp.text, unit.text, desc.text
        else:
            return None, None, "Could not fetch the weather details."

    except Exception as e:
        return None, None, f"An error occurred: {str(e)}"

temperature, unit, description = weather()
print(f"Temperature: {temperature} {unit}")
print(f"Description: {description}")
