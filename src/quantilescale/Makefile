all: quantilescale.eps quantilescale.pdf quantilescale.png

quantilescale.eps: quantilescale.gle
	gle /device EPS /cairo quantilescale.gle

quantilescale.pdf: quantilescale.gle
	gle /device PDF /cairo quantilescale.gle

quantilescale.png: quantilescale.gle
	gle /device PNG /cairo /DPI 150 quantilescale.gle

clean:
	-del quantilescale.eps quantilescale.pdf quantilescale.png
	-rmdir /SQ .gle