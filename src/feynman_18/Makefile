all: feynman_18.eps feynman_18.pdf feynman_18.png

feynman_18.eps: feynman_18.gle
	gle /device EPS /cairo feynman_18.gle

feynman_18.pdf: feynman_18.gle
	gle /device PDF /cairo feynman_18.gle

feynman_18.png: feynman_18.gle
	gle /device PNG /cairo /DPI 150 feynman_18.gle

clean:
	-del feynman_18.eps feynman_18.pdf feynman_18.png
	-rmdir /SQ .gle