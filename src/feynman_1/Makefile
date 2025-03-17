all: feynman_1.eps feynman_1.pdf feynman_1.png

feynman_1.eps: feynman_1.gle
	gle /device EPS /cairo feynman_1.gle

feynman_1.pdf: feynman_1.gle
	gle /device PDF /cairo feynman_1.gle

feynman_1.png: feynman_1.gle
	gle /device PNG /cairo /DPI 150 feynman_1.gle

clean:
	-del feynman_1.eps feynman_1.pdf feynman_1.png
	-rmdir /SQ .gle