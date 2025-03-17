all: drawpie.eps drawpie.pdf drawpie.png

drawpie.eps: drawpie.gle
	gle /device EPS /cairo drawpie.gle

drawpie.pdf: drawpie.gle
	gle /device PDF /cairo drawpie.gle

drawpie.png: drawpie.gle
	gle /device PNG /cairo /DPI 150 drawpie.gle

clean:
	-del drawpie.eps drawpie.pdf drawpie.png
	-rmdir /SQ .gle