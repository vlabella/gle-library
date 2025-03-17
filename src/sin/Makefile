all: sin.eps sin.pdf sin.png

sin.eps: sin.gle
	gle /device EPS /cairo sin.gle

sin.pdf: sin.gle
	gle /device PDF /cairo sin.gle

sin.png: sin.gle
	gle /device PNG /cairo /DPI 150 sin.gle

clean:
	-del sin.eps sin.pdf sin.png
	-rmdir /SQ .gle