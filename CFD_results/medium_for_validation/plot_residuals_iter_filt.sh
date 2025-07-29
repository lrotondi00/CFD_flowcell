#!/bin/bash

gnuplot -persist > /dev/null 2>&1 << EOF
        set logscale y
        set title "Residual vs. Iterations trans_pimple1"
        set xlabel "Iterations"
        set ylabel "Residual"
        plot "< cat *.out | grep 'Solving for Ux' | cut -d' ' -f9 | sed -n '9000,9200p' | tr -d ',' | awk '{print NR+8999, \$1}'" title 'Ux' with lines,\
               "< cat *.out | grep 'Solving for Uy' | cut -d' ' -f9 | sed -n '9000,9200p' | tr -d ',' | awk '{print NR+8999, \$1}'" title 'Uy' with lines,\
                 "< cat *.out | grep 'Solving for Uz' | cut -d' ' -f9 | sed -n '9000,9200p' | tr -d ',' | awk '{print NR+8999, \$1}'" title 'Uz' with lines,\
                   "< cat *.out | grep 'Solving for p' | cut -d' ' -f9 | sed '1,9p' | sed -n '9000,9200p' | tr -d ',' | awk '{print NR+8999, \$1}'" title 'p' with lines


EOF
