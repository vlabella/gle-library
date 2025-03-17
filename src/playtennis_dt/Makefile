all: playtennis_dt.eps playtennis_dt.pdf playtennis_dt.png

playtennis_dt.eps: playtennis_dt.gle
	gle /device EPS /cairo playtennis_dt.gle

playtennis_dt.pdf: playtennis_dt.gle
	gle /device PDF /cairo playtennis_dt.gle

playtennis_dt.png: playtennis_dt.gle
	gle /device PNG /cairo /DPI 150 playtennis_dt.gle

clean:
	-del playtennis_dt.eps playtennis_dt.pdf playtennis_dt.png
	-rmdir /SQ .gle