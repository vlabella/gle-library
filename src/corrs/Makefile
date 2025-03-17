all: corrs.eps corrs.pdf corrs.png

corrs.eps: corrs.gle
	gle /device EPS /cairo corrs.gle

corrs.pdf: corrs.gle
	gle /device PDF /cairo corrs.gle

corrs.png: corrs.gle
	gle /device PNG /cairo /DPI 150 corrs.gle

clean:
	-del corrs.eps corrs.pdf corrs.png
	-rmdir /SQ .gle