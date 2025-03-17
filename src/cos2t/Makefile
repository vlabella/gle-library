all: cos2t.eps cos2t.pdf cos2t.png

cos2t.eps: cos2t.gle
	gle /device EPS /cairo cos2t.gle

cos2t.pdf: cos2t.gle
	gle /device PDF /cairo cos2t.gle

cos2t.png: cos2t.gle
	gle /device PNG /cairo /DPI 150 cos2t.gle

clean:
	-del cos2t.eps cos2t.pdf cos2t.png
	-rmdir /SQ .gle