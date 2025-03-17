all: sierpinski.eps sierpinski.pdf sierpinski.png

sierpinski.eps: sierpinski.gle
	gle /device EPS /cairo sierpinski.gle

sierpinski.pdf: sierpinski.gle
	gle /device PDF /cairo sierpinski.gle

sierpinski.png: sierpinski.gle
	gle /device PNG /cairo /DPI 150 sierpinski.gle

clean:
	-del sierpinski.eps sierpinski.pdf sierpinski.png
	-rmdir /SQ .gle