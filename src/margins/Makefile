all: margins.eps margins.pdf margins.png

margins.eps: margins.gle
	gle /device EPS /cairo margins.gle

margins.pdf: margins.gle
	gle /device PDF /cairo margins.gle

margins.png: margins.gle
	gle /device PNG /cairo /DPI 150 margins.gle

clean:
	-del margins.eps margins.pdf margins.png
	-rmdir /SQ .gle