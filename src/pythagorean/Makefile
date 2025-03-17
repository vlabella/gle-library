all: pythagorean.eps pythagorean.pdf pythagorean.png

pythagorean.eps: pythagorean.gle
	gle /device EPS /cairo pythagorean.gle

pythagorean.pdf: pythagorean.gle
	gle /device PDF /cairo pythagorean.gle

pythagorean.png: pythagorean.gle
	gle /device PNG /cairo /DPI 150 pythagorean.gle

clean:
	-del pythagorean.eps pythagorean.pdf pythagorean.png
	-rmdir /SQ .gle