all: tgplot.eps tgplot.pdf tgplot.png

tgplot.eps: tgplot.gle
	gle /device EPS /cairo tgplot.gle

tgplot.pdf: tgplot.gle
	gle /device PDF /cairo tgplot.gle

tgplot.png: tgplot.gle
	gle /device PNG /cairo /DPI 150 tgplot.gle

clean:
	-del tgplot.eps tgplot.pdf tgplot.png
	-rmdir /SQ .gle