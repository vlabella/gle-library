all: barcode_example.eps barcode_example.pdf barcode_example.png

barcode_example.eps: barcode_example.gle
	gle /device EPS /cairo barcode_example.gle

barcode_example.pdf: barcode_example.gle
	gle /device PDF /cairo barcode_example.gle

barcode_example.png: barcode_example.gle
	gle /device PNG /cairo /DPI 150 barcode_example.gle

clean:
	-del barcode_example.eps barcode_example.pdf barcode_example.png
	-rmdir /SQ .gle