import os

view_file = file('./render_pipeline/view_params.txt', 'w')
for i in range(0, 360, 15):
    for j in range(0, 60, 15):
        print >> view_file, i, j, 0, 1.1

view_file.close()
