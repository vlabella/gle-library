all: protract.eps protract.pdf protract.png

protract.eps: protract.gle
	gle /device EPS /cairo protract.gle

protract.pdf: protract.gle
	gle /device PDF /cairo protract.gle

protract.png: protract.gle
	gle /device PNG /cairo /DPI 150 protract.gle

clean:
	-del protract.eps protract.pdf protract.png
	-rmdir /SQ .gle