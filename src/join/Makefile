all: join.eps join.pdf join.png

join.eps: join.gle
	gle /device EPS /cairo join.gle

join.pdf: join.gle
	gle /device PDF /cairo join.gle

join.png: join.gle
	gle /device PNG /cairo /DPI 150 join.gle

clean:
	-del join.eps join.pdf join.png
	-rmdir /SQ .gle