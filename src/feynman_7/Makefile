all: feynman_7.eps feynman_7.pdf feynman_7.png

feynman_7.eps: feynman_7.gle
	gle /device EPS /cairo feynman_7.gle

feynman_7.pdf: feynman_7.gle
	gle /device PDF /cairo feynman_7.gle

feynman_7.png: feynman_7.gle
	gle /device PNG /cairo /DPI 150 feynman_7.gle

clean:
	-del feynman_7.eps feynman_7.pdf feynman_7.png
	-rmdir /SQ .gle