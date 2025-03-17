all: legend.eps legend.pdf legend.png

legend.eps: legend.gle
	gle /device EPS /cairo legend.gle

legend.pdf: legend.gle
	gle /device PDF /cairo legend.gle

legend.png: legend.gle
	gle /device PNG /cairo /DPI 150 legend.gle

clean:
	-del legend.eps legend.pdf legend.png
	-rmdir /SQ .gle