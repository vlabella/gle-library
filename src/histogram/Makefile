all: histogram.eps histogram.pdf histogram.png

histogram.eps: histogram.gle
	gle /device EPS /cairo histogram.gle

histogram.pdf: histogram.gle
	gle /device PDF /cairo histogram.gle

histogram.png: histogram.gle
	gle /device PNG /cairo /DPI 150 histogram.gle

clean:
	-del histogram.eps histogram.pdf histogram.png
	-rmdir /SQ .gle