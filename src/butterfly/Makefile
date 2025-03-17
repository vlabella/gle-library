all: butterfly.eps butterfly.pdf butterfly.png

butterfly.eps: butterfly.gle
	gle /device EPS /cairo butterfly.gle

butterfly.pdf: butterfly.gle
	gle /device PDF /cairo butterfly.gle

butterfly.png: butterfly.gle
	gle /device PNG /cairo /DPI 150 butterfly.gle

clean:
	-del butterfly.eps butterfly.pdf butterfly.png
	-rmdir /SQ .gle