all: markers.eps markers.pdf markers.png

markers.eps: markers.gle
	gle /device EPS /cairo markers.gle

markers.pdf: markers.gle
	gle /device PDF /cairo markers.gle

markers.png: markers.gle
	gle /device PNG /cairo /DPI 150 markers.gle

clean:
	-del markers.eps markers.pdf markers.png
	-rmdir /SQ .gle