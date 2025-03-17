all: feynman_2.eps feynman_2.pdf feynman_2.png

feynman_2.eps: feynman_2.gle
	gle /device EPS /cairo feynman_2.gle

feynman_2.pdf: feynman_2.gle
	gle /device PDF /cairo feynman_2.gle

feynman_2.png: feynman_2.gle
	gle /device PNG /cairo /DPI 150 feynman_2.gle

clean:
	-del feynman_2.eps feynman_2.pdf feynman_2.png
	-rmdir /SQ .gle