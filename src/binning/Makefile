all: binning.eps binning.pdf binning.png

binning.eps: binning.gle
	gle /device EPS /cairo binning.gle

binning.pdf: binning.gle
	gle /device PDF /cairo binning.gle

binning.png: binning.gle
	gle /device PNG /cairo /DPI 150 binning.gle

clean:
	-del binning.eps binning.pdf binning.png
	-rmdir /SQ .gle