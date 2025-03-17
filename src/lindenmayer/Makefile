all: lindenmayer.eps lindenmayer.pdf lindenmayer.png

lindenmayer.eps: lindenmayer.gle
	gle /device EPS /cairo lindenmayer.gle

lindenmayer.pdf: lindenmayer.gle
	gle /device PDF /cairo lindenmayer.gle

lindenmayer.png: lindenmayer.gle
	gle /device PNG /cairo /DPI 150 lindenmayer.gle

clean:
	-del lindenmayer.eps lindenmayer.pdf lindenmayer.png
	-rmdir /SQ .gle