all: spider.eps spider.pdf spider.png

spider.eps: spider.gle
	gle /device EPS /cairo spider.gle

spider.pdf: spider.gle
	gle /device PDF /cairo spider.gle

spider.png: spider.gle
	gle /device PNG /cairo /DPI 150 spider.gle

clean:
	-del spider.eps spider.pdf spider.png
	-rmdir /SQ .gle