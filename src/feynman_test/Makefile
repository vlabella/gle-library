all: feynman_test.eps feynman_test.pdf feynman_test.png

feynman_test.eps: feynman_test.gle
	gle /device EPS /cairo feynman_test.gle

feynman_test.pdf: feynman_test.gle
	gle /device PDF /cairo feynman_test.gle

feynman_test.png: feynman_test.gle
	gle /device PNG /cairo /DPI 150 feynman_test.gle

clean:
	-del feynman_test.eps feynman_test.pdf feynman_test.png
	-rmdir /SQ .gle