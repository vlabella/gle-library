all: ellipses.eps ellipses.pdf ellipses.png

ellipses.eps: ellipses.gle
	gle /device EPS /cairo ellipses.gle

ellipses.pdf: ellipses.gle
	gle /device PDF /cairo ellipses.gle

ellipses.png: ellipses.gle
	gle /device PNG /cairo /DPI 150 ellipses.gle

clean:
	-del ellipses.eps ellipses.pdf ellipses.png
	-rmdir /SQ .gle