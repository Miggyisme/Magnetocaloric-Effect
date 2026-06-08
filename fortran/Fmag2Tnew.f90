program NewmediaU
    implicit real*8 (a-h,o-z)
	DIMENSION FBV(5000),TV(5000),F1V(5000),F2V(5000),F3V(500),AMAGV(5000)
	DIMENSION UMEDV(5000),SMNUMV(5000)


    ! unidades em Joules
!****** parametros de entrada *********************************************
!    ak=1.38d-23   ! em joules
!    amib=9.274D-24	   ! em joules
	G=2.0
	AJ=1.0/2.0
!	aj0=0.0001
!	aj0=0.01
    avog=6.02d23
    AR=8.31
    ! unidades em  eletronvoltz


    ak=8.617d-5	   ! em eV/K
    amib=5.78838d-5	  !em ev/T
!	amib=1.0


      OPEN(UNIT=20,STATUS='UNKNOWN',FILE='energiaT.DAT')
      OPEN(UNIT=30,STATUS='UNKNOWN',FILE='probT.DAT')
      OPEN(UNIT=40,STATUS='UNKNOWN',FILE='magT.DAT')
	  OPEN(UNIT=50,STATUS='UNKNOWN',FILE='m1m2.DAT')
      OPEN(UNIT=60,STATUS='UNKNOWN',FILE='AJ0.DAT')
      OPEN(UNIT=70,STATUS='UNKNOWN',FILE='SUSCN.DAT')
      OPEN(UNIT=80,STATUS='UNKNOWN',FILE='SUSCA.DAT')
	  OPEN(UNIT=90,STATUS='UNKNOWN',FILE='ENTROP.DAT')
	  OPEN(UNIT=100,STATUS='UNKNOWN',FILE='SHEAT.DAT')
	  OPEN(UNIT=101,STATUS='UNKNOWN',FILE='FREENUM.DAT')
	  OPEN(UNIT=102,STATUS='UNKNOWN',FILE='SNUM2.DAT')
  	  OPEN(UNIT=103,STATUS='UNKNOWN',FILE='SUSCN2.DAT')

     write (*,*) 'Entre com o valor dO campo magnetico  EM TESLA.'
     read (*,*) B
     write (*,*) 'Entre com o valor da interacao de troca J0 em eV (j0= 0.004).'
     read (*,*) ajf

      write (*,*) 'Entre com o valor da interacao de troca J1 em eV (j1= 0.02).'
     read (*,*) aj1


	 
!	 AJI=0.8*AJF
	 AJI=1.0*AJF
!	 AJI=1.2*AJF


!	 AJ00=AJ0
!	 DELTA=0.0000002
	 IJ=1
!      TC=AJf*AJ*(AJ+1)/(3.0*AK*amib)
      TC=AJF*AJ*(AJ+1)/(3.0*AK)

      TC1=AJf/(4.0*AK*amib)

!	  TC=AJ0/(3.0*AK)



	 Write (*,*) 'tc tc1 ' , tc,tc1
     pause 



     Write (*,*) 'Tmin, Tmax, nT'
     read (*,*) Tmin,Tmax, nT
      !     CRIT=0.000001
!        CRIT=0.0000000001
		CRIT=0.000000000001
        dT=(Tmax-Tmin)/dfloat(nT)
!		 DELTAB=0.000000000001
		 DELTAB=0.00001
		 DELTAT=0.00001

      do i = 1 , nT+1 , 1
         T=Tmin+(i-1)*dT


		 IF(IJ.EQ.1) THEN
		 if (T.LT.TC) THEN
!		 AJ0=(DELTA/TC)*T+(AJ00-DELTA)
!         AJ0=-(DELTA/TC)*T+(AJ00+DELTA)
         AJ0=AJI+(AJF-AJI)*(T/TC)


		 END IF
		 END IF

		 B2=B+DELTAB
	 	 B3=B2+DELTAB


	  AM=G*AJ*AMIB
      beta = (1.0)/(ak*t)
	  betaT = (1.0)/(ak*(t+DELTAT))
