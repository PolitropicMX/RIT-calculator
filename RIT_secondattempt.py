# RIT firs aself.Tself.Tempt
import numpy as np
from math import *

# ALL IMPORTANT FIRST DATA
##dTperm = 20
##Te = np.array([280,230,50,170])
##Ts = np.array([70,110,210,260])
##FCP = np.array([4.5,7.5,6,9])
##Q = np.array([945,900,960,810])

#HOY TOCA COMENTAR ESTE CODIGO PARA CAMBIARLO A JAVASCRIPT
class RIT:
    def __init__(self,Te,Ts,FCP,dT):
        self.Te = Te
        self.Ts = Ts
        self.FCP = FCP
        self.Q = []
        for i,j in enumerate(self.FCP):
            if self.Ts[i]-self.Te[i] < 0:
                self.Q.append(j*(self.Te[i]-self.Ts[i]))
            else:
                self.Q.append(j*(self.Ts[i]-self.Te[i]))
        self.Q = np.array(self.Q)
        self.new_dt = dT/2
        # ALL THESE ARRAYS ABOVE must have the same length
        self.results = np.array([])# Columna que nos dice si es caliente o fria
        self.Te_mod = np.array([])# Te*
        self.Ts_mod = np.array([])# Ts*
        if len(self.Te) == len(self.Ts):# check if they both have the same length
            for i,j in enumerate(self.Te):
                if self.Te[i] > self.Ts[i]:# SI ES CORRIENTE CALIENTE
                    self.results = np.append(self.results,(-1))# ASIGNA UN -1
                else:# SI ES CORRIENTE FRIA
                    self.results = np.append(self.results,(1))# ASIGNA UN +1
            for i,j in enumerate(self.Te):
                self.Te_mod = np.append(self.Te_mod, (self.Te[i]+self.results[i]*self.new_dt))# SE CREA TE*
                self.Ts_mod = np.append(self.Ts_mod, (self.Ts[i]+self.results[i]*self.new_dt))# SE CREA TS*
        print('Para un dT permisible de: ' + str(self.new_dt*2))
        print('   Te   Ts      FCP Q      D/E   Te*   Ts*')
        self.table1 = np.vstack((self.Te,self.Ts,self.FCP,self.Q.T,self.results.T,self.Te_mod.T,self.Ts_mod.T)).transpose()
        print(self.table1)
        
        # AQUI TODO BIEN: Primer tabla completada

        self.alp = set()# SE CREA UN CONJUNTO
        for i,j in enumerate(self.Te_mod):# SE INGRESAN ELEMENTO POR ELEMENTO LOS VALORES DE LOS TE' Y TS'
            self.alp.add(self.Te_mod[i])
            self.alp.add(self.Ts_mod[i])
        self.mfp = list(self.alp)# EL CONJUNTO SE CAMBIA A LIST, ESTO PARA ELIMINAR ELEMENTOS DUPLICADOS
        self.np_mfp = np.array(self.mfp)# AQUI LA LISTA LA COONVERTIMOS A NUMPY ARRAY
        self.np_mfp = np.sort(self.np_mfp)# SE SORTEA DE MENOR A MAYOR
        self.np_mfp = self.np_mfp[::-1]# SE CAMBIA EL SENTIDO DE MAYOR A MENOR   <----- EMPEZAMOS AQUI
        self.ind_np_mfp = np.array([])# SE CREA UN ARRAY NUMPY DE INDICES POR CADA ELEMENTO DE MFP
        for i,j in enumerate(self.np_mfp):
            self.ind_np_mfp = np.append(self.ind_np_mfp, i)    
        self.a, self.b = self.np_mfp[0:len(self.np_mfp)-1],self.np_mfp[1:len(self.np_mfp)]# SE CREAN 2 LISTAS IGUALES PERO, EXCLUYENDO EL PRIMER Y EL ULTIMO ELEMENT0
        self.dT = self.a - self.b# dT = self.Te - self.Ts# SE RESTAN PARA TENER UN ARRAY DE dT
        #FCP*
        # AQUI TODOP BIEN
        # AQUI VIENE LO IMPORTANTE
        self.fcpmodtable = np.zeros((len(self.dT),len(self.FCP)))# SE CREA UN MATRIZ DE MFP SORTED FILAS Y FCP'S COLUMNAS
        self.new_interv_list = np.zeros((len(self.dT),2))## MATRIZ DE MFP SORTED FILAS Y 2 COLUMNAS
        for j,k in enumerate(self.Te_mod):# SE ITERA A TRAVES DE TE'    
            for i,o in enumerate(self.np_mfp):# sE ITERA A TRAVES DE LA LISTA MFP SORTEADA
                if k == o:# SI NP_MFP CONCUERDA EN IGUALDAD CON UN DATO DE TE'
                    self.new_interv_list[j,1] = self.ind_np_mfp[i] # SE GUARDA EL INDICE DE LA CONCURRENCIA SEGUN SU POSICION EN MFP SORTED EN LA SEGUNDA COLUMNA
                if self.Ts_mod[j] == o:# SI NP_MFP CONCUERDA EN IGUALDAD CON UN DATO DE TS'
                    self.new_interv_list[j,0] = self.ind_np_mfp[i] # SE GUARDA EL INDICE DE LA CONCURRENCIA SEGUN SU POSICION EN MFP SORTED EN LA PRIMER COLUMNA
                    # aqui es donde el codigo empieza a disminuir el vasslor mas alto por cada fila menos 1
        self.new_interv = self.new_interv_list[:,0]- self.new_interv_list[:,1]# SE RESTA LA PRIMER COLUMNA MENOS LA SEDUNDA, DEJANDO UN VECTOR SOLAMENTE
        self.sign = np.zeros((len(self.new_interv)))# SE CREA UN VECTOR CON LA MISMA LONGITUD QUE new_interv_list
        for h,k in enumerate(self.new_interv):# SE ITERA A TRAVES DE new_interv_list
            if self.new_interv[h] < 0:# SE ITERA A TRAVES DEL VECTOR, SI EL ELEMENTO ES MENOR A CERO
                self.sign[h] = -1# SE GUARDA UN SIGNO NEGATIVO
            else:
                self.sign[h] = 1# SI ES MAYOR A 1 SE GUARDA UN SIGNO POSITIVO

        # AQUI EMPIEZA LO QUE ESTAMOS BUSCANDO
         
        for i in range(len(FCP)):# SE ITERA A TRAVES DEL ARRAYS DE FCp'S
            if self.new_interv_list[i,0] > self.new_interv_list[i,1]:# SI EL INDICE DE Ts' a Te'
                for k in range(int(self.new_interv_list[i,1]),int(self.new_interv_list[i,0])):
                    self.fcpmodtable[k,i] = self.sign[i]*FCP[i]# SE ASIGNA EL VALOR DEL FCP CORRESPONDIENTE MULTIPLICADO POR SU SIGNO
                for k in range(int(self.new_interv_list[i,0]),len(FCP)):
                    self.fcpmodtable[k,i] = 0
            else:
                for k in range(int(self.new_interv_list[i,0]),int(self.new_interv_list[i,1])):
                    self.fcpmodtable[k,i] = self.sign[i]*FCP[i]
                for k in range(int(self.new_interv_list[i,1]),len(FCP)):
                    self.fcpmodtable[k,i] = 0

        self.fcpmod = np.zeros((len(self.dT)))
        for i,k in enumerate(self.dT):
            self.fcpmod[i] = np.sum(self.fcpmodtable[i,:])
        self.H = np.zeros((len(self.dT)+1))
        for i,k in enumerate(self.dT):
            self.H[i] = self.fcpmod[i]*self.dT[i]
        print('Punto pinch ')
        print('   Te*    Ts*     dT                                 FCP*  H')
        self.table2 = np.vstack((self.a,self.b,self.dT,self.fcpmodtable[:,0],self.fcpmodtable[:,1],self.fcpmodtable[:,2],self.fcpmodtable[:,3],self.fcpmod,self.H[:len(self.H)-1])).transpose()
        print(self.table2)
        print('Cascada de calor')
        print('   T    H            PP')
        self.cascada = np.zeros((len(self.H),2))
        for i,k in enumerate(self.H):
            if i == 0:
                continue
            else:
                self.cascada[i,0] = self.cascada[i-1,0]+ self.H[i-1]
        
        self.lowest = 0
        for i,k in enumerate(self.cascada):
            if self.cascada[i,0] < self.lowest:
                self.lowest = self.cascada[i,0]
        self.cascada[0,1] = -self.lowest
        for i in  range(len(self.H)):
            if i == 0:
                continue
            else:
                self.cascada[i,1] = self.cascada[i-1,1]+ self.H[i-1]
        for f,k in enumerate(self.H):
