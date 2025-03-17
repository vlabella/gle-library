all: dragon.eps dragon.pdf dragon.png

dragon.eps: dragon.gle
	gle /device EPS /cairo dragon.gle

dragon.pdf: dragon.gle
	gle /device PDF /cairo dragon.gle

dragon.png: dragon.gle
	gle /device PNG /cairo /DPI 150 dragon.gle

clean:
	-del dragon.eps dragon.pdf dragon.png
	-rmdir /SQ .gle