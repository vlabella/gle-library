all: sine-approx.eps sine-approx.pdf sine-approx.png

sine-approx.eps: sine-approx.gle
	gle /device EPS /cairo sine-approx.gle

sine-approx.pdf: sine-approx.gle
	gle /device PDF /cairo sine-approx.gle

sine-approx.png: sine-approx.gle
	gle /device PNG /cairo /DPI 150 sine-approx.gle

clean:
	-del sine-approx.eps sine-approx.pdf sine-approx.png
	-rmdir /SQ .gle