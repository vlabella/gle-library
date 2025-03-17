all: math.eps math.pdf math.png

math.eps: math.gle
	gle /device EPS /cairo math.gle

math.pdf: math.gle
	gle /device PDF /cairo math.gle

math.png: math.gle
	gle /device PNG /cairo /DPI 150 math.gle

clean:
	-del math.eps math.pdf math.png
	-rmdir /SQ .gle