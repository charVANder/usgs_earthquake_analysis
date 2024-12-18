.PHONY: data

data:
	mkdir -p data
	cd src; python get_main_data.py
	cd src; python merge_data.py
	cd src; python depth_mag.py

images:
	cd src; python merged_graph.py
	cd src; python depth_graph.py
	cd src; python depth_vs_mag_graph.py

gif:
	cd src; python depth_graph.py
	cd src; python make_gif.py

clean:
	rm -f data/
	rm -f figs/
