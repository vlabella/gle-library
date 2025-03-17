all: curvedarrow.eps curvedarrow.pdf curvedarrow.png

curvedarrow.eps: curvedarrow.gle
	gle /device EPS /cairo curvedarrow.gle

curvedarrow.pdf: curvedarrow.gle
	gle /device PDF /cairo curvedarrow.gle

curvedarrow.png: curvedarrow.gle
	gle /device PNG /cairo /DPI 150 curvedarrow.gle

clean:
	-del curvedarrow.eps curvedarrow.pdf curvedarrow.png
	-rmdir /SQ .gle