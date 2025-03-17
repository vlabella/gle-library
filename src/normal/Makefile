all: normal.eps normal.pdf normal.png

normal.eps: normal.gle
	gle /device EPS /cairo normal.gle

normal.pdf: normal.gle
	gle /device PDF /cairo normal.gle

normal.png: normal.gle
	gle /device PNG /cairo /DPI 150 normal.gle

clean:
	-del normal.eps normal.pdf normal.png
	-rmdir /SQ .gle