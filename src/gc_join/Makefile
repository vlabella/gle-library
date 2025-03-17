all: gc_join.eps gc_join.pdf gc_join.png

gc_join.eps: gc_join.gle
	gle /device EPS /cairo gc_join.gle

gc_join.pdf: gc_join.gle
	gle /device PDF /cairo gc_join.gle

gc_join.png: gc_join.gle
	gle /device PNG /cairo /DPI 150 gc_join.gle

clean:
	-del gc_join.eps gc_join.pdf gc_join.png
	-rmdir /SQ .gle