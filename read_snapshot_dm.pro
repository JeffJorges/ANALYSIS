function read_snapshot_dm,fsnapbase,nparttotal,time,z,h,mass,pos,vel,id,types,pot=pot

nlast =0L
nthis = 0L




time = 0.0D
redshift = 0.0D
BoxSize = 0.0D
HubbleParam = 0.0D
Omega0 = 0.0D
OmegaLambda = 0.0D
flag_sfr= 0L
flag_feedback= 0L
npartTotal =lonarr(6)
flag_cooling= 0L
flag_multiphase= 0L
flag_stellarage= 0L
flag_sfrhistogram= 0L
num_files= 0L
seed = 0L
npart = lonarr(6)
massarr = dblarr(6)
npartTotal = lonarr(6)
slack_array = lonarr(21)

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; open snapshot
;;;;;;;;;;;;;;;;;;;;;;;;;;;

fdata = fsnapbase

 if not keyword_set(silent) then print,'Snapshot: ',fdata
openr,1,fdata,/f77_unformatted,/swap_if_big_endian


;;;;;;;;;;;;;;;;;;;;;;;;;;;
; read header
;;;;;;;;;;;;;;;;;;;;;;;;;;;
readu,1,npart,massarr,time,redshift,flag_sfr,flag_feedback,npartTotal,flag_cooling,num_files,BoxSize,Omega0,OmegaLambda,HubbleParam,flag_multiphase,flag_stellarage,flag_sfrhistogram,slack_array
time  = float(time)
HubbleParam = float(HubbleParam)

for i=0,5 do if nparttotal(i) lt npart(i) then nparttotal(i) = npart(i)

 if not keyword_set(silent) then print,'npart',npart
 if not keyword_set(silent) then print,'nparttotal',npartTotal
 if not keyword_set(silent) then print,'massaray',massarr
 if not keyword_set(silent) then print,"a = ", time
 if not keyword_set(silent) then print,"z = ",redshift
;print,"flag_sfr = ",flag_sfr
;print,"flag_feedback= ",flag_feedback
;print,"npartTotal = ",npartTotal
;print,"flag_cooling= ",flag_cooling
;print,"numfiles = ",num_files
;print,'BoxSize= ',BoxSize
;print,'Omega_m = ',Omega0
;print,'Omega_L = ',OmegaLambda
;print,'h = ',HubbleParam
;print,"flag_multiphase= ",flag_multiphase
;print,"flag_stellarage= ",flag_stellarage
z = redshift
h = hubbleparam
;;;;;;;;;;;;;;;;;;;;;;;;;
; set numbers of particles
;;;;;;;;;;;;;;;;;;;;;;;;;

NGas  =nparttotal(0)
NHalo =nparttotal(1)
NDisk =nparttotal(2)
NBulge=nparttotal(3)
NStars=nparttotal(4)
NBH   =nparttotal(5)
N=nparttotal(0)+nparttotal(1)+nparttotal(2)+nparttotal(3)+nparttotal(4)+nparttotal(5)


;;;;;;;;;;;;;;;;;;;;;;;;;
; make data arrays
;;;;;;;;;;;;;;;;;;;;;;;;;


pos		=fltarr(3,N)				;positions
vel		=fltarr(3,N) 				;velocities
;id		=lonarr(N)				;particle ids
id		=lonarr(N)				;particle ids
if nparttotal(0) gt 0 then begin
u		=fltarr(nparttotal(0))			;gas internal energy
rho		=fltarr(nparttotal(0))			;gas density
hsml		=fltarr(nparttotal(0))			;gas smoothing length
endif
mass		= fltarr(N)				;masses
types 		= lonarr(N)				;types

;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; Read in data 
;
;;;;;;;;;;;;;;;;;;;;;;;;;;

n_without = 0
for i=0,5 do if massarr(i) eq 0.0 then n_without = n_without+npart(i)

if n_without gt 0 then masstmp = fltarr(n_without)

readu,1,pos
readu,1,vel
readu,1,id 
if n_without gt 0 then readu,1,masstmp
if nparttotal(0) gt 0 then  begin
readu,1,u
readu,1,rho
readu,1,hsml
endif
if keyword_set(pot) then begin
pot = fltarr(N)
readu,1,pot

endif
close,1


;;;;;;;;;;;;;;;;;;;;;;;;;;
; set particle masses
;;;;;;;;;;;;;;;;;;;;;;;;;;

for i=0,5 do begin
	if i eq 0 then begin
		n_previous = 0
		n_before   = 0
	endif else begin
		n_previous = total(npart(0:i-1))
	endelse
	if massarr(i) eq 0.0 then begin
		if npart(i) gt 0 then mass(n_previous:n_previous+npart(i)-1) = masstmp(n_before:n_before+npart(i)-1)
		n_before = n_before+npart(i)
	endif else begin
		mass(n_previous:n_previous+npart(i)-1) = massarr(i)
	endelse
endfor

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; set mass units to solar masses
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
mass(*) = mass(*)
  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; set particle types
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
if nparttotal(0) gt 0 then types(0:nparttotal(0)-1)=0
if nparttotal(1) gt 0 then types(nparttotal(0):nparttotal(0)+nparttotal(1)-1)=1
if nparttotal(2) gt 0 then types(nparttotal(0)+nparttotal(1):nparttotal(0)+nparttotal(1)+nparttotal(2)-1)=2
if nparttotal(3) gt 0 then types(nparttotal(0)+nparttotal(1)+nparttotal(2):nparttotal(0)+nparttotal(1)+nparttotal(2)+nparttotal(3)-1)=3
if nparttotal(4) gt 0 then types(nparttotal(0)+nparttotal(1)+nparttotal(2)+nparttotal(3):nparttotal(0)+nparttotal(1)+nparttotal(2)+nparttotal(3)+nparttotal(4)-1)=4
if nparttotal(5) gt 0 then types(nparttotal(0)+nparttotal(1)+nparttotal(2)+nparttotal(3)+nparttotal(4):nparttotal(0)+nparttotal(1)+nparttotal(2)+nparttotal(3)+nparttotal(4)+nparttotal(5)-1)=5


	return,0

end
