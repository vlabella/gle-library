all: web.eps web.pdf web.png

web.eps: web.gle
	gle /device EPS /cairo web.gle

web.pdf: web.gle
	gle /device PDF /cairo web.gle

web.png: web.gle
	gle /device PNG /cairo /DPI 150 web.gle

clean:
	-del web.eps web.pdf web.png
	-rmdir /SQ .gle