all: armand.eps armand.pdf armand.png

armand.eps: armand.gle
	gle /device EPS /cairo armand.gle

armand.pdf: armand.gle
	gle /device PDF /cairo armand.gle

armand.png: armand.gle
	gle /device PNG /cairo /DPI 150 armand.gle

clean:
	-del armand.eps armand.pdf armand.png
	-rmdir /SQ .gle