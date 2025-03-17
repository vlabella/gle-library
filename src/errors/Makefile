all: errors.eps errors.pdf errors.png

errors.eps: errors.gle
	gle /device EPS /cairo errors.gle

errors.pdf: errors.gle
	gle /device PDF /cairo errors.gle

errors.png: errors.gle
	gle /device PNG /cairo /DPI 150 errors.gle

clean:
	-del errors.eps errors.pdf errors.png
	-rmdir /SQ .gle