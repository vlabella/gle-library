all: arrowdesign.eps arrowdesign.pdf arrowdesign.png

arrowdesign.eps: arrowdesign.gle
	gle /device EPS /cairo arrowdesign.gle

arrowdesign.pdf: arrowdesign.gle
	gle /device PDF /cairo arrowdesign.gle

arrowdesign.png: arrowdesign.gle
	gle /device PNG /cairo /DPI 150 arrowdesign.gle

clean:
	-del arrowdesign.eps arrowdesign.pdf arrowdesign.png
	-rmdir /SQ .gle