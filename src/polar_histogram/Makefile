all: polar_histogram.eps polar_histogram.pdf polar_histogram.png

polar_histogram.eps: polar_histogram.gle
	gle /device EPS /cairo polar_histogram.gle

polar_histogram.pdf: polar_histogram.gle
	gle /device PDF /cairo polar_histogram.gle

polar_histogram.png: polar_histogram.gle
	gle /device PNG /cairo /DPI 150 polar_histogram.gle

clean:
	-del polar_histogram.eps polar_histogram.pdf polar_histogram.png
	-rmdir /SQ .gle