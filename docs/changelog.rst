MOOG_SCAT v1.0.0 CHANGELOG
==========================

Purpose:

- update all LTE subroutines so that they are consistent with the current 2019 release

- general update/vet of MOOG-SCAT code in order to issue new release

General log of changes:

- Compared MOOG_LTE v.2019 to MOOG_SCAT v.2017-2020 (unreleased)

- Adopted and integrated all non-SCAT MOOG-LTE subroutines

- Modified, as needed, SCAT-associated routines to be consistent with their LTE counterparts

- Uncovered a few errors in MOOG-LTE v.2019 (release Nov 2019) and altered them in current SCAT code version

List of LTE Coverted Routines
-----------------------------

(All MOOG Drivers; ! indicates unxpected version differences)

Abfind --> Abfind_SCAT

Abpop --> Abpop_SCAT (!; resolved)

Binary --> Binary_SCAT

Blends --> Blends_SCAT (!; resolved)

Cdcalc --> Cdcalc_SCAT

Cog --> Cog_SCAT

Cogsyn --> Cogsyn_SCAT

Curve --> Curve_SCAT

Doflux --> Doflux_SCAT

Ewfind --> Ewfind_SCAT (!)

Fakeline --> Fakeline_SCAT

Getsyns --> Getsyns_SCAT

Gridsyn --> Gridsyn_SCAT

Lineabund --> Lineabund_SCAT

Various Makefiles (!)

Moog --> Moog_SCAT (!; resolved)

Moogsilent -->Moogsilent_SCAT (!; resolved)

Oneline --> Oneline_SCAT (!; resolved??---> check equations/theory)

Synpop --> Synpop_SCAT (!; resolved)

Synspec --> Synspec_SCAT(!; resolved)

Synth --> Synth_SCAT

SCAT-Only Routines/Files
------------------------

Scat.com

Ang_Weight_SCAT.f

Gauss_Quad_Sum.f

Sourcefunc_cont_SCAT.f

Sourcefunc_line_SCAT.f

LTE Code Changes
----------------

- Removal of the ESTIM routine (as compared to earlier LTE [2017, 2014] versions)

- Removal of the Minimax routine (as compared to earlier LTE [2017, 2014] versions)

- Addition of SETMOLS routine (as compared to earlier LTE [2017, 2014] versions)

- In Moog_silent.f, there is still redundancy if a user calls the deprecated 'isotop' driver while in Moog.f no such redundancy exists. Consistency issue!

JS Suggested MOOG_LTE Modifications
-----------------------------------

- Removal of PLOTVALS common block (still mentioned in Correl.f; but as Correl.f subroutine does not employ any of the VAR, should be fine)

- Modification of Correl.f to remove PLOTVALS common block

- Removal of common block file from distribution

JS To Do
--------

- Modified LTE routines list

- New/additional SCAT routines

- How to call MOOG_SCAT, e.g., ./MOOG_SCAT

- General Documentation

LTE - SCAT Common Subroutines: Difference (dff) Comparisons
-----------------------------------------------------------
>>> Abfind
2c2
<       subroutine abfind
---
>       subroutine abfind_scat
60c60
< 100   call fakeline
---
> 100   call fakeline_scat
92c92
<             call lineabund (abundin)
---
>             call lineabund_scat (abundin)
105c105
<             call lineabund (abundin)
---
>             call lineabund_scat (abundin)

>>> Abpop [!ONE CHANGE; RESOLVED]
2c2
<       subroutine abpop
---
>       subroutine abpop_scat
101c101
<             call curve
---
>             call curve_scat
223d222
<       if (silent .eq. 'n') then 
227,229d225
<       else
<          choice = 'y'
<       endif

>>>Binary
c2
<       subroutine binary
---
>       subroutine binary_scat
111c111
<          call synspec
---
>          call synspec_scat
122c122
<             call synspec
---
>             call synspec_scat

>>> Blends [!UNEXPECTED CHANGES]
2c2
<       subroutine blends 
---
>       subroutine blends_scat
14a15
>       include 'Scat.com'
122c123
<             call synspec
---
>             call synspec_scat
180c181
<          call synspec
---
>          call synspec_scat
194,196c195,200
<             call cdcalc(2)
<             first = 0.4343*cd(1)
<             d(1) = rinteg(xref,cd,dummy1,ntau,first)
---
> c            call cdcalc (2)
>             call cdcalc_scat(2)
> c            first = 0.4343*cd(1)
>             first = 0.4343*adepth
> c            d(1) = rinteg(xref,cd,dummy1,ntau,first)
>             d(1) = adepth
198c202,203
<                dummy1(i) = xref(i)*cd(i)
---
> c               dummy1(i) = xref(i)*cd(i)
>                dummy1(i) = xref(i)*adepth
200a206,207
> c            cdmean = rinteg(xref,dummy1,dummy2,ntau,first)/
> c     .      rinteg(xref,cd,dummy2,ntau,first)
202c209
<      .      rinteg(xref,cd,dummy2,ntau,first)
---
>      .      rinteg(xref,adepth,dummy2,ntau,first)
204c211,212
<                if (cdmean .lt. cd(i)) exit
---
> c               if (cdmean .lt. cd(i)) exit
>                if (cdmean .lt. adepth) exit


