all: feynman_17.eps feynman_17.pdf feynman_17.png

feynman_17.eps: feynman_17.gle
	gle /device EPS /cairo feynman_17.gle

feynman_17.pdf: feynman_17.gle
	gle /device PDF /cairo feynman_17.gle

feynman_17.png: feynman_17.gle
	gle /device PNG /cairo /DPI 150 feynman_17.gle

clean:
	-del feynman_17.eps feynman_17.pdf feynman_17.png
	-rmdir /SQ .gle