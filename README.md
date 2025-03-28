# Description CFD_flowcell

This repository contains electronic supporting information for the paper **Establishing The Link Between Flow Uniformity and Overpotential in Electrocatalytic Flow Cell** submitted by L. Rotondi, A. Di Mascio and L. D'Amario. 


Relevant files are:

- *VUC_data.py* which is the python script used in the paraview python shell to gather datasets for VUC and store them in files *VUC_data_foam.csv*

- *calc_VUC.py* is the python script used to calculate VUC for every cells

- *VUC_total_results.csv* stores VUC results of every flow cells

- *medium_video.avi* shows the normal velocity simulation in the same sampling plane of the VUC, as represented in Figure 4 in the main paper

- *medium_video_sample.avi* resembles *medium_video.avi* showing also the part of the flow cell cross section not included in the VUC sampling to limit boundary layer effects. The VUC sampling radius is highlighted by a cylinder

A folder is present for each flow cell studied by Computational Fluid Dynamic. Each folder contains both input and output OpenFOAM files. 

### Input files

Input files are stored in the directories *system*, *constant* and *orig*. 

- *system* contains files specifying setting parameters related to the solution procedure, such as time step, start/end time, equation solvers, tolerances and discretisation schemes

- *constant* contains files specifying physical properties for the computed simulation, such as dynamic viscosity of the fluid and Darcy and Forchheimer coefficients of the porous media, and files descripting case mesh, stored in subfolders *polyMesh* and *triSurface*

- *orig* contains *p* and *U* files, specifying pressures and velocity fields. Inlet velocity is expressed in terms of inlet flow rate 


### Output files

Output files are stored in the time directories (0, 0.1, 0.2... etc.) and *logs*.

- time directories contain *p*, *U* and *phi* files, specifying pressure, velocity and flux field for every time step. Directories from *0.1* to *2* also contain *uniform* subfolder which specifies time step. This subfolder is absent in *0* since the fields stored here are related to the first approximated solution as potential flow, not characterized by any time steps

- *logs* contains several files specifying number of iterations, initial and final residual for every solved variable. This datas are extracted from the cellname.out file exploiting "foamLog". This cellname.out file stores the computed variables for every iteration of every time steps


Other relevant files are: 

- *pv.foam* used as dummy file to load results on Paraview 

- *VUC_data_foam_cellname.csv* contains dataset used to calculate VUC. *Quality* column stores areas of every grid cells while *U_0*, *U_1* and *U_2* are the related velocities along x, y and z axis respectively. It is generated by the *VUC_data.py* script

- *XY_Uz_cellname.csv* contains dataset used to 3D plot velocities for Fig S20, S21 and S22. *Points_0*, *Points_1* and *Points_2* columns store flow cell geometrical coordinates associated with related velocities stored in columns *U_0*, *U_1* and *U_2*. 0, 1 and 2 correspond to x, y and z axis respectively. This file is present only in *short*, *medium* and *long* folders




