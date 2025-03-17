all: rugplot.eps rugplot.pdf rugplot.png

rugplot.eps: rugplot.gle
	gle /device EPS /cairo rugplot.gle

rugplot.pdf: rugplot.gle
	gle /device PDF /cairo rugplot.gle

rugplot.png: rugplot.gle
	gle /device PNG /cairo /DPI 150 rugplot.gle

clean:
	-del rugplot.eps rugplot.pdf rugplot.png
	-rmdir /SQ .gle