>>> Cdcalc 

>>> Cog
2c2
<       subroutine cog
---
>       subroutine cog_scat
73c73
<          call curve
---
>          call curve_scat

>>> Cogsyn
<       subroutine cogsyn
---
>       subroutine cogsyn_scat
68c68
<       call synspec
---
>       call synspec_scat
83c83
<       call synspec
---
>       call synspec_scat


>>> Curve
2c2
<       subroutine curve
---
>       subroutine curve_scat
24c24
< 31    call oneline (2)
---
> 31    call oneline_scat (2)
41c41
< 61    call oneline (2)
---
> 61    call oneline_scat (2)


>>> Doflux
2c2
<       subroutine doflux
---
>       subroutine doflux_scat
11a12
>       include 'Scat.com'
53,55c54,58
<       call cdcalc (1)
<       first = 0.4343*cd(1)
<       flux = rinteg(xref,cd,dummy1,ntau,first)
---
> c      call cdcalc (1)
>       call cdcalc_scat (1)
> c      first = 0.4343*cd(1)
> c      flux = rinteg(xref,cd,dummy1,ntau,first)
>       flux = Flux_cont_MOOG

>>> EWfind [?UNEXPECTED CHANGES]
,2c1
< 
<       subroutine ewfind
---
>       subroutine ewfind_scat
12a12
>       include 'Scat.com'
16a17
> 
19a21
> 
51a54
>       isynth = 1
69,70c72,73
<          array(1:40) = 'wavelength        EP     logGF     ident'
<          array(41:60) = '     Abund    EWcalc'
---
>          call molquery
>          write (array,1001)
77c80
<          call oneline (1)
---
>          call oneline_scat (1)
79a83,85
> 
> 
>          if (iatom .lt. 100) then
80a87,89
>          else
>             xab = dlog10(xabund(iabtom)) + 12.
>          endif
93,94c102,103
<      .                         dlog10(gf(lim1)), atom1(lim1), 
<      .                         xab, 1000.*widout(lim1)
---
>      .                         dlog10(gf(lim1)), names(iaa), 
>      .                         names(ibb), xab, 1000.*widout(lim1)
98,99c107,108
<      .                          dlog10(gf(lim1)), atom1(lim1), 
<      .                          xab, 1000.*widout(lim1)
---
>      .                          dlog10(gf(lim1)), names(iaa), 
>      .                          names(ibb), xab, 1000.*widout(lim1)
103a113
> 
111,114d120
<          do i=1,ntau
<             taunu(i) = taunu0(i)
<          enddo
<          call cdcalc (2)
117a124,129
>          do i=1,ntau
>             taunu(i) = taunu0(i)
>          enddo
> c         call cdcalc (2)
>          call cdcalc_SCAT (2)
>          if (linprintopt .ge. 2) then
120,121c132,134
<      .                        pgas(i), rho(i), xdepth(i), taulam(i), 
<      .                        taunu0(i), cd(i), i=1,ntau)
---
>      .                          pgas(i), rho(i), kaplam(i), 
>      .                          taulam(i), taunu0(i), adepth, i=1,ntau)
>          endif
127,129c140
<                xdepthlam1 = xdepth(i-1) + (1.-taulam(i-1))*
<      .                (xdepth(i)-xdepth(i-1))/(taulam(i)-taulam(i-1))
<                write (nf2out,1013) int(xdepthlam1), i
---
>                write (nf2out,1013) tauref(i), i
142,144c153
<                xdepthnu01 = xdepth(i-1) + (1.-taunu0(i-1))*
<      .                (xdepth(i)-xdepth(i-1))/(taunu0(i)-taunu0(i-1))
<                write (nf2out,1014) int(xdepthnu01), i
---
>                write (nf2out,1014) tauref(i), i
153,157c162
<                tautot1 = taulam(i-1) + taunu0(i-1)
<                tautot2 = taulam(i) + taunu0(i)
<                xdepthtot1 = xdepth(i-1) + (1.-tautot1)*
<      .                (xdepth(i)-xdepth(i-1))/(tautot2-tautot1)
<                write (nf2out,1015) int(xdepthtot1), i
---
>                write (nf2out,1015) tauref(i), i
163a169,170
> c    SCATTERING TO DO: create a two-dimensional array that stores adepth as a function of line
> c    frequency; then consider the code below
165c172,173
<             dummy1(i) = xref(i)*dabs(cd(i))
---
> c            dummy1(i) = xref(i)*dabs(cd(i))
>             dummy1(i) = xref(i)*dabs(adepth)
169c177,178
<             dummy1(i) = dabs(cd(i))
---
> c            dummy1(i) = dabs(cd(i))
>             dummy1(i) = dabs(adepth)                                     | RE-CONSIDER
175,178c184
<                xdepthxrefmean = xdepth(i-1) + (xrefmean-xref(i-1))* 
<      .                (xdepth(i)-xdepth(i-1))/(xref(i)-xref(i-1))
<                write (nf2out,1017) int(xdepthxrefmean), i, tauref(i),
<      .                             taulam(i)
---
>                write (nf2out,1017) 10**(xrefmean), i
195,211c201,216
< 1003  format (f10.2,f10.2,f10.3,'     ',a2,a3,f10.2,f10.1)
< 1004  format (f10.2,f10.2,f10.3,a10,f10.2,f10.1)
< 1010     format ('  i', 2x, 'rhox', 5x, 'xref', 5x, 'T', 5x, 'Pgas', 
<      .           6x, 'rho', 8x, 'X', 3x, 'taulam', 3x, 'taunu0',
<      .           8x, 'Cd')
< 1011  format (i3, 1pe9.2, 0pf6.2, i6, 1p5e9.2, e10.2)
< 1013           format (i7, 'km (layer ~', i3, ') = physical depth',
<      .                 ' for tau(cont) ~ 1')
< 1014           format (i7, 'km (layer ~', i3, ') = physical depth',
<      .                 ' for tau(line center) ~ 1')
< 1015           format (i7, 'km (layer ~', i3, ') = physical depth',
<      .                 ' for tau(cont)+tau(line center) ~ 1')
< 1016           format (7x,'  NOTE: tau(line center) < 1 at deepest',
<      .                 ' atmosphere layer')
< 1017           format (i7, 'km (layer ~', i3, ') = line center ',
<      .                 'formation mean depth; C_d weight'/
<      .                 25x, 'where tauref, taulam =', 2f8.3)
---
> 1003  format (f10.2,f10.2,f10.3,'     ',a2,a3,f10.2,f10.1/)
> 1004  format (f10.2, f10.2, f10.3, 6x, a2, a2, f10.2, f10.1/)
> 1010     format (' i', 5x, 'rhox', 2x, 'xref', 5x, 'T', 5x, 'Pgas', 
>      .           6x, 'rho', 3x, 'kaplam', 3x, 'taulam',
>      .           3x, 'taunu0', 8x, 'Cd')
> 1011  format (i2, 1pd9.2, 0pf6.2, i6, 1p5d9.2, d10.2)
> 1013           format (5x, 'tau(ref) =', 1pe10.2,
>      .                 ' (level=',i2, ') for tau(cont) ~ 1')
> 1014           format (5x, 'tau(ref) =', 1pe10.2,
>      .                 ' (level=',i2, ') for tau(line) ~ 1')
> 1015           format (5x, 'tau(ref) =', 1pe10.2,
>      .                 ' (level=',i2, ') for tau(cont+line) ~ 1')
> 1016           format (7x,'  NOTE: line center tau(line) < 1',
>      .                 '  at deepest atmosphere layer')
> 1017           format (5x, 'C_d weighted mean formation tau(ref) =',
>      .                 1pe10.2, ' (level=',i2, ')')

