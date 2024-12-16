.PHONY: data

data:
	mkdir -p data
	cd src; python get_main_data.py
	cd src; python merge_multiple.py
	cd src; python depth_mag.py

image:

gif:

clean:
	rm -f data/
	rm -f figs/
