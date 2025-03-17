all: saddle-contour.eps saddle-contour.pdf saddle-contour.png

saddle-contour.eps: saddle-contour.gle
	gle /device EPS /cairo saddle-contour.gle

saddle-contour.pdf: saddle-contour.gle
	gle /device PDF /cairo saddle-contour.gle

saddle-contour.png: saddle-contour.gle
	gle /device PNG /cairo /DPI 150 saddle-contour.gle

clean:
	-del saddle-contour.eps saddle-contour.pdf saddle-contour.png
	-rmdir /SQ .gle