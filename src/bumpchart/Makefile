all: bumpchart.eps bumpchart.pdf bumpchart.png

bumpchart.eps: bumpchart.gle
	gle /device EPS /cairo bumpchart.gle

bumpchart.pdf: bumpchart.gle
	gle /device PDF /cairo bumpchart.gle

bumpchart.png: bumpchart.gle
	gle /device PNG /cairo /DPI 150 bumpchart.gle

clean:
	-del bumpchart.eps bumpchart.pdf bumpchart.png
	-rmdir /SQ .gle