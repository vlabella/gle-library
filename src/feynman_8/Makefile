all: feynman_8.eps feynman_8.pdf feynman_8.png

feynman_8.eps: feynman_8.gle
	gle /device EPS /cairo feynman_8.gle

feynman_8.pdf: feynman_8.gle
	gle /device PDF /cairo feynman_8.gle

feynman_8.png: feynman_8.gle
	gle /device PNG /cairo /DPI 150 feynman_8.gle

clean:
	-del feynman_8.eps feynman_8.pdf feynman_8.png
	-rmdir /SQ .gle