>>> Fakeline
2c2
<       subroutine fakeline
---
>       subroutine fakeline_scat
64c64
<       call curve
---
>       call curve_scat

>>> Getsyns
2c2
<       subroutine getsyns (lscreen,ncall)
---
>       subroutine getsyns_scat (lscreen,ncall)
73c73
<          call synspec
---
>          call synspec_scat
85c85
<             call synspec
---
>             call synspec_scat

>>> Gridsyn
2c2
<       subroutine gridsyn
---
>       subroutine gridsyn_scat
103c103
<          call synspec
---
>          call synspec_scat
115c115
<             call synspec
---
>             call synspec_scat

>>> Lineabund
2c2
<       subroutine lineabund (abundin)
---
>       subroutine lineabund_scat (abundin)
36c36
< 15    call oneline (1)
---
> 15    call oneline_scat (1)
82c82
<       call oneline (2)
---
>       call oneline_scat (2)

>>> Moog [!UNEXPECTED CHANGES]
2c2
<       program moog
---
>       program moog_scat
22c22
<      .  '/Users/jsobeck/moog2019_LTE'
---
>      .  '/Users/jsobeck/moog_SCAT-update'
53a54,55
> c*****Call the Ang_Weight_SCAT routine
>         call ang_weight_SCAT
55c57
< c*****use one of the standard driver routines
---
> c*****use one of the standard driver routines ("isotop" is obsolete):
59c61
<          call synth
---
>          call synth_scat
61c63
<          call cogsyn  
---
>          call cogsyn_scat  
63c65
<          call blends  
---
>          call blends_scat  
65c67
<          call abfind
---
>          call abfind_scat
67c69
<          call ewfind
---
>          call ewfind_scat
69c71
<          call cog
---
>          call cog_scat
73c75
<          call doflux   
---
>          call doflux_scat   
77c79
<          call gridsyn  
---
>          call gridsyn_scat  
81c83
<          call binary
---
>          call binary_scat
83c85
<          call abpop
---
>          call abpop_scat
85c87
<          call synpop
---
>          call synpop_scat
106d107
< 
108a110,111
> 1002  format ('The "isotop" driver is obsolete; "synth" does ',
>      .        'its functions now!')

