from save_graph import save_graph
for i in range(1, 13):
    save_graph(f"data{i}.geojson", f"graph{i}", "Grouped by Month")