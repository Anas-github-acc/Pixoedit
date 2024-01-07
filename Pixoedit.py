def change():
	swt=[]#switch pixel data
	sys.stdout.write("For help type: _help()\nType f/F to finish feeding\n")
	while True:
		try:
			mxn=input("Target Pixel ("+mode+" mode) & Replacing pixel:\n")
			if(mxn.upper()=="F"):
				break
			if(mxn[0]=="_"):
				if(mxn[-2:]=="()"):
					eval(mxn)
				else:
					eval(mxn+"()")
				continue
			mxn=mxn.split(" ")
			sv,mxn=mxn[-1],mxn[0]
			if(mxn[0]=="("):
				mxn=eval(mxn)
			else:
				sys.stderr.write("----Unexpected target pixel----\n'")
				continue
			if(sv[0]=="("):
				sv=eval(sv)
				swt+=[[mxn,sv]]
				system('clear')
				shows(swt)
			else:
				sys.stderr.write("----Unexpected replacing pixel---\n")
		except:
			sys.stderr.write("----Unexpected Input----\n")
	lst=[]
	x,y=im.size
	xy=x*y
	pr=-1
	#Search Algorithm
	for i in range(x):
		for j in range(y):
			pt=p[i,j]
			for i1 in range(len(swt)):
				fg=[]
				mxn=swt[i1][0]
				sv=swt[i1][1]
				for e in range(len(mxn)):
					if(str(type(mxn[e]))=="<class 'int'>"):
						fg+=[pt[e]==mxn[e]]
					elif(len(mxn[0])==2):
						fg+=[(pt[e]<=mxn[e][0] and \
						pt[e]>=mxn[e][1])]
					else:
						sys.stderr.write("----Range must be two number list----\n")
						return 1
				c=True
				for ci in range(len(fg)):
					c=c and fg[ci]
				if(c):
					p[i,j]=sv
				pg=int((i*(y+1)+i+1)/(xy)*100)
				if(pr<pg):
					system("clear")
					sys.stdout.write("|"*(pg//2)+" "*(50-(pg//2))+" "+str(pg)+"%\n")
					pr=pg
	return 0

def creating_cf():
	from datetime import datetime as dt
	n=dt.now()
	a="switched_"+n.strftime("(%d-%m-%Y)%H:%M:%S")
	return a

def _help():
	help="""Enter the target pixel and replacing pixel
 e.g.,(R,G,B) (R,G,B):
	 px=(100,100,45)
	 if alpha(rgba) then add it also
	*To add range:
	 Write this [max,min] at the possition of R/G/B\n
	 px=([255,0],[255,0],[255,0])
	*Passing 1 or 2 element:
	  if 1 then (255,) = (255,[255,0],[255,0])
	  if 2 then (255,20) =(255,20,[255,0])
	*In more than two inputs:
	  order of preferenxe:
	   last > first\n"""
	sys.stdout.write(help)
	return "C"

def shows(swt):
	for dt in range(len(swt)):
		sys.stdout.write(str(dt)+": "+str(swt[dt][0])+"=>"+str(swt[dt][1])+"\n")
		return 0

from PIL import Image
from os import system
import sys

dict={'rgb':'.jpeg',
'rgba':'.png'}
while True:
		try:
			lc=input("Image Location:")
			if(lc.upper()=="D"):
				lc="Images.jpg"
			im = Image.open(lc)
			break
		except:
			sys.stderr.write("----No such file or maybe wrong file type----\n")
			continue
while True:
	mode=input(" Mode? opt:\n  1 'rgb'\n  2 'rgba'\n Type : ")
	if(mode not in dict):
		sys.stdout.write("----Mode is not Available----\n")
		continue
	if(mode!=im.mode):
		im=im.convert(mode.upper())
	break
p=im.load()
wr=1
while(wr):
	try:
		wr=change()
	except:
		sys.stdout.write("----replacing pixel cannot be two element----\n\n")
cmp=creating_cf()
cmp+=dict[mode]
im.save(cmp)
sys.stdout.write("SAVED SUCCESSFULLY  :"+cmp)