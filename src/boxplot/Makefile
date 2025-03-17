all: boxplot.eps boxplot.pdf boxplot.png

boxplot.eps: boxplot.gle
	gle /device EPS /cairo boxplot.gle

boxplot.pdf: boxplot.gle
	gle /device PDF /cairo boxplot.gle

boxplot.png: boxplot.gle
	gle /device PNG /cairo /DPI 150 boxplot.gle

clean:
	-del boxplot.eps boxplot.pdf boxplot.png
	-rmdir /SQ .gle