all: feynman_6.eps feynman_6.pdf feynman_6.png

feynman_6.eps: feynman_6.gle
	gle /device EPS /cairo feynman_6.gle

feynman_6.pdf: feynman_6.gle
	gle /device PDF /cairo feynman_6.gle

feynman_6.png: feynman_6.gle
	gle /device PNG /cairo /DPI 150 feynman_6.gle

clean:
	-del feynman_6.eps feynman_6.pdf feynman_6.png
	-rmdir /SQ .gle