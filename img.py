from PIL import Image
import os

for file in os.listdir('orig'):# 讀取orig資料夾裡面的檔案
	if file.endswith('.jpg'):
		with Image.open(os.path.join('orig', file)) as im:
			im = im.convert("L") #轉換成黑白
			im = im.save(os.path.join('result', file[:-4] + '_mono.jpg')) #[-4]:倒數第四個位置到結尾都去掉(清單分割法)