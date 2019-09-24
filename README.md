url = 'https://www.instagram.com/{}/'.format(PUBLIC_USER)
path = 'C:/users/{}/Desktop/'.format(YOUR_USERNAME)
ins = InstaScrape(path)
ins.getinfo(url,to_txt=True)

OR

ins.getinfo(url)
