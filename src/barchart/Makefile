all: barchart.eps barchart.pdf barchart.png

barchart.eps: barchart.gle
	gle /device EPS /cairo barchart.gle

barchart.pdf: barchart.gle
	gle /device PDF /cairo barchart.gle

barchart.png: barchart.gle
	gle /device PNG /cairo /DPI 150 barchart.gle

clean:
	-del barchart.eps barchart.pdf barchart.png
	-rmdir /SQ .gle