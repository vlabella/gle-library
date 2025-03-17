all: feynman_4.eps feynman_4.pdf feynman_4.png

feynman_4.eps: feynman_4.gle
	gle /device EPS /cairo feynman_4.gle

feynman_4.pdf: feynman_4.gle
	gle /device PDF /cairo feynman_4.gle

feynman_4.png: feynman_4.gle
	gle /device PNG /cairo /DPI 150 feynman_4.gle

clean:
	-del feynman_4.eps feynman_4.pdf feynman_4.png
	-rmdir /SQ .gle