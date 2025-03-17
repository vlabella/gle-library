all: gradient.eps gradient.pdf gradient.png

gradient.eps: gradient.gle
	gle /device EPS /cairo gradient.gle

gradient.pdf: gradient.gle
	gle /device PDF /cairo gradient.gle

gradient.png: gradient.gle
	gle /device PNG /cairo /DPI 150 gradient.gle

clean:
	-del gradient.eps gradient.pdf gradient.png
	-rmdir /SQ .gle