##            print(str(self.np_mfp[f])+'  '+str(self.H[f])+'  '+str(self.cascada[f,0])+'  '+str(self.cascada[f,1])+'  ')
            if self.cascada[f,1] == 0:
                self.pinch = self.np_mfp[f]
        hot_cold_limit = np.array([self.pinch-self.new_dt,self.pinch+self.new_dt])

        self.table3 = np.vstack((self.np_mfp,self.H,self.cascada[:,0],self.cascada[:,1])).transpose()
        print(self.table3)
        print(f"El punto pinch es: {self.pinch} °C")
        # AQUI EMPIEZA EL ABAJO Y ARRIBA DEL PINCH
        k = 0
        self.teup = np.array([])
        self.tsup = np.array([])
        FCPup = np.array([])
        Qup = np.array([])
        for i,j in enumerate(Te):# por arriba del pinch
            hot_or_cold = j - self.Ts[i]
            if hot_or_cold < 0:# corriente fria
                if j > hot_cold_limit[1] or self.Ts[i] > hot_cold_limit[1]:
                    if j > hot_cold_limit[1]:
                        FCPup = np.append(FCPup, FCP[i])
##                        Qup = np.append(Qup , (FCP[i]*hot_or_cold))
                        self.teup = np.append(self.teup, j)
                    else:
                        FCPup = np.append(FCPup, FCP[i])
