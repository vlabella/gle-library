all: horizon.eps horizon.pdf horizon.png

horizon.eps: horizon.gle
	gle /device EPS /cairo horizon.gle

horizon.pdf: horizon.gle
	gle /device PDF /cairo horizon.gle

horizon.png: horizon.gle
	gle /device PNG /cairo /DPI 150 horizon.gle

clean:
	-del horizon.eps horizon.pdf horizon.png
	-rmdir /SQ .gle