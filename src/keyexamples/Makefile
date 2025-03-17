all: keyexamples.eps keyexamples.pdf keyexamples.png

keyexamples.eps: keyexamples.gle
	gle /device EPS /cairo keyexamples.gle

keyexamples.pdf: keyexamples.gle
	gle /device PDF /cairo keyexamples.gle

keyexamples.png: keyexamples.gle
	gle /device PNG /cairo /DPI 150 keyexamples.gle

clean:
	-del keyexamples.eps keyexamples.pdf keyexamples.png
	-rmdir /SQ .gle