!  2	  BEF=B+(AJ0*AM)/(G*G*AMIB*AMIB)
!   	  BEFB=B2+(AJ0*AM)/(G*G*AMIB*AMIB)

 2	  BEF=B+(AJ0*AM)/(G*G*AMIB*AMIB)+(AJ1*(AM**3))/(G*G*G*G*AMIB*AMIB*AMIB*AMIB)
   	  BEFB=B2+(AJ0*AM)/(G*G*AMIB*AMIB)+(AJ1*(AM**3))/(G*G*G*G*AMIB*AMIB*AMIB*AMIB)
      BEFB3=B3+(AJ0*AM)/(G*G*AMIB*AMIB)+(AJ1*(AM**3))/(G*G*G*G*AMIB*AMIB*AMIB*AMIB)




!************* CALCULO DAS GRANDEZAS PARA B=B *****************************
      E1=amib*g*Bef*aj
	  E2=-amib*g*Bef*aj

      E1b=amib*g*Befb*aj
	  E2b=-amib*g*Befb*aj


      E1b3=amib*g*Befb3*aj
	  E2b3=-amib*g*Befb3*aj

      z=Dexp(-beta*E1)+Dexp(-beta*E2)
      zt=Dexp(-betat*E1)+Dexp(-betat*E2)
	  ztbdb=Dexp(-beta*E1B)+Dexp(-beta*E2B)

	  E1M=(E1*exp(-BETA*E1))/z
      E2M=(E2*exp(-beta*E2))/z


	  FB=-AK*T*DLOG(Z)
	  FBT=-AK*(T+deltaT)*DLOG(ZT)
	  F3V(I)=AK*T*T*T
!  	 Write (*,*) 'T FBJ ' , T, FBJ
!     pause 


 !************* CALCULO DAS GRANDEZAS PARA B=B+dB *************************
      E1B=amib*g*BefB*aj
	  E2B=-amib*g*BefB*aj
	  zB=Dexp(-beta*E1B)+Dexp(-beta*E2B)
  	  zBt=Dexp(-betat*E1B)+Dexp(-betat*E2B)

 
	  E1BM=(E1B*Dexp(-BETA*E1B))/zB
      E2BM=(E2B*Dexp(-beta*E2B))/zB




	  FBMDB=-AK*T*DLOG(ZB)
	  FBMDBt=-AK*(T+deltat)*DLOG(ZBt)
! CÁLCULO DA ENERGIA MAGNETICA MEDIA ******************************************
!      z=exp(beta*amib*g*Bef*aj)+exp(-beta*amib*g*Bef*aj)
      U1=(-amib*g*Bef*aj*exp(beta*amib*g*Bef*aj))/z
      U2=(amib*g*Bef*aj*exp(-beta*amib*g*Bef*aj))/z
      umed=U1+U2
	  UMEDV(I)=UMED
!      STEO=AK*DLOG(Z)+UMED

! cÃƒÂ¡lculo da probabilidade ( colocar as expressÃƒÂµes para a probabilidade )
      P1=exp(beta*amib*g*Bef*aj)/z
      P2=exp(-beta*amib*g*Bef*aj)/z
      P=P1+P2
!****************** CÁLCULO DA MAGNETIZAÇÃO (MÉTODO 1: MÉDIA DOS MOMENTOS)****
      am1=amib*exp(beta*amib*g*Bef*aj)/z
!      am1=am1/amib
      am2=-amib*exp(-beta*amib*g*Bef*aj)/z
!      am2=am2/amib


  	  am1b=amib*exp(beta*amib*g*Befb*aj)/zb
!      am1b=am1b/amib
      am2b=-amib*exp(-beta*amib*g*Befb*aj)/zb
!      am2b=am2b/amib


!      am2=amib*exp(-beta*amib*B)/z
      amc=am1+am2
	  amcb=am1b+am2b

!********** quadrado do momento *********************************************************

     am12=amib*amib*exp(beta*amib*g*Bef*aj)/z
     am22=amib*amib*exp(-beta*amib*g*Bef*aj)/z
	 VMAMQ=(am12+am22)/AMIB

!	   DIF=AMC-AM
       DIF=DABS(AMC-AM)
	  IF (DIF.gt.CRIT) THEN
	  am=amc
	  go to 2
	  ELSE
	  am=amc
	  END IF


	  QVMAM=(AMC*AMC)/AMIB
	  QUIG=(VMAMQ-QVMAM)/(AK*T)

