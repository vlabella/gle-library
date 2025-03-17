all: ellipsearrow.eps ellipsearrow.pdf ellipsearrow.png

ellipsearrow.eps: ellipsearrow.gle
	gle /device EPS /cairo ellipsearrow.gle

ellipsearrow.pdf: ellipsearrow.gle
	gle /device PDF /cairo ellipsearrow.gle

ellipsearrow.png: ellipsearrow.gle
	gle /device PNG /cairo /DPI 150 ellipsearrow.gle

clean:
	-del ellipsearrow.eps ellipsearrow.pdf ellipsearrow.png
	-rmdir /SQ .gle