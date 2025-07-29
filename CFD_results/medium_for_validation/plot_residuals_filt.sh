#!/bin/bash

sed -n '/^0.001/,/^0.3/p' logs/Ux_0 > filtered_Ux_0
sed -n '/^0.001/,/^0.3/p' logs/Uy_0 > filtered_Uy_0
sed -n '/^0.001/,/^0.3/p' logs/Uz_0 > filtered_Uz_0
sed -n '/^0.001/,/^0.3/p' logs/p_0 > filtered_p_0


gnuplot -persist > /dev/null 2>&1 << EOF
        set logscale y
        set title "Residual vs. Time"
        set xlabel "Time (s)"
        set ylabel "Residual"
        plot "filtered_Ux_0" with lines,\
               "filtered_Uy_0" with lines,\
                 "filtered_Uz_0" with lines,\
                   "filtered_p_0" with lines

EOF

rm filtered_Ux_0 filtered_Uy_0 filtered_Uz_0 filtered_p_0
