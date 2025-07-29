#!/bin/bash

#module load bioinfo-tools

#module load OpenFOAM/v1612+

#foamLog *.out >/dev/null

module load gnuplot/5.4.rc1

gnuplot -persist > /dev/null 2>&1 << EOF
        set logscale y
        set title "Residual vs. Time nomod"
        set xlabel "Time (s)"
        set ylabel "Residual"
        plot "logs/Ux_0" with lines,\
                "logs/Uy_0" with lines,\
                   "logs/Uz_0" with lines,\
                      #"logs/p_0" with lines

EOF
