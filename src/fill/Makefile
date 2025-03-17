all: fill.eps fill.pdf fill.png

fill.eps: fill.gle
	gle /device EPS /cairo fill.gle

fill.pdf: fill.gle
	gle /device PDF /cairo fill.gle

fill.png: fill.gle
	gle /device PNG /cairo /DPI 150 fill.gle

clean:
	-del fill.eps fill.pdf fill.png
	-rmdir /SQ .gle