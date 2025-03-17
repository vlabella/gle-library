all: feynman_14.eps feynman_14.pdf feynman_14.png

feynman_14.eps: feynman_14.gle
	gle /device EPS /cairo feynman_14.gle

feynman_14.pdf: feynman_14.gle
	gle /device PDF /cairo feynman_14.gle

feynman_14.png: feynman_14.gle
	gle /device PNG /cairo /DPI 150 feynman_14.gle

clean:
	-del feynman_14.eps feynman_14.pdf feynman_14.png
	-rmdir /SQ .gle