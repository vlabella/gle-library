all: cavity.eps cavity.pdf cavity.png

cavity.eps: cavity.gle
	gle /device EPS /cairo cavity.gle

cavity.pdf: cavity.gle
	gle /device PDF /cairo cavity.gle

cavity.png: cavity.gle
	gle /device PNG /cairo /DPI 150 cavity.gle

clean:
	-del cavity.eps cavity.pdf cavity.png
	-rmdir /SQ .gle