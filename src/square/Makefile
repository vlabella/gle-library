all: square.eps square.pdf square.png

square.eps: square.gle
	gle /device EPS /cairo square.gle

square.pdf: square.gle
	gle /device PDF /cairo square.gle

square.png: square.gle
	gle /device PNG /cairo /DPI 150 square.gle

clean:
	-del square.eps square.pdf square.png
	-rmdir /SQ .gle