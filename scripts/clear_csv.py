import os

files_to_remove = ['nodes.csv', 'nodes_tags.csv', 'ways_nodes.csv', 'ways_tags.csv', 'ways.csv']

for f in files_to_remove:
    os.remove(f)
