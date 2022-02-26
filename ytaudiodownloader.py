import os

def getAudio(link):
	from pytube import YouTube
	yt = YouTube(link)
	my = yt.streams.filter(only_audio=True)
	final = []
	for count,i in enumerate (my):
		list_ok = (str(str(str(i).replace("<",""))).replace(">","").split(" "))
		list_ok.pop(0)
		itag = str(str(list_ok[0]).replace('itag="',"")). replace ('"',"")		
		abr = str(str(list_ok[2]).replace('abr="',"")). replace ('"',"")
		final.append((abr,yt.streams.get_by_itag(int(itag)),yt.title))
	return final


Types = getAudio(input("Enter the video url : "))
print()
for count,i in enumerate ( Types):
	abr,stream,name=i
	print(str(count+1)+". Quality : "+f"{abr}")
a = int(input(f"\nEnter the quality to download [1-{len(Types)}] : "))
abr, stream,title=Types[a-1]

out_file = stream.download()
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 
print(f"\nSaved as : {new_file}")
