all: line.eps line.pdf line.png

line.eps: line.gle
	gle /device EPS /cairo line.gle

line.pdf: line.gle
	gle /device PDF /cairo line.gle

line.png: line.gle
	gle /device PNG /cairo /DPI 150 line.gle

clean:
	-del line.eps line.pdf line.png
	-rmdir /SQ .gle