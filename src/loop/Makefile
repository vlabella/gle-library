all: loop.eps loop.pdf loop.png

loop.eps: loop.gle
	gle /device EPS /cairo loop.gle

loop.pdf: loop.gle
	gle /device PDF /cairo loop.gle

loop.png: loop.gle
	gle /device PNG /cairo /DPI 150 loop.gle

clean:
	-del loop.eps loop.pdf loop.png
	-rmdir /SQ .gle