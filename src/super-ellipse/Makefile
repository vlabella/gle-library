all: super-ellipse.eps super-ellipse.pdf super-ellipse.png

super-ellipse.eps: super-ellipse.gle
	gle /device EPS /cairo super-ellipse.gle

super-ellipse.pdf: super-ellipse.gle
	gle /device PDF /cairo super-ellipse.gle

super-ellipse.png: super-ellipse.gle
	gle /device PNG /cairo /DPI 150 super-ellipse.gle

clean:
	-del super-ellipse.eps super-ellipse.pdf super-ellipse.png
	-rmdir /SQ .gle