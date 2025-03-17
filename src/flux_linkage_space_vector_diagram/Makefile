all: flux_linkage_space_vector_diagram.eps flux_linkage_space_vector_diagram.pdf flux_linkage_space_vector_diagram.png

flux_linkage_space_vector_diagram.eps: flux_linkage_space_vector_diagram.gle
	gle /device EPS /cairo flux_linkage_space_vector_diagram.gle

flux_linkage_space_vector_diagram.pdf: flux_linkage_space_vector_diagram.gle
	gle /device PDF /cairo flux_linkage_space_vector_diagram.gle

flux_linkage_space_vector_diagram.png: flux_linkage_space_vector_diagram.gle
	gle /device PNG /cairo /DPI 150 flux_linkage_space_vector_diagram.gle

clean:
	-del flux_linkage_space_vector_diagram.eps flux_linkage_space_vector_diagram.pdf flux_linkage_space_vector_diagram.png
	-rmdir /SQ .gle