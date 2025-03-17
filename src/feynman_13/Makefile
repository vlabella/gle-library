all: feynman_13.eps feynman_13.pdf feynman_13.png

feynman_13.eps: feynman_13.gle
	gle /device EPS /cairo feynman_13.gle

feynman_13.pdf: feynman_13.gle
	gle /device PDF /cairo feynman_13.gle

feynman_13.png: feynman_13.gle
	gle /device PNG /cairo /DPI 150 feynman_13.gle

clean:
	-del feynman_13.eps feynman_13.pdf feynman_13.png
	-rmdir /SQ .gle