!   	  write(*, 210) T, VMAMQ,QVMAM,QUIG
!	  PAUSE


	  AMAGV(I)=AMC
 	  FBV(I)=FB
	  TV(I)=T
      FBJ=FB*avog*1.60218d-19
	  F1V(I)=AK*T
	  F2V(I)=DLOG(Z)
!	  F2V(I)=T*T
!	  F3V(I)=AK*T*T*T

!****************** CÁLCULO DA MAGNETIZAÇÃO (MÉTODO 2: DERIVADA DA ENERGIA)**** 

      AX=(G*AMIB*BEF)/(2.0*AK*T)
	  SECH=1.0/COSH(AX)
	  SECH2=SECH*SECH

	  TC2=(AJf*SECH2)/(4.0*AK*amib)
!  	  TC3=(AJf*SECH2)/(4.0*AK)
	  TC3=((AJf+(3.0*aj1*AM*AM)/(G*G*AMIB*AMIB))*SECH2)/(4.0*AK)


!	  TC2=AJf*G*G*SECH2/(4.0*AK*amib)
	  CA2=(G*G*AMIB*AMIB)/(4.0*AK)
	  CA=(G*G*amib)/(4.0*AK)
!	  SUSCA=(CA*SECH2)/(T-TC2)
	  SUSCA=(CA2*SECH2)/(T-TC3)
	  ALAMB=AJ0/(G*G*amib*amib)

!********** CÁLCULO DA SUSCEPTIBILIDADE MAGNÉTICA **********************************************
!  	  SUSCN=g*amib*((AMCB-AMC)/DELTAB)
	  SUSCN=((AMCB-AMC)/DELTAB)
!	  SUSCN=SUSCN/AMIB
!      SUSCN2=SUSCN*(1.0+(ALAMB*(AMCB-AMC))/DELTAB)
	  SUSCN2=SUSCN/(1.0-(ALAMB*(AMCB-AMC))/DELTAB)

	  if(suscn.ne.0) then
	  suscnI=1.0/suscn
	  end if

	  DE1DB=-(E1B-E1)/DELTAB
	  AM1N2=(DE1DB*exp(-BETA*E1B))/z
      AM1N2=AM1N2/AMIB


	  DE2DB=-(E2B-E2)/DELTAB
	  AM2N2=(DE2DB*exp(-BETA*E2B))/z
	  AM2N2=AM2N2/AMIB
	  AMNT=AM1N2+AM2N2

 !********************CÁLCULO DA ENTROPIA **********************************************
      E1AN=-(G*AMIB*BEF)/(2.0*AK)*TANH(BETA*amib*BEF)
  	  st1=	  dlog(2.0*cosh(ax))
      st2=	  E1AN/T
	  SMAN=ar*(st1+st2)
	  SMNUM=-((FBT-FB)/DELTAT)
!   conversão de eV para Joule
!     SMNUM=-((FBT-FB)/DELTAT)*1.619d-19
!   conversão de eV para Joule/mol

	 SMNUM=-avog*((FBT-FB)/DELTAT)*1.60218d-19
	 SMNUMV(I)=SMNUM
	 STEO=AK*DLOG(Z)+(UMED/T)
	 STEO=STEO*(avog*1.60218d-19)



!  	 SB0= -(FBT-FB)/DELTAT
!     SB5= -(FBMDBT-FBT)/DELTAT


!****************** CÁLCULO DA MAGNETIZAÇÃO (MÉTODO 3: DERIVADA DA ENERGIA LIVRE)****
   
	 SB0= -(FBT-FB)/DELTAT
	 SB5= -(FBMDBT-FBT)/DELTAT


	 
	  AMN2=-(FBMDB-FB)/DELTAB
	  AMN2=AMN2/AMIB

 !****************** CÁLCULO DA MAGNETIZAÇÃO (MÉTODO 4: FUNÇÃO ANALÍTICA TANH)****
   
	  AMAN=AMIB*TANH(BETA*amib*BEF)
!	  TAH=SINH(BETA*amib*B)/COSH(BETA*amib*B)
	  AMAN=AMAN/AMIB

! Cálculo da capacidde termica  analitica tanh )****************)
	  
