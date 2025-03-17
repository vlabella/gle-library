all: curve.eps curve.pdf curve.png

curve.eps: curve.gle
	gle /device EPS /cairo curve.gle

curve.pdf: curve.gle
	gle /device PDF /cairo curve.gle

curve.png: curve.gle
	gle /device PNG /cairo /DPI 150 curve.gle

clean:
	-del curve.eps curve.pdf curve.png
	-rmdir /SQ .gle