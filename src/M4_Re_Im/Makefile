all: M4_Re_Im.eps M4_Re_Im.pdf M4_Re_Im.png

M4_Re_Im.eps: M4_Re_Im.gle
	gle /device EPS /cairo M4_Re_Im.gle

M4_Re_Im.pdf: M4_Re_Im.gle
	gle /device PDF /cairo M4_Re_Im.gle

M4_Re_Im.png: M4_Re_Im.gle
	gle /device PNG /cairo /DPI 150 M4_Re_Im.gle

clean:
	-del M4_Re_Im.eps M4_Re_Im.pdf M4_Re_Im.png
	-rmdir /SQ .gle