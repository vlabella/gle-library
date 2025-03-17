all: linemode.eps linemode.pdf linemode.png

linemode.eps: linemode.gle
	gle /device EPS /cairo linemode.gle

linemode.pdf: linemode.gle
	gle /device PDF /cairo linemode.gle

linemode.png: linemode.gle
	gle /device PNG /cairo /DPI 150 linemode.gle

clean:
	-del linemode.eps linemode.pdf linemode.png
	-rmdir /SQ .gle