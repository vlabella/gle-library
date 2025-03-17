all: regrmodel.eps regrmodel.pdf regrmodel.png

regrmodel.eps: regrmodel.gle
	gle /device EPS /cairo regrmodel.gle

regrmodel.pdf: regrmodel.gle
	gle /device PDF /cairo regrmodel.gle

regrmodel.png: regrmodel.gle
	gle /device PNG /cairo /DPI 150 regrmodel.gle

clean:
	-del regrmodel.eps regrmodel.pdf regrmodel.png
	-rmdir /SQ .gle