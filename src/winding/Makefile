all: winding.eps winding.pdf winding.png

winding.eps: winding.gle
	gle /device EPS /cairo winding.gle

winding.pdf: winding.gle
	gle /device PDF /cairo winding.gle

winding.png: winding.gle
	gle /device PNG /cairo /DPI 150 winding.gle

clean:
	-del winding.eps winding.pdf winding.png
	-rmdir /SQ .gle