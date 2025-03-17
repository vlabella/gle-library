all: feynman_9.eps feynman_9.pdf feynman_9.png

feynman_9.eps: feynman_9.gle
	gle /device EPS /cairo feynman_9.gle

feynman_9.pdf: feynman_9.gle
	gle /device PDF /cairo feynman_9.gle

feynman_9.png: feynman_9.gle
	gle /device PNG /cairo /DPI 150 feynman_9.gle

clean:
	-del feynman_9.eps feynman_9.pdf feynman_9.png
	-rmdir /SQ .gle