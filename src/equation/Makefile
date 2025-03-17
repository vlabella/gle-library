all: equation.eps equation.pdf equation.png

equation.eps: equation.gle
	gle /device EPS /cairo equation.gle

equation.pdf: equation.gle
	gle /device PDF /cairo equation.gle

equation.png: equation.gle
	gle /device PNG /cairo /DPI 150 equation.gle

clean:
	-del equation.eps equation.pdf equation.png
	-rmdir /SQ .gle