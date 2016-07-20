
;num = '050'
num = '005'
plot_fname = 'snapshot_'+num+'.eps'
fname = '/pfs/jeffjorges/runs/new_smooth/files/snapshot_'+num
test = read_snapshot_dm(fname,nparttotal,time,z,h,mass,pos,vel,id,types,pot=pot)



lg = 0.1
bg = 0.12
tg = 0.05
rg = 0.05
wx = 1.0 - lg - rg
wy = 1.0 - bg - tg

fsize = 5.0

cps = 1.2
set_plot,'ps'
device,filename=plot_fname,/encapsulate
device,xsize=5,ysize=5*wy/wx,/inches

plot,[0],[0],xrange=[0,100],yrange=[0,100],xtitle="x [mpc/h]",ytitle="y [mpc/h]",font=1,charsize=cps,xstyle=1,ystyle=1,xthick=3,ythick=3,position=[lg,bg,lg+wx,bg+wy],/normal
oplot,pos(0,*),pos(1,*),psym=3

device,/close
set_plot,'x'



end