>>> Moogsilent [!UNEXPECTED CHANGES]
2c2
<       program moogsilent
---
>       program moogsilent_scat
4c4
< c     This is the main driver for the non-interactive version of MOOG.  
---
> c     This is the main driver for "non-interactive" version of MOOG.
6c6
< c     subroutines.  In this version of MOOG the parameter file must
---
> c     subroutines.  In this version of MOOG, the parameter file must
8c8
< c     user to name the parameter file)
---
> c     user to name the parameter file).      
12a13
>       character yesno*1
16c17
< c     in compiling MOOG, here the various machine-specific things are
---
> c*****in compiling MOOG, here the various machine-specific things are 
19c20
< c     generate a reminder of this
---
> c     generate a reminder of this necessity
22c23
<      .  '/Users/chris/CODES/moognov2019/'
---
>      .  '/Users/jsobeck/moog_SCAT-update'
42c43
< c*****declare this to be the non-interactive version; variable "silent"
---
> c*****declare this to be the normal interactive version; variable "silent"
51c52
<       control = '       '
---
> 1     control = '       '
58,59d58
<       elseif (control .eq. 'isoplot') then
<          call plotit
61c60
<          call synth
---
>          call synth_scat
63c62
<          call cogsyn  
---
>          call cogsyn_scat  
65c64
<          call blends  
---
>          call blends_scat  
67c66
<          call abfind
---
>          call abfind_scat
69c68
<          call ewfind
---
>          call ewfind_scat
71c70
<          call cog
---
>          call cog_scat
74,76d72
<       elseif (control .eq. 'isotop ') then
<          control = 'synth  '
<          call synth
78c74
<          call doflux   
---
>          call doflux_scat   
82c78
<          call gridsyn  
---
>          call gridsyn_scat  
86c82
<          call binary
---
>          call binary_scat
88c84
<          call abpop
---
>          call abpop_scat
90c86
<          call synpop
---
>          call synpop_scat
100c96
<          array = 'THIS IS NOT ONE OF THE DRIVERS. I QUIT!'
---
>          array = 'THIS IS NOT ONE OF THE DRIVERS.  TRY AGAIN (y/n)?'
102c98,104
<          stop
---
>          istat = ivmove (3,1)
>          read (*,*) yesno
>          if (yesno .eq. 'y') then
>             go to 1
>          else
>             call finish (0)
>          endif
104a107,108
> c*****Call the Ang_Weight_SCAT routine
>         call ang_weight_SCAT
107a112,114
> 1002  format ('The "isotop" driver is obsolete; "synth" does ',
>      .        'its functions now!')
> 1003  format (22x,'MOOG IS CONTROLLED BY DRIVER ',a7)
109c116
< 1018  format ('x11 -bg black -title MOOGplot -geom 1200x400+20+450')
---
> 1018  format ('x11 -bg black -title MOOGplot -geom 1200x350+20+450')
113a121,122
> 


