all: shadow.eps shadow.pdf shadow.png

shadow.eps: shadow.gle
	gle /device EPS /cairo shadow.gle

shadow.pdf: shadow.gle
	gle /device PDF /cairo shadow.gle

shadow.png: shadow.gle
	gle /device PNG /cairo /DPI 150 shadow.gle

clean:
	-del shadow.eps shadow.pdf shadow.png
	-rmdir /SQ .gle