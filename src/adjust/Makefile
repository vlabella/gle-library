all: adjust.eps adjust.pdf adjust.png

adjust.eps: adjust.gle
	gle /device EPS /cairo adjust.gle

adjust.pdf: adjust.gle
	gle /device PDF /cairo adjust.gle

adjust.png: adjust.gle
	gle /device PNG /cairo /DPI 150 adjust.gle

clean:
	-del adjust.eps adjust.pdf adjust.png
	-rmdir /SQ .gle