>>> Oneline [!UNEXPECTED CHANGES]
2c2
<       subroutine oneline (imode)                                    
---
>       subroutine oneline_scat (imode)                                    
10a11
>       include 'Scat.com'
12a14
>       real*8 d_lc
40,42c42,46
<          call cdcalc(1)
<          first = 0.4343*cd(1)
<          flux = rinteg(xref,cd,dummy1,ntau,first)
---
> c         call cdcalc(1)
>          call cdcalc_SCAT (1)
> c         first = 0.4343*cd(1)
> c         flux = rinteg(xref,cd,dummy1,ntau,first)
>          flux = Flux_cont_moog
57,59c61,66
<          call cdcalc(2)
<          first = 0.4343*cd(1)
<          d(1) = rinteg(xref,cd,dummy1,ntau,first)
---
> c         call cdcalc(2)
>          call cdcalc_SCAT (2)
> c         first = 0.4343*cd(1)
> c         d(1) = rinteg(xref,cd,dummy1,ntau,first)
>          d(1) = adepth 
>          d_lc = adepth                                                  | Depth at Line Center                    
65c72
<             wave = wave1(lim1) + 5.*st1
---
>             wave = wave1(lim1) + 5.*st1                                 | Wavelength Step 
67,69c74,77
<             call cdcalc(2)
<             first = 0.4343*cd(1)
<             d(2) = rinteg(xref,cd,dummy1,ntau,first)       
---
> c            call cdcalc(2)
>             call cdcalc_SCAT (2)
> c            first = 0.4343*cd(1)
>             d(2) = adepth   
96,98c104,108
<          call cdcalc(2)
<          first = 0.4343*cd(1)
<          d(n) = rinteg(xref,cd,dummy1,ntau,first)       
---
> c         call cdcalc(2)
>          call cdcalc_SCAT (2)
> c         first = 0.4343*cd(1)
> c         d(n) = rinteg(xref,cd,dummy1,ntau,first)    
>          d(n) = adepth 
100,109c110,119
<             do i=1,ntau
<                dummy1(i) = xref(i)*cd(i)
<             enddo
<             first = 0.
<             cdmean = rinteg(xref,dummy1,dummy2,ntau,first)/
<      .               rinteg(xref,cd,dummy2,ntau,first)
<             do i=1,ntau
<                if (cdmean .lt. cd(i)) exit
<             enddo
<             write (nf1out,1005) lim1, cdmean, i, xref(i)
---
> c            do i=1,ntau
> c               dummy1(i) = xref(i)*cd(i)
> c            enddo
> c            first = 0.
> c            cdmean = rinteg(xref,dummy1,dummy2,ntau,first)/
> c     .               rinteg(xref,cd,dummy2,ntau,first)
> c            do i=1,ntau
> c               if (cdmean .lt. cd(i)) exit
> c            enddo
> c            write (nf1out,1005) lim1, cdmean, i, xref(i)

>>> Synpop [!UNEXPECTED CHANGES]
2c2
<       subroutine synpop
---
>       subroutine synpop_scat
128c128
<             call synspec
---
>             call synspec_scat
132c132
<                isorun = n
---
>                isorun = 1
139c139
<                call synspec
---
>                call synspec_scat
262,265d261
<          if (plotopt .eq. 3) then
<             call smooth (-1,ncall)
<             choice = 'q'
<          else
267d262
<          endif

>>> Synspec [!UNEXPECTED CHANGES]
2c2
<       subroutine synspec
---
>       subroutine synspec_scat
12a13
>       include 'Scat.com'
64,66c65,69
<             call cdcalc (1)  
<             first = 0.4343*cd(1)
<             flux = rinteg(xref,cd,dummy1,ntau,first)
---
> c            call cdcalc (1)
>             call cdcalc_SCAT (1)
> c            first = 0.4343*cd(1)
> c            flux = rinteg(xref,cd,dummy1,ntau,first)
>             flux = Flux_cont_moog
97,99c100,104
<             call cdcalc (2)
<             first = 0.4343*cd(1)
<             d(num) = rinteg(xref,cd,dummy1,ntau,first)
---
> c            call cdcalc (2)
>             call cdcalc_SCAT (2)
> c            first = 0.4343*cd(1)
> c            d(num) = rinteg(xref,cd,dummy1,ntau,first)
>             d(num) = adepth
161,162c166
< 1104  format ('SIMPLE  =                    T / Fits standard'/
<      .        'NAXIS   =     1'/'NAXIS1  = ',i10,/
---
> 1104  format ('SIMPLE  =    t'/'NAXIS   =     1'/'NAXIS1  = ',i10,/

>>> Synth
2c2
<       subroutine synth                   
---
>       subroutine synth_scat                   
96c96
<          call getsyns (lscreen,ncall)
---
>          call getsyns_scat (lscreen,ncall)















