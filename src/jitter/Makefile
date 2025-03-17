all: jitter.eps jitter.pdf jitter.png

jitter.eps: jitter.gle
	gle /device EPS /cairo jitter.gle

jitter.pdf: jitter.gle
	gle /device PDF /cairo jitter.gle

jitter.png: jitter.gle
	gle /device PNG /cairo /DPI 150 jitter.gle

clean:
	-del jitter.eps jitter.pdf jitter.png
	-rmdir /SQ .gle