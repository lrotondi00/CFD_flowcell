#!/bin/bash

gnuplot -persist > /dev/null 2>&1 << EOF
        set logscale y
        set title "Residual vs. Iterations trans"
        set xlabel "Iterations"
        set ylabel "Residual"
        plot "< cat *.out | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ','" title 'Ux' with lines,\
               "< cat *.out | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ','" title 'Uy' with lines,\
                 "< cat *.out | grep 'Solving for Uz' | cut -d' ' -f9 | tr -d ','" title 'Uz' with lines,\
                       "< cat *.out | grep 'Solving for p' | cut -d' ' -f9 | sed '1,9p' | sed -n 'p;N;N;N;N;N;N;N;N' | tr -d ','" title 'p' with lines,\

EOF
