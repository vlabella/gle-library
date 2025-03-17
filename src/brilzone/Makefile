all: brilzone.eps brilzone.pdf brilzone.png

brilzone.eps: brilzone.gle
	gle /device EPS /cairo brilzone.gle

brilzone.pdf: brilzone.gle
	gle /device PDF /cairo brilzone.gle

brilzone.png: brilzone.gle
	gle /device PNG /cairo /DPI 150 brilzone.gle

clean:
	-del brilzone.eps brilzone.pdf brilzone.png
	-rmdir /SQ .gle