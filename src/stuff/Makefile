all: stuff.eps stuff.pdf stuff.png

stuff.eps: stuff.gle
	gle /device EPS /cairo stuff.gle

stuff.pdf: stuff.gle
	gle /device PDF /cairo stuff.gle

stuff.png: stuff.gle
	gle /device PNG /cairo /DPI 150 stuff.gle

clean:
	-del stuff.eps stuff.pdf stuff.png
	-rmdir /SQ .gle