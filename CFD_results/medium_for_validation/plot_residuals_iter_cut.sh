#!/bin/bash

gnuplot -persist > /dev/null 2>&1 << EOF
        set logscale y
        set title "Residual vs. Iterations"
        set xlabel "Iterations"
        set ylabel "Residual"
        plot "< cat *.out | grep 'Solving for Ux' | cut -d' ' -f9 | tr -d ',' | head -n 100" title 'Ux' with lines,\
               "< cat *.out | grep 'Solving for Uy' | cut -d' ' -f9 | tr -d ',' | head -n 100" title 'Uy' with lines,\
                 "< cat *.out | grep 'Solving for Uz' | cut -d' ' -f9 | tr -d ',' | head -n 100" title 'Uz' with lines,\
                   "< cat *.out | grep 'Solving for omega' | cut -d' ' -f9 | tr -d ',' | head -n 100" title 'omega' with lines,\
                     "< cat *.out | grep 'Solving for k' | cut -d' ' -f9 | tr -d ',' | head -n 100" title 'k' with lines,\
                       "< cat *.out | grep 'Solving for p' | cut -d' ' -f9 | tr -d ',' | head -n 100" title 'p' with lines,\

EOF
