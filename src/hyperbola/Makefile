all: hyperbola.eps hyperbola.pdf hyperbola.png

hyperbola.eps: hyperbola.gle
	gle /device EPS /cairo hyperbola.gle

hyperbola.pdf: hyperbola.gle
	gle /device PDF /cairo hyperbola.gle

hyperbola.png: hyperbola.gle
	gle /device PNG /cairo /DPI 150 hyperbola.gle

clean:
	-del hyperbola.eps hyperbola.pdf hyperbola.png
	-rmdir /SQ .gle