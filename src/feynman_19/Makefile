all: feynman_19.eps feynman_19.pdf feynman_19.png

feynman_19.eps: feynman_19.gle
	gle /device EPS /cairo feynman_19.gle

feynman_19.pdf: feynman_19.gle
	gle /device PDF /cairo feynman_19.gle

feynman_19.png: feynman_19.gle
	gle /device PNG /cairo /DPI 150 feynman_19.gle

clean:
	-del feynman_19.eps feynman_19.pdf feynman_19.png
	-rmdir /SQ .gle