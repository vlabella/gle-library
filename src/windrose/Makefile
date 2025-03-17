all: windrose.eps windrose.pdf windrose.png

windrose.eps: windrose.gle
	gle /device EPS /cairo windrose.gle

windrose.pdf: windrose.gle
	gle /device PDF /cairo windrose.gle

windrose.png: windrose.gle
	gle /device PNG /cairo /DPI 150 windrose.gle

clean:
	-del windrose.eps windrose.pdf windrose.png
	-rmdir /SQ .gle