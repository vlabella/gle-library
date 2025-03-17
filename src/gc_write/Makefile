all: gc_write.eps gc_write.pdf gc_write.png

gc_write.eps: gc_write.gle
	gle /device EPS /cairo gc_write.gle

gc_write.pdf: gc_write.gle
	gle /device PDF /cairo gc_write.gle

gc_write.png: gc_write.gle
	gle /device PNG /cairo /DPI 150 gc_write.gle

clean:
	-del gc_write.eps gc_write.pdf gc_write.png
	-rmdir /SQ .gle