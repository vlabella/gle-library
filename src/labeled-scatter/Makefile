all: labeled-scatter.eps labeled-scatter.pdf labeled-scatter.png

labeled-scatter.eps: labeled-scatter.gle
	gle /device EPS /cairo labeled-scatter.gle

labeled-scatter.pdf: labeled-scatter.gle
	gle /device PDF /cairo labeled-scatter.gle

labeled-scatter.png: labeled-scatter.gle
	gle /device PNG /cairo /DPI 150 labeled-scatter.gle

clean:
	-del labeled-scatter.eps labeled-scatter.pdf labeled-scatter.png
	-rmdir /SQ .gle