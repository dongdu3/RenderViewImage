This project is used for rendering images from different views (default is 128*128*3 RGB image, 96 views). If you want to change some params, you should change the code like:

1. change the path of 3d model dataset;

2. change the g_syn_images_num_per_model and run "setup.py";

3. use the 'gene_view_params.py' file to change the view_params: (azimuth_deg, elevation_deg, theta_deg, rho_deg), generate a 'view_params.txt' file in the dir 'render_pipeline';

4. just run the file 'run_render.py' the the dir 'render_pipeline' to get the synthesis images.
