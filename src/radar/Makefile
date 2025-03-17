all: radar.eps radar.pdf radar.png

radar.eps: radar.gle
	gle /device EPS /cairo radar.gle

radar.pdf: radar.gle
	gle /device PDF /cairo radar.gle

radar.png: radar.gle
	gle /device PNG /cairo /DPI 150 radar.gle

clean:
	-del radar.eps radar.pdf radar.png
	-rmdir /SQ .gle