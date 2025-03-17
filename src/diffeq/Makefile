all: diffeq.eps diffeq.pdf diffeq.png

diffeq.eps: diffeq.gle
	gle /device EPS /cairo diffeq.gle

diffeq.pdf: diffeq.gle
	gle /device PDF /cairo diffeq.gle

diffeq.png: diffeq.gle
	gle /device PNG /cairo /DPI 150 diffeq.gle

clean:
	-del diffeq.eps diffeq.pdf diffeq.png
	-rmdir /SQ .gle