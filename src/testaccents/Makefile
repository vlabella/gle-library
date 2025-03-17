all: testaccents.eps testaccents.pdf testaccents.png

testaccents.eps: testaccents.gle
	gle /device EPS /cairo testaccents.gle

testaccents.pdf: testaccents.gle
	gle /device PDF /cairo testaccents.gle

testaccents.png: testaccents.gle
	gle /device PNG /cairo /DPI 150 testaccents.gle

clean:
	-del testaccents.eps testaccents.pdf testaccents.png
	-rmdir /SQ .gle