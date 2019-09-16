"""


"""

class module:
	
	class angle:        
		def __init__(self,curr):   # mi= min  ma=max  curr=angle to be set
			self.curr=curr            
		
		def setAngle(self,curr,motno):
			print(curr," ",motno)
		
		def setParentAng(self,pangtype,curr):
			if pangtype=="t":
				print("parentTopAngle:",curr)
			else:
				print("parentAng(",pangtype,"):",curr)


	def __init__(self,modtag, parent,prot, link,phib,deltab,phit,deltat):  #for multiple modules modtag=tag of module; parent=parent module tag;prot=relative rotation between parent and current module
		self.tag=modtag
		self.linktype=link
		self.parent=parent
		
		if link == 1:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='p'
			pangtype='t'
		elif link == 2:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='t'
		elif link == 3:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='t'
		elif link == 6:
 			min1=-90
 			max1=90
 			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='a'
			motno=6
		elif link == 7:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='a'
			motno=5
		elif link == 8:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='a'
			motno=5 
		elif link == 9:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='a'
			motno=6 
		elif link == 10:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='a'
			motno=6 
		elif link == 11:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='a'
			motno=5 
		elif link == 12:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='t'
		elif link == 13:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='p'
			pangtype=6
			prot=-prot
		elif link == 14:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='p'
			pangtype=6
			prot=-prot
		elif link == 15:
  			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='p'
			pangtype=5
			prot=-prot
		elif link == 16:
			min1=-90
			max1=90
			min2=-180
			max2=180
			min3=-90
			max3=90
			min4=-180
			max4=180
			phib= self.limit(min1,max1,phib)
			deltab=self.limit(min2,max2,deltab)
			phit=self.limit(min3,max3,phit)
			deltat=self.limit(min4,max4,deltat)
			contype='p'
			pangtype=5
			prot=-prot

		"""

		if contype=='a':
			self.conv(prot,motno,link,phib,deltab,phit,deltat)    #connection type(contype) is the type angle requires for realtive rot between the modules ,ie t=top disk,p=parent,a=is for active disk
		elif contype=='t':
			self.conv(prot,phib,deltab,phit,deltat)
		elif contype=='p':
			self.conv(prot,phib,deltab,phit,deltat,pangtype)      #pangtype=parent angle type it top ot anything else
	#	self.tag=modtag
	#	self.phi=phi
	#	self.delta=delta
	#	self.conv(phi,delta)

	def limit(self,mi,ma,curr): 
		if curr<mi:
			return mi;
		elif curr>ma:
			return ma;
		else:
			return curr;

	def conv(self,phi,delta):            #for a single module
		ang1=module.angle(-delta)
		ang2=module.angle(delta)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang1=module.angle(phi)
		ang2=module.angle(phi)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)

	def conv(self,prot,motno,link,phib,deltab,phit,deltat):
 		ang1=module.angle(-deltab)
		ang2=module.angle(deltab)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang1=module.angle(phib)
		ang2=module.angle(-phib)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang3=module.angle(-deltat)
		ang4=module.angle(deltat)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)                 
		ang3=module.angle(phit)
		ang4=module.angle(-phit)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)
		angx=module.angle(prot)
		angx.setAngle(angx.curr,motno)

	def conv(self,prot,phib,deltab,phit,deltat):
 		ang1=module.angle(-deltab)
		ang2=module.angle(deltab)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang1=module.angle(phib)
		ang2=module.angle(-phib)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang3=module.angle(-deltat)
		ang4=module.angle(deltat)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)                 
		ang3=module.angle(phit)
		ang4=module.angle(-phit)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)
		ang3=module.angle(-prot)
		ang4=module.angle(prot)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)

	def conv(self,prot,phib,deltab,phit,deltat,pangtype):
 		ang1=module.angle(-deltab)
		ang2=module.angle(deltab)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang1=module.angle(phib)
		ang2=module.angle(-phib)
		ang1.setAngle(ang1.curr,1)
		ang2.setAngle(ang2.curr,2)
		ang3=module.angle(-deltat)
		ang4=module.angle(deltat)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)                 
		ang3=module.angle(phit)
		ang4=module.angle(-phit)
		ang3.setAngle(ang3.curr,3)
		ang4.setAngle(ang4.curr,4)
		if pangtype=='t':
			pang=module.angle(prot)
			pang.setParentAng('t',pang.curr)
		else:
			pang=module.angle(prot)
			pang.setParentAng(pangtype,pang.curr)

"""
if __name__ == "__main__":
	print("Inside main")
	mod1=module(2,1,45,1,30,60,25,67)