!	  AX=(G*AMIB*BEF)/(2.0*AK*T)
!	  SECH=1.0/COSH(AX)
!	  TC2=(AJf*SECH2)/(4.0*AK*amib)
	  DMDTN=(G*G*AMIB*AMIB*BEF*SECH2)/(4.0*AK*T)
	  DMDTD=T-TC3
	  DMDTANL=-DMDTN/DMDTD
	  QUIANL2=-(T/BEF)*DMDTANL

!***********CAPACIDADE TÉRMICA ************************************
	  CAH=(G*G*amib*AMIB*BEF*BEF)/(4.0*AK*T)
	  TD= SECH2*(AJF*G*G*amib*AMIB)/(4.0*AK)
  	  CDEN=T-TC3
	  SHEATAN=(CAH*SECH2)/CDEN
	  SHEATANJ=SHEATAN*AVOG*1.60218d-19

	   
      write(20, 210) T, U1, U2, umed
      write(30, 210) T, P1, P2, P
!      write(40, 210) T, am1, am2, am,AMN2
!      write(40, 210) T, amC/AMIB, AMNT,aMN2,AMAN
      write(40, 210) T, amC/AMIB

      write(50, 210) T, am1, am2, am1N2,AM2N2,AMC,AMNT
      write(60, 210) T, AJ0*1000,TC
	  write(70, 210) T, SUSCN, SUSCN2
  	  write(80, 210) T, SUSCA,TC3,SB0
!  	  write(80, 210) T, VMAMQ,QVMAM,QUIG

	  write(90, 210) T, SMAN,SMNUM,STEO
	  write(100, 210) T, SHEATAN,SHEATANJ,TC2,tc3
!	  write(100, 210) T, BEF, (T/BEF),DMDTANL,QUIANL2

!      write(101, 211) T, Z, FBJ
      write(101, 211) T, Z, LOG(Z),AK*T,-AK*T*LOG(Z),FB

!  	 Write (*,*) 'T FBJ ' , T, FBJ
!     pause 	  
	   end do

	 DO 23 J=1,NT-1
	 DMDTNUM=(AMAGV(J+1)-AMAGV(J))/(TV(J+1)-TV(J))
	 DSDT=(SMNUMV(J+1)-SMNUMV(J))/(TV(J+1)-TV(J))
!	 AM=AMAGV(J)/AMIB
 	 AM=AMAGV(J)

	 BEF=B+(AJ0*AM)/(G*G*AMIB*AMIB)+(AJ1*(AM**3))/(G*G*G*G*AMIB*AMIB*AMIB*AMIB)
	 QUINUM=-1.0d00*(TV(J)/BEF)*DMDTNUM
	 SHEATNUM=-BEF*DMDTNUM
	 SHEATNUM= SHEATNUM*(avog*1.60218d-19)

	 SHEATNUM2=TV(J)*DSDT
!	 SHEATNUM= SHEATNUM2*(avog*1.60218d-19)


	 SNUM2=-(FBV(J+1)-FBV(J))/(TV(J+1)-TV(J))
	 SNUM2= avog*SNUM2*1.60218d-19
!	 SMNUMV(I)=SNUM2
!****** SNUM2 NÃO ESTÁ FUNCIONANDO ********************************************
	 DF1=(F1V(J+1)-F1V(J))/(TV(J+1)-TV(J))
     DF2=(F2V(J+1)-F2V(J))/(TV(J+1)-TV(J))
	 DF3=(F3V(J+1)-F3V(J))/(TV(J+1)-TV(J))
	 DFT1=DF1*F2V(J)
	 DFT2=F1V(J)*DF2
	 DF=DFT1+DFT2
     DFJ= avog*DF*1.60218d-19
	 CESP4=(UMEDV(J+1)-UMEDV(J))/(TV(J+1)-TV(J))
	 CESP4=CESP4*(avog*1.60218d-19)
    write(102, 210) TV(J), SNUM2,DFJ
    write(103, 210) TV(J),DMDTNUM,QUINUM,CESP4,SHEATNUM,SHEATNUM2
!    write(102, 211) TV(J),BEF, TV(J)/BEF, DMDTNUM,QUINUM


  23 CONTINUE

 211   format (7(1x,d14.7))
 210   format (8(1x,f22.10))

    close(20)
    close(30)
    close(40)
  	 Write (*,*) 'aj0 alamb ', aj0,alamb
	 pause


end program

