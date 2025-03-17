all: data.eps data.pdf data.png

data.eps: data.gle
	gle /device EPS /cairo data.gle

data.pdf: data.gle
	gle /device PDF /cairo data.gle

data.png: data.gle
	gle /device PNG /cairo /DPI 150 data.gle

clean:
	-del data.eps data.pdf data.png
	-rmdir /SQ .gle