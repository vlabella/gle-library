all: bayesiannet.eps bayesiannet.pdf bayesiannet.png

bayesiannet.eps: bayesiannet.gle
	gle /device EPS /cairo bayesiannet.gle

bayesiannet.pdf: bayesiannet.gle
	gle /device PDF /cairo bayesiannet.gle

bayesiannet.png: bayesiannet.gle
	gle /device PNG /cairo /DPI 150 bayesiannet.gle

clean:
	-del bayesiannet.eps bayesiannet.pdf bayesiannet.png
	-rmdir /SQ .gle