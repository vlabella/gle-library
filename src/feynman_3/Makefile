all: feynman_3.eps feynman_3.pdf feynman_3.png

feynman_3.eps: feynman_3.gle
	gle /device EPS /cairo feynman_3.gle

feynman_3.pdf: feynman_3.gle
	gle /device PDF /cairo feynman_3.gle

feynman_3.png: feynman_3.gle
	gle /device PNG /cairo /DPI 150 feynman_3.gle

clean:
	-del feynman_3.eps feynman_3.pdf feynman_3.png
	-rmdir /SQ .gle