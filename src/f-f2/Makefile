all: f-f2.eps f-f2.pdf f-f2.png

f-f2.eps: f-f2.gle
	gle /device EPS /cairo f-f2.gle

f-f2.pdf: f-f2.gle
	gle /device PDF /cairo f-f2.gle

f-f2.png: f-f2.gle
	gle /device PNG /cairo /DPI 150 f-f2.gle

clean:
	-del f-f2.eps f-f2.pdf f-f2.png
	-rmdir /SQ .gle