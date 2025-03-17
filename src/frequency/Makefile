all: frequency.eps frequency.pdf frequency.png

frequency.eps: frequency.gle
	gle /device EPS /cairo frequency.gle

frequency.pdf: frequency.gle
	gle /device PDF /cairo frequency.gle

frequency.png: frequency.gle
	gle /device PNG /cairo /DPI 150 frequency.gle

clean:
	-del frequency.eps frequency.pdf frequency.png
	-rmdir /SQ .gle