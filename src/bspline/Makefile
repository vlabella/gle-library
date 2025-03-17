all: bspline.eps bspline.pdf bspline.png

bspline.eps: bspline.gle
	gle /device EPS /cairo bspline.gle

bspline.pdf: bspline.gle
	gle /device PDF /cairo bspline.gle

bspline.png: bspline.gle
	gle /device PNG /cairo /DPI 150 bspline.gle

clean:
	-del bspline.eps bspline.pdf bspline.png
	-rmdir /SQ .gle