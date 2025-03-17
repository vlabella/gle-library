all: feynman_5.eps feynman_5.pdf feynman_5.png

feynman_5.eps: feynman_5.gle
	gle /device EPS /cairo feynman_5.gle

feynman_5.pdf: feynman_5.gle
	gle /device PDF /cairo feynman_5.gle

feynman_5.png: feynman_5.gle
	gle /device PNG /cairo /DPI 150 feynman_5.gle

clean:
	-del feynman_5.eps feynman_5.pdf feynman_5.png
	-rmdir /SQ .gle