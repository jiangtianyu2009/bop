import urllib.request

vericode_url = 'https://wappass.baidu.com/cgi-bin/genimage?njGc306e2363599de0402681597de01c51387b5a60637020058&v=1528187871070'

counter = 1000

while counter < 1100:
    urllib.request.urlretrieve(
        vericode_url, r'C:\Users\jiangt6\Desktop\vericode\p' + str(counter) + r'.jpg')
    counter = counter + 1
