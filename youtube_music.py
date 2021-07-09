import os
from youtube_dl import YoutubeDL
import progressbar
import urllib.request

current = (os.path.abspath('.'))
new = os.path.join(current, 'Download')

if os.path.isdir(new) == False:
	os.mkdir(new)



audio_downloader = YoutubeDL({
	'format':'m4a', 
	'quiet': True, 
	'no_warnings': True, 
	'outtmpl': new+'/%(title)s.%(ext)s'})

youtube = []

def start():

	count = 0
	bar = progressbar.ProgressBar(max_value=len(youtube))

	for url in youtube:
		count += 1
		bar.update(count)
		try:	
			audio_downloader.extract_info(url)
		except Exception:
			print("Couldn\'t download the audio", count+1)

while True:
	s = input('請輸入影片網址,或輸入menu進入選單: ')

	if s == 'menu':
		print('\n',s.center(29,'-'),'\n')
		print('  list : 查看已加入影片清單')
		print('  epty : 清空已加入影片清單')
		print('  quit : 終止程式')
		print('  start: 開始下載')
		print('  或按任意鍵回到上一頁\n')
		print(s.center(29,'-'),'\n')
		cmd = input('請輸入指令: ')

		if cmd == 'list':
			count = 1
			for s in youtube:
				print(count, '.', s)
				count += 1

		elif cmd =='epty':
			youtube.clear()

		elif cmd == 'quit':
			exit()

		elif cmd == 'start':
			start()

	elif s == 'start':
		start()

	else:
		try:
			status = urllib.request.urlopen(s).code		
			print(status)
			youtube.append(s)
		except Exception as err:
			print('\n這似乎不是個網址,請輸入正確網址...\n')
		



		