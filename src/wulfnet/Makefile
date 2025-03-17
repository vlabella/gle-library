all: wulfnet.eps wulfnet.pdf wulfnet.png

wulfnet.eps: wulfnet.gle
	gle /device EPS /cairo wulfnet.gle

wulfnet.pdf: wulfnet.gle
	gle /device PDF /cairo wulfnet.gle

wulfnet.png: wulfnet.gle
	gle /device PNG /cairo /DPI 150 wulfnet.gle

clean:
	-del wulfnet.eps wulfnet.pdf wulfnet.png
	-rmdir /SQ .gle