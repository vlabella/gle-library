all: AFM.eps AFM.pdf AFM.png

AFM.eps: AFM.gle
	gle /device EPS /cairo AFM.gle

AFM.pdf: AFM.gle
	gle /device PDF /cairo AFM.gle

AFM.png: AFM.gle
	gle /device PNG /cairo /DPI 150 AFM.gle

clean:
	-del AFM.eps AFM.pdf AFM.png
	-rmdir /SQ .gle