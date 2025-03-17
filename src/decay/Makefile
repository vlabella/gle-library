all: decay.eps decay.pdf decay.png

decay.eps: decay.gle
	gle /device EPS /cairo decay.gle

decay.pdf: decay.gle
	gle /device PDF /cairo decay.gle

decay.png: decay.gle
	gle /device PNG /cairo /DPI 150 decay.gle

clean:
	-del decay.eps decay.pdf decay.png
	-rmdir /SQ .gle