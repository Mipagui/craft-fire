# coding: latin-1
import sys, pygame
from movimiento import Movimiento
class Bala(Movimiento):
      """Recibe una lista de figuras creando distintos objetos Movimiento,
	 que corresponderán a las balas.
      """
      def __init__(self,figura,dispara=False):
	  Movimiento.__init__(self,figura)
          self.tiempo_de_vida  = 0
	  self.explocion       = False
	  self.dispara         = dispara #controla  que se dibuje un disparo
	  self.posx            =figura.rectangulo.x
	  self.posy            =figura.rectangulo.y

      def reiniciar(self):
          self.tiempo_de_vida  = 0
	  self.explocion       = False
          self.dispara         = False
	  self.figura.rectangulo.x = self.posx
	  self.figura.rectangulo.y = self.posy


      def balas_pasaron_los_limite(self):
	  """Si hay una bala que pasa los limites retorna True
	  """
	  if not self.esta_en_area_de_juego():
                 self.dispara = False
		 return True
	  return False

      def disparo_vertical(self,screen,posx,posy,vy,separacion):
          #si la bala pasa los límites  comienza en posx y posy
	  if self.balas_pasaron_los_limite(): self.reiniciar()
	  if not self.explocion and self.dispara:
	         self.mover_vertical(screen,vy)
	  else: self.reiniciar()

      def disparo_vertical_circular(self,screen,posx,posy,vx,vy,separacion,tiempo,tiempo_de_duracion,orientacion="posy",paso=5):
	  if self.balas_pasaron_los_limite(): self.reiniciar()
	  if not self.explocion and self.dispara:
		 self.mover_circular(screen,vx,vy,tiempo,tiempo_de_duracion,orientacion,paso)
	  else: self.reiniciar()

      def disparo_diagonal(self,screen,posx,posy,vx,vy):
	  if self.balas_pasaron_los_limite(): self.reiniciar()
	  if not self.explocion and self.dispara: self.mover_diagonal(screen,vx,vy)           
	  else: self.reiniciar()
       
      def disparo_escudo(self,screen,posx,posy,vx,vy,separacion):
	  if self.balas_pasaron_los_limite() or self.tiempo_de_vida == 0:
	     xx=[separacion,-separacion,0,0,separacion,separacion,-separacion,-separacion]
	     yy=[0,0,separacion,-separacion,-separacion,separacion,-separacion,separacion]
             for i in range(len(self.balas)):
                 self.balas[i].figura.rectangulo.x= posx + xx[i]
                 self.balas[i].figura.rectangulo.y= posy + yy[i] 
	     
	  if not self.explocion and (len(self.balas) >= 4 and self.dispara):
             for i in range(len(self.balas)):
                 if   i ==0: self.balas[0].mover_horizontal(screen,vx)
                 elif i ==1: self.balas[1].mover_horizontal(screen,-vx)
                 elif i ==2: self.balas[2].mover_vertical(screen,-vy)
                 elif i ==3: self.balas[3].mover_vertical(screen,vy)
                 elif i ==4: self.balas[4].mover_diagonal(screen,vx,-vy)
                 elif i ==5: self.balas[5].mover_diagonal(screen,vx,vy)
                 elif i ==6: self.balas[6].mover_diagonal(screen,-vx,vy)
                 elif i ==7: self.balas[7].mover_diagonal(screen,-vx,-vy)
	     self.tiempo_de_vida+=1
	  else: self.reiniciar()
