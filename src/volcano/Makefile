all: volcano.eps volcano.pdf volcano.png

volcano.eps: volcano.gle
	gle /device EPS /cairo volcano.gle

volcano.pdf: volcano.gle
	gle /device PDF /cairo volcano.gle

volcano.png: volcano.gle
	gle /device PNG /cairo /DPI 150 volcano.gle

clean:
	-del volcano.eps volcano.pdf volcano.png
	-rmdir /SQ .gle