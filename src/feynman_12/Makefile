all: feynman_12.eps feynman_12.pdf feynman_12.png

feynman_12.eps: feynman_12.gle
	gle /device EPS /cairo feynman_12.gle

feynman_12.pdf: feynman_12.gle
	gle /device PDF /cairo feynman_12.gle

feynman_12.png: feynman_12.gle
	gle /device PNG /cairo /DPI 150 feynman_12.gle

clean:
	-del feynman_12.eps feynman_12.pdf feynman_12.png
	-rmdir /SQ .gle