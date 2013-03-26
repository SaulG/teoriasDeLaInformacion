
set term postscript eps color 24
set output "ejemplo.eps"
set size 2, 5
unset key
set title "Simulacion de canal"
#set logscale x
#set logscale y
set xlabel "Frecuencia de cero" offset -1,-1 font "Helvetica Bold"
set ylabel "Probabilidad de cero" offset -1,-2 font "Helvetica Bold"
set zlabel "Probabilidad de uno" rotate by 90 left offset 2,-1.5 font "Helvetica Bold"
set multiplot
set cbrange [0:1]
set size 1,1
set xrange [-0.05:1.05]
set yrange [-0.05:1.05]
set zrange [-0.05:1.05]
set ytics 0.1, 0.2
set xtics 0.1, 0.2
set ztics 0.1, 0.2
#unset surf
#set style line 1 lt 4 lw .5
#set pm3d #at s hidden3d 1
set origin 0, 4
set label 1 "Largo 1" offset 0, 8 font "Helvetica Bold"
splot "largo1.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 1, 4
set label 1 "Largo 2" offset 0, 8 font "Helvetica Bold"
splot "largo2.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 0, 3
set label 1 "Largo 4" offset 0, 8 font "Helvetica Bold"
splot "largo4.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 1, 3
set label 1 "Largo 8" offset 0, 8 font "Helvetica Bold"
splot "largo8.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 0, 2
set label 1 "Largo 16" offset 0, 8 font "Helvetica Bold"
splot "largo16.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 1, 2
set label 1 "Largo 32" offset 0, 8 font "Helvetica Bold"
splot "largo32.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 0, 1
set label 1 "Largo 64" offset 0, 8 font "Helvetica Bold"
splot "largo64.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 1, 1
set label 1 "Largo 128" offset 0, 8 font "Helvetica Bold"
splot "largo128.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 0, 0
set label 1 "Largo 256" offset 0, 8 font "Helvetica Bold"
splot "largo256.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
set origin 1, 0
set label 1 "Largo 512" offset 0, 8 font "Helvetica Bold"
splot "largo512.dat" using 1:2:3:($5+1):6 with points pt 9 ps variable palette #lc variable
unset label 1
unset multiplot