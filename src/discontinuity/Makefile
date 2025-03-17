all: discontinuity.eps discontinuity.pdf discontinuity.png

discontinuity.eps: discontinuity.gle
	gle /device EPS /cairo discontinuity.gle

discontinuity.pdf: discontinuity.gle
	gle /device PDF /cairo discontinuity.gle

discontinuity.png: discontinuity.gle
	gle /device PNG /cairo /DPI 150 discontinuity.gle

clean:
	-del discontinuity.eps discontinuity.pdf discontinuity.png
	-rmdir /SQ .gle