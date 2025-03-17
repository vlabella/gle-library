all: feynman_15.eps feynman_15.pdf feynman_15.png

feynman_15.eps: feynman_15.gle
	gle /device EPS /cairo feynman_15.gle

feynman_15.pdf: feynman_15.gle
	gle /device PDF /cairo feynman_15.gle

feynman_15.png: feynman_15.gle
	gle /device PNG /cairo /DPI 150 feynman_15.gle

clean:
	-del feynman_15.eps feynman_15.pdf feynman_15.png
	-rmdir /SQ .gle