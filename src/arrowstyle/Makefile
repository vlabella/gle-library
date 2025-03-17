all: arrowstyle.eps arrowstyle.pdf arrowstyle.png

arrowstyle.eps: arrowstyle.gle
	gle /device EPS /cairo arrowstyle.gle

arrowstyle.pdf: arrowstyle.gle
	gle /device PDF /cairo arrowstyle.gle

arrowstyle.png: arrowstyle.gle
	gle /device PNG /cairo /DPI 150 arrowstyle.gle

clean:
	-del arrowstyle.eps arrowstyle.pdf arrowstyle.png
	-rmdir /SQ .gle