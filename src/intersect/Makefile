all: intersect.eps intersect.pdf intersect.png

intersect.eps: intersect.gle
	gle /device EPS /cairo intersect.gle

intersect.pdf: intersect.gle
	gle /device PDF /cairo intersect.gle

intersect.png: intersect.gle
	gle /device PNG /cairo /DPI 150 intersect.gle

clean:
	-del intersect.eps intersect.pdf intersect.png
	-rmdir /SQ .gle