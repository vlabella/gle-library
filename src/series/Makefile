all: series.eps series.pdf series.png

series.eps: series.gle
	gle /device EPS /cairo series.gle

series.pdf: series.gle
	gle /device PDF /cairo series.gle

series.png: series.gle
	gle /device PNG /cairo /DPI 150 series.gle

clean:
	-del series.eps series.pdf series.png
	-rmdir /SQ .gle