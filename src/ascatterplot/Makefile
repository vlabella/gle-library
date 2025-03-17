all: ascatterplot.eps ascatterplot.pdf ascatterplot.png

ascatterplot.eps: ascatterplot.gle
	gle /device EPS /cairo ascatterplot.gle

ascatterplot.pdf: ascatterplot.gle
	gle /device PDF /cairo ascatterplot.gle

ascatterplot.png: ascatterplot.gle
	gle /device PNG /cairo /DPI 150 ascatterplot.gle

clean:
	-del ascatterplot.eps ascatterplot.pdf ascatterplot.png
	-rmdir /SQ .gle