all: saddle.eps saddle.pdf saddle.png

saddle.eps: saddle.gle
	gle /device EPS /cairo saddle.gle

saddle.pdf: saddle.gle
	gle /device PDF /cairo saddle.gle

saddle.png: saddle.gle
	gle /device PNG /cairo /DPI 150 saddle.gle

clean:
	-del saddle.eps saddle.pdf saddle.png
	-rmdir /SQ .gle