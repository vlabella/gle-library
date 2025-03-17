all: feynman_11.eps feynman_11.pdf feynman_11.png

feynman_11.eps: feynman_11.gle
	gle /device EPS /cairo feynman_11.gle

feynman_11.pdf: feynman_11.gle
	gle /device PDF /cairo feynman_11.gle

feynman_11.png: feynman_11.gle
	gle /device PNG /cairo /DPI 150 feynman_11.gle

clean:
	-del feynman_11.eps feynman_11.pdf feynman_11.png
	-rmdir /SQ .gle