all: feynman_16.eps feynman_16.pdf feynman_16.png

feynman_16.eps: feynman_16.gle
	gle /device EPS /cairo feynman_16.gle

feynman_16.pdf: feynman_16.gle
	gle /device PDF /cairo feynman_16.gle

feynman_16.png: feynman_16.gle
	gle /device PNG /cairo /DPI 150 feynman_16.gle

clean:
	-del feynman_16.eps feynman_16.pdf feynman_16.png
	-rmdir /SQ .gle