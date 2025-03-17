all: feynman_shadow.eps feynman_shadow.pdf feynman_shadow.png

feynman_shadow.eps: feynman_shadow.gle
	gle /device EPS /cairo feynman_shadow.gle

feynman_shadow.pdf: feynman_shadow.gle
	gle /device PDF /cairo feynman_shadow.gle

feynman_shadow.png: feynman_shadow.gle
	gle /device PNG /cairo /DPI 150 feynman_shadow.gle

clean:
	-del feynman_shadow.eps feynman_shadow.pdf feynman_shadow.png
	-rmdir /SQ .gle