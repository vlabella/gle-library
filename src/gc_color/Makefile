all: gc_color.eps gc_color.pdf gc_color.png

gc_color.eps: gc_color.gle
	gle /device EPS /cairo gc_color.gle

gc_color.pdf: gc_color.gle
	gle /device PDF /cairo gc_color.gle

gc_color.png: gc_color.gle
	gle /device PNG /cairo /DPI 150 gc_color.gle

clean:
	-del gc_color.eps gc_color.pdf gc_color.png
	-rmdir /SQ .gle