##                        Qup = np.append(Qup , (FCP[i]*hot_or_cold))
                        self.teup = np.append(self.teup, hot_cold_limit[0])
                    if self.Ts[i] > hot_cold_limit[1]:
                        self.tsup = np.append(self.tsup, self.Ts[i])
                    else:
                        self.tsup = np.append(self.tsup, hot_cold_limit[1])
                else:
                    continue
            else:# corriente caliente
                if j > hot_cold_limit[1] or self.Ts[i] > hot_cold_limit[1]:
                    if j > hot_cold_limit[1]:
                        FCPup = np.append(FCPup, FCP[i])
                        self.teup = np.append(self.teup, j)
##                        Qup = np.append(Qup , (FCP[i]*hot_or_cold))
                    else:
                        FCPup = np.append(FCPup, FCP[i])
##                        Qup = np.append(Qup , (FCP[i]*hot_or_cold))
                        self.teup = np.append(self.teup, hot_cold_limit[0])
                    if self.Ts[i] > hot_cold_limit[1]:
                        self.tsup = np.append(self.tsup, j)
                    else:
                        self.tsup = np.append(self.tsup, hot_cold_limit[1])
                else:
                    continue
                
        dtup = self.teup - self.tsup
        for i,k in enumerate(dtup):
            Qup = np.append(Qup , (FCP[i]*k))
        self.tedw = np.array([])
        self.tsdw = np.array([])
        FCPdw = np.array([])
        Qdw = np.array([])
        for i,j in enumerate(Te):#por abajo del pinch
            hot_or_cold = j - self.Ts[i]
            if hot_or_cold < 0:# corriente fria
                if j < hot_cold_limit[0] or self.Ts[i] < hot_cold_limit[0]:
                    if j < hot_cold_limit[1]:
                        FCPdw = np.append(FCPdw, FCP[i])
##                        Qdw = np.append(Qdw, (FCP[i]*hot_or_cold))
                        self.tedw = np.append(self.tedw, j)
                    else:
                        FCPdw = np.append(FCPdw, FCP[i])
##                        Qdw = np.append(Qdw, (FCP[i]*hot_or_cold))
                        self.tedw = np.append(self.tedw, hot_cold_limit[1])
                    if self.Ts[i] < hot_cold_limit[1]:
                        self.tsdw = np.append(self.tsdw, self.Ts[i])
                    else:
                        self.tsdw = np.append(self.tsdw, hot_cold_limit[0])
                else:
                    continue
            else:# corriente caliente
                if j < hot_cold_limit[1] or self.Ts[i] < hot_cold_limit[1]:
                    if j < hot_cold_limit[1]:
                        FCPdw = np.append(FCPdw, FCP[i])
                        self.tedw = np.append(self.tedw, j)
##                        Qdw = np.append(Qdw, (FCP[i]*hot_or_cold))
                    else:
                        FCPdw = np.append(FCPdw, FCP[i])
                        self.tedw = np.append(self.tedw, hot_cold_limit[1])
##                        Qdw = np.append(Qdw, (FCP[i]*hot_or_cold))
                    if self.Ts[i] < hot_cold_limit[1]:
                        self.tsdw = np.append(self.tsdw, self.Ts[i])
                    else:
                        self.tsdw = np.append(self.tsdw, hot_cold_limit[0])
                else:
                    continue
        
        dtdw = self.tedw - self.tsdw
        for i,k in enumerate(dtdw):
            Qdw = np.append(Qdw , (FCP[i]*k))
        self.table4 = np.vstack((self.teup,self.tsup,dtup,FCPup,Qup)).transpose()
        self.table5 = np.vstack((self.tedw,self.tsdw,dtdw,FCPdw,Qdw)).transpose()
##        print(self.teup,self.tsup)
        print('Arriba del pinch')
        print(self.table4)
        print('Abajo del pinch')
        print(self.table5)
            

    def tabla1(self):
        return self.table1
    def tabla2(self):
        return self.table2
    def tabla3(self):
        return self.table3
    def pinch_point(self):
        return self.pinch
    def up_pinch(self):
        return self.table4
    def down_pinch(self):
        return self.table5
    
##Rit = RIT(Te,Ts,FCP,Q,dTperm)


            
