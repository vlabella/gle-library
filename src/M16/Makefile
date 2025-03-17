all: M16.eps M16.pdf M16.png

M16.eps: M16.gle
	gle /device EPS /cairo M16.gle

M16.pdf: M16.gle
	gle /device PDF /cairo M16.gle

M16.png: M16.gle
	gle /device PNG /cairo /DPI 150 M16.gle

clean:
	-del M16.eps M16.pdf M16.png
	-rmdir /SQ .gle