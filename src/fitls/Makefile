all: fitls.eps fitls.pdf fitls.png

fitls.eps: fitls.gle
	gle /device EPS /cairo fitls.gle

fitls.pdf: fitls.gle
	gle /device PDF /cairo fitls.gle

fitls.png: fitls.gle
	gle /device PNG /cairo /DPI 150 fitls.gle

clean:
	-del fitls.eps fitls.pdf fitls.png
	-rmdir /SQ .gle