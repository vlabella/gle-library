all: dvifill.eps dvifill.pdf dvifill.png

dvifill.eps: dvifill.gle
	gle /device EPS /cairo dvifill.gle

dvifill.pdf: dvifill.gle
	gle /device PDF /cairo dvifill.gle

dvifill.png: dvifill.gle
	gle /device PNG /cairo /DPI 150 dvifill.gle

clean:
	-del dvifill.eps dvifill.pdf dvifill.png
	-rmdir /SQ .gle