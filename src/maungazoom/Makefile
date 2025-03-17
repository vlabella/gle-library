all: maungazoom.eps maungazoom.pdf maungazoom.png

maungazoom.eps: maungazoom.gle
	gle /device EPS /cairo maungazoom.gle

maungazoom.pdf: maungazoom.gle
	gle /device PDF /cairo maungazoom.gle

maungazoom.png: maungazoom.gle
	gle /device PNG /cairo /DPI 150 maungazoom.gle

clean:
	-del maungazoom.eps maungazoom.pdf maungazoom.png
	-rmdir /SQ .gle