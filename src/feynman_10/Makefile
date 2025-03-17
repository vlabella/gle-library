all: feynman_10.eps feynman_10.pdf feynman_10.png

feynman_10.eps: feynman_10.gle
	gle /device EPS /cairo feynman_10.gle

feynman_10.pdf: feynman_10.gle
	gle /device PDF /cairo feynman_10.gle

feynman_10.png: feynman_10.gle
	gle /device PNG /cairo /DPI 150 feynman_10.gle

clean:
	-del feynman_10.eps feynman_10.pdf feynman_10.png
	-rmdir /SQ .gle