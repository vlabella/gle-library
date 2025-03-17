all: logo.eps logo.pdf logo.png

logo.eps: logo.gle
	gle /device EPS /cairo logo.gle

logo.pdf: logo.gle
	gle /device PDF /cairo logo.gle

logo.png: logo.gle
	gle /device PNG /cairo /DPI 150 logo.gle

clean:
	-del logo.eps logo.pdf logo.png
	-rmdir /SQ .gle