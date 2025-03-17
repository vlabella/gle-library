all: zoom-in.eps zoom-in.pdf zoom-in.png

zoom-in.eps: zoom-in.gle
	gle /device EPS /cairo zoom-in.gle

zoom-in.pdf: zoom-in.gle
	gle /device PDF /cairo zoom-in.gle

zoom-in.png: zoom-in.gle
	gle /device PNG /cairo /DPI 150 zoom-in.gle

clean:
	-del zoom-in.eps zoom-in.pdf zoom-in.png
	-rmdir /SQ .gle