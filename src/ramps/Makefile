all: ramps.eps ramps.pdf ramps.png

ramps.eps: ramps.gle
	gle /device EPS /cairo ramps.gle

ramps.pdf: ramps.gle
	gle /device PDF /cairo ramps.gle

ramps.png: ramps.gle
	gle /device PNG /cairo /DPI 150 ramps.gle

clean:
	-del ramps.eps ramps.pdf ramps.png
	-rmdir /SQ .gle