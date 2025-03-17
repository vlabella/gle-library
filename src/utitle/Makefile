all: utitle.eps utitle.pdf utitle.png

utitle.eps: utitle.gle
	gle /device EPS /cairo utitle.gle

utitle.pdf: utitle.gle
	gle /device PDF /cairo utitle.gle

utitle.png: utitle.gle
	gle /device PNG /cairo /DPI 150 utitle.gle

clean:
	-del utitle.eps utitle.pdf utitle.png
	-rmdir /SQ .gle