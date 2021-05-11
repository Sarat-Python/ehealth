from google.appengine.ext import blobstore, db, webapp, webapp
from google.appengine.ext.webapp import blobstore_handlers, template
from google.appengine.ext.webapp.util import run_wsgi_app
from util.sessions import Session
import base64
import logging
import os
import re
import wsgiref.handlers
#from google.appengine.ext.webapp import util
_DEBUG = True


class Counter(db.Model):
    counter=db.IntegerProperty()
#co=Counter(counter=100)
#co.put()    

class UserProfile(db.Model):                        
    firstName=db.StringProperty()
    lastName=db.StringProperty()   
    email=db.StringProperty()  
    password=db.StringProperty()
    userType=db.StringProperty()
    bloodGroup=db.StringProperty()
    dob=db.StringProperty()
    birthDay=db.StringProperty()
    birthMonth=db.StringProperty()
    birthYear=db.StringProperty()
    gender=db.StringProperty()
    maritalStatus=db.StringProperty()
    address=db.PostalAddressProperty()
    street=db.StringProperty()
    city=db.StringProperty()
    state=db.StringProperty()
    country=db.StringProperty()
    pincode=db.StringProperty()
    fax=db.IntegerProperty()
    phone=db.StringProperty()
    email2=db.EmailProperty()
    identityDisclose=db.BooleanProperty()
    userId=db.StringProperty()
    occupation=db.StringProperty()
    newField=db.StringProperty()

class DoctorProfile(db.Model):                        
    firstName=db.StringProperty()
    lastName=db.StringProperty()   
    email=db.StringProperty()  
    password=db.StringProperty()
    userType=db.StringProperty()
    bloodGroup=db.StringProperty()
    dob=db.DateProperty()
    gender=db.StringProperty()
    maritalStatus=db.StringProperty()
    address=db.PostalAddressProperty()
    street=db.StringProperty()
    city=db.StringProperty()
    state=db.StringProperty()
    country=db.StringProperty()
    pincode=db.IntegerProperty()
    fax=db.IntegerProperty()
    phone=db.StringProperty()
    email2=db.EmailProperty()
    identityDisclose=db.BooleanProperty()
    doctorId=db.StringProperty()
    specialization=db.StringProperty()
    hospital=db.StringProperty()
    newField=db.StringProperty()

class Hospital(db.Model):                        
    hospitalName=db.StringProperty()
    contactPerson=db.StringProperty()   
    contactPerson2=db.StringProperty()   
    email=db.StringProperty()  
    password=db.StringProperty()
    userType=db.StringProperty()
    address=db.PostalAddressProperty()
    street=db.StringProperty()
    city=db.StringProperty()
    state=db.StringProperty()
    country=db.StringProperty()
    pincode=db.IntegerProperty()
    fax=db.IntegerProperty()
    phone=db.PhoneNumberProperty()
    phone2=db.PhoneNumberProperty()
    email2=db.EmailProperty()
    website=db.StringProperty()
    identityDisclose=db.BooleanProperty()
    doctorId=db.StringProperty()
    specialization=db.StringProperty()
    newField=db.StringProperty()

class Bloodbank(db.Model):                        
    bloodBank=db.StringProperty()
    contactPerson=db.StringProperty()   
    contactPerson2=db.StringProperty()   
    email=db.StringProperty()  
    password=db.StringProperty()
    userType=db.StringProperty()
    address=db.PostalAddressProperty()
    street=db.StringProperty()
    city=db.StringProperty()
    state=db.StringProperty()
    country=db.StringProperty()
    pincode=db.IntegerProperty()
    fax=db.IntegerProperty()
    phone=db.PhoneNumberProperty()
    phone2=db.PhoneNumberProperty()
    email2=db.EmailProperty()
    website=db.StringProperty()
    bloodBankId=db.StringProperty()
    newField=db.StringProperty()
 
class Others(db.Model):                        
    other=db.StringProperty()
    contactPerson=db.StringProperty()   
    contactPerson2=db.StringProperty()   
    email=db.StringProperty()  
    password=db.StringProperty()
    userType=db.StringProperty()
    address=db.PostalAddressProperty()
    street=db.StringProperty()
    city=db.StringProperty()
    state=db.StringProperty()
    country=db.StringProperty()
    pincode=db.IntegerProperty()
    fax=db.IntegerProperty()
    phone=db.PhoneNumberProperty()
    phone2=db.PhoneNumberProperty()
    email2=db.EmailProperty()
    website=db.StringProperty()
    otherId=db.StringProperty()
    newField=db.StringProperty()

class Wellness(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()
    
    weight=db.StringProperty()
    height=db.StringProperty()   
    bmi=db.StringProperty()   
    bmiGoal=db.StringProperty()
    bmiNote=db.StringProperty()
    
class BloodPressure(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()
    
    bloodPressure1=db.StringProperty()  
    bloodPressure2=db.StringProperty()
    bpGoal=db.StringProperty()
    bpNote=db.StringProperty()
    
class Exercise(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()
    
    exerciseTime=db.StringProperty()
    exerciseGoal=db.StringProperty()
    exerciseNote=db.StringProperty()
      
class Walking(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()
    walkingDist=db.StringProperty()
    walkingDistGoal=db.StringProperty()
    walkingTime=db.StringProperty()
    walkingTimeGoal=db.StringProperty()
    walkingNote=db.StringProperty()
    
class Swim(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()    
    
    swimDist=db.StringProperty()
    swimDistGoal=db.StringProperty()
    swimTime=db.StringProperty()
    swimTimeGoal=db.StringProperty()
    swimNote=db.StringProperty()
    
class Sugar(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()    

    
    sugarLevel=db.StringProperty()
    sugarLevelGoal=db.StringProperty()
    sugarLevelNote=db.StringProperty()
    
class Sleep(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()    
    
    sleepTime=db.StringProperty()
    sleepTimeGoal=db.StringProperty()
    sleepTimeNote=db.StringProperty()
    
    
class Cycling(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()
    
    cyclingDist=db.StringProperty()
    cyclingtGoal=db.StringProperty()
    cyclingTime=db.StringProperty()
    cyclingTimeGoal=db.StringProperty()
    cyclingNote=db.StringProperty()
  
class Temperature(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()
        
    temperature=db.StringProperty()
    temperatureGoal=db.StringProperty()
    temperatureNote=db.StringProperty()
    
class Heart(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()    
    
    heartRate=db.StringProperty()
    heartRateGoal=db.StringProperty()
    heartRateNote=db.StringProperty()
  
class NewField(db.Model):       
    user=db.StringProperty()
    userId=db.StringProperty()
    collectionDate=db.StringProperty()     
    newField1=db.StringProperty()
    newField2=db.StringProperty()
    newField3=db.StringProperty()
    
class MyFile(db.Model): 
    filedata = db.BlobProperty()


class BPHandler(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        heart=Heart.all().filter('user', uservalue)
        tempe=Temperature.all().filter('user', uservalue)
        blood=BloodPressure.all().filter('user', uservalue)
        template_values = {'msg':'','tempe':tempe,'heart':heart,'blood':blood,'session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','bloodpressure.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','bloodpressure.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            bp1=self.request.get('bldprs1')
            bp2=self.request.get('bldprs2')
            colDate=self.request.get('cdate')
            bpGoal=self.request.get('bpgoal')
            if bp1 and bp2 and bpGoal and colDate:
                blood1=BloodPressure.all().filter('user', uservalue).filter('collectionDate', colDate).fetch(1)
                blood=BloodPressure.all().filter('user', uservalue)
                if blood1:
                    for a in blood1:
                        a.bloodPressure1=self.request.get('bldprs1')
                        a.bloodPressure2=self.request.get('bldprs2')
                        a.bpGoal=self.request.get('bpgoal')
                        a.bpNote=''
                        a.put()
                    directory = os.path.dirname(__file__)
                    heart=Heart.all().filter('user', uservalue)
                    tempe=Temperature.all().filter('user', uservalue)
                    blood=BloodPressure.all().filter('user', uservalue)
                    template_values = {'bpmsg':'updated with the same date','session':self.session,'tempe':tempe,'heart':heart,'blood':blood,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','bloodpressure.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    blood=BloodPressure.all().filter('user', uservalue)
                    bp1=self.request.get('bldprs1')
                    bp2=self.request.get('bldprs2')
                    colDate=self.request.get('cdate')
                    bpGoal=self.request.get('bpgoal')
                    bpupdate=BloodPressure(bloodPressure1=bp1,bloodPressure2=bp2,bpGoal=bpGoal,bpNote='',collectionDate=colDate,user=self.session['username'])
                    bpupdate.put()
                    directory = os.path.dirname(__file__)
                    heart=Heart.all().filter('user', uservalue)
                    tempe=Temperature.all().filter('user', uservalue)
                    blood=BloodPressure.all().filter('user', uservalue)
                    template_values = {'bpmsg':'added with the same date','session':self.session,'tempe':tempe,'heart':heart,'blood':blood,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','bloodpressure.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                blood=BloodPressure.all().filter('user', uservalue)
                template_values = {'bpmsg':'Please enter all details','session':self.session,'blood':blood}
                path = os.path.join(directory, os.path.join('templates','bloodpressure.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
                
               


                              
class WalkingTracker(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)        
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        exercise=Exercise.all().filter('user', uservalue)
        walking=Walking.all().filter('user', uservalue)
        swim=Swim.all().filter('user', uservalue)
        cycle=Cycling.all().filter('user', uservalue)
        template_values = {'msg':'','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','walking.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','walking.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            walkingDist=self.request.get('wdst')
            walkingDistGoal=self.request.get('wdgoal')
            walkngTime=self.request.get('walktme')
            wlkdate=self.request.get('wlkdate')
            wtGoal=self.request.get('wtgoal')
            walkingNote=self.request.get('wlknote')
            if walkingDist and wlkdate:
                walking1=Walking.all().filter('user', uservalue).filter('collectionDate', wlkdate).fetch(1)
                walking=Walking.all().filter('user', uservalue)
                if walking1:
                    for a in walking1:
                        a.walkingDist=self.request.get('wdst')
                        a.walkingDistGoal=self.request.get('wdgoal')
                        a.walkingTime=self.request.get('walktme')
                        a.walkingTimeGoal=self.request.get('wtgoal')
                        a.walkingNote=self.request.get('wlknote')
                        a.put()
                    directory = os.path.dirname(__file__)
                    exercise=Exercise.all().filter('user', uservalue)
                    walking=Walking.all().filter('user', uservalue)
                    swim=Swim.all().filter('user', uservalue)
                    cycle=Cycling.all().filter('user', uservalue)
                    template_values = {'msg':'','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','walking.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    walking=Walking.all().filter('user', uservalue)
                    wlkupdate=Walking(walkingDist=walkingDist,walkingDistGoal=walkingDistGoal,walkingTime=walkngTime,walkingTimeGoal=wtGoal,walkingNote=walkingNote,collectionDate=wlkdate,user=self.session['username'])
                    wlkupdate.put()
                    directory = os.path.dirname(__file__)
                    exercise=Exercise.all().filter('user', uservalue)
                    walking=Walking.all().filter('user', uservalue)
                    swim=Swim.all().filter('user', uservalue)
                    cycle=Cycling.all().filter('user', uservalue)
                    template_values = {'wmsg':'added with new date','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','walking.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                walking=Walking.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'wmsg':'Please enter the date','session':self.session,'walking':walking}
                path = os.path.join(directory, os.path.join('templates','walking.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
  
        

    
       
class SugarTracker(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)         
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        sugar=Sugar.all().filter('user', uservalue)
        template_values = {'msg':' ','sugar':sugar,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','bloodsugar.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','bloodsugar.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            sugarLevel=self.request.get('slevel')
            sugarLevelGoal=self.request.get('sugoal')
            sdate=self.request.get('sdate')
            if sugarLevel and sugarLevelGoal:
                sugar1=Sugar.all().filter('user', uservalue).filter('collectionDate', sdate).fetch(1)
                sugar=Sugar.all().filter('user', uservalue)
                if sugar1:
                    for a in sugar1:
                        a.sugarLevel=self.request.get('slevel')
                        a.sugarLevelGoal=self.request.get('sugoal')
                        a.put()
                    sugar=Sugar.all().filter('user', uservalue)
                    directory = os.path.dirname(__file__)
                    template_values = {'bsmsg':'updated with the same date','session':self.session,'sugar':sugar,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','bloodsugar.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    sugar=Sugar.all().filter('user', uservalue)
                    sugarupdate=Sugar(sugarLevel=sugarLevel,sugarLevelGoal=sugarLevelGoal,collectionDate=sdate,user=self.session['username'])
                    sugarupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'bsmsg':'added with new date','sugar':sugar,'session':self.session,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','bloodsugar.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                sugar=Sugar.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'bsmsg':'Please enter all details','session':self.session,'sugar':sugar,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','bloodsugar.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
         
class HoursSlept(webapp.RequestHandler):
    def get(self): 
        self.session = Session()  
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        sleep=Sleep.all().filter('user', uservalue)
        template_values = {'msg':' ','sleep':sleep,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','sleep.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','sleep.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            sleepTime=self.request.get('slptme')
            sleepTimeGoal=self.request.get('sltmegoal')
            sldate=self.request.get('sldate')
            if sleepTime and sleepTimeGoal:
                sleep1=Sleep.all().filter('user', uservalue).filter('collectionDate', sldate).fetch(1)
                sleep=Sleep.all().filter('user', uservalue)
                if sleep1:
                    for a in sleep1:
                        a.sleepTime=self.request.get('slptme')
                        a.sleepTimeGoal=self.request.get('sltmegoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'hsmsg':'updated with the same date','session':self.session,'sleep':sleep,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','sleep.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    sleep=Sleep.all().filter('user', uservalue)
                    slpupdate=Sleep(sleepTime=sleepTime,sleepTimeGoal=sleepTimeGoal,collectionDate=sldate,user=self.session['username'])
                    slpupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'hsmsg':'added with new date','sleep':sleep,'session':self.session,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','sleep.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                sleep=Sleep.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'hsmsg':'Please enter the date','session':self.session,'sleep':sleep,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','sleep.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class BodyTemperature(webapp.RequestHandler):
    def get(self): 
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)   
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        tempe=Temperature.all().filter('user', uservalue)
        template_values = {'msg':' ','tempe':tempe,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','bodytemperature.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','bodytemperature.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            temperature=self.request.get('ptemp')
            temperatureGoal=self.request.get('tempgoal')
            btempdate=self.request.get('btempdate')
            if temperature :
                tempe1=Temperature.all().filter('user', uservalue).filter('collectionDate', btempdate).fetch(1)
                tempe=Temperature.all().filter('user', uservalue)
                if tempe1:
                    for a in tempe1:
                        a.temperature=self.request.get('ptemp')
                        a.temperatureGoal=self.request.get('tempgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    heart=Heart.all().filter('user', uservalue)
                    tempe=Temperature.all().filter('user', uservalue)
                    blood=BloodPressure.all().filter('user', uservalue)
                    template_values = {'btmsg':'updated with the same date','tempe':tempe,'heart':heart,'blood':blood,'hits':pagehits,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','bodytemperature.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    if btempdate:
                        tempe=Temperature.all().filter('user', uservalue)
                        btupdate=Temperature(temperature=temperature,temperatureGoal=temperatureGoal,collectionDate=btempdate,user=self.session['username'])
                        btupdate.put()
                        directory = os.path.dirname(__file__)
                        tempe=Temperature.all().filter('user', uservalue)
                        template_values = {'btmsg':'added with the new date','tempe':tempe,'hits':pagehits,'session':self.session}
                        path = os.path.join(directory, os.path.join('templates','bodytemperature.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                    else:
                        tempe=Temperature.all().filter('user', uservalue)
                        directory = os.path.dirname(__file__)
                        template_values = {'btmsgLog':'Please enter all details','session':self.session,'tempe':tempe}
                        path = os.path.join(directory, os.path.join('templates','bodytemperature.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))                

class HeartRate(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        heart=Heart.all().filter('user', uservalue)
        tempe=Temperature.all().filter('user', uservalue)
        blood=BloodPressure.all().filter('user', uservalue)
        template_values = {'msg':' ','tempe':tempe,'heart':heart,'blood':blood,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','heartrate.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','heartrate.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            heartRate=self.request.get('phr')
            heartRateGoal=self.request.get('hrtgoal')
            hrdate=self.request.get('hrdate')
            if heartRate :
                heart1=Heart.all().filter('user', uservalue).filter('collectionDate', hrdate).fetch(1)
                heart=Heart.all().filter('user', uservalue)
                if heart1:
                    for a in heart1:
                        a.heartRate=self.request.get('phr')
                        a.heartRateGoal=self.request.get('hrtgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    heart=Heart.all().filter('user', uservalue)
                    tempe=Temperature.all().filter('user', uservalue)
                    blood=BloodPressure.all().filter('user', uservalue)
                    template_values = {'hrmsg':'updated with the same date','session':self.session,'tempe':tempe,'heart':heart,'blood':blood,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','heartrate.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    if hrdate:
                        heart=Heart.all().filter('user', uservalue)
                        hrtupdate=Heart(heartRate=heartRate,heartRateGoal=heartRateGoal,collectionDate=hrdate,user=self.session['username'])
                        hrtupdate.put()
                        directory = os.path.dirname(__file__)
                        heart=Heart.all().filter('user', uservalue)
                        tempe=Temperature.all().filter('user', uservalue)
                        blood=BloodPressure.all().filter('user', uservalue)
                        template_values = {'hrmsg':'added with new date','heart':heart,'session':self.session,'hits':pagehits}
                        path = os.path.join(directory, os.path.join('templates','heartrate.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                    else:
                        heart=Heart.all().filter('user', uservalue)
                        directory = os.path.dirname(__file__)
                        template_values = {'hrmsg':'Please enter all details','session':self.session,'heart':heart,'hits':pagehits}
                        path = os.path.join(directory, os.path.join('templates','heartrate.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG)) 

class Profile(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        directory = os.path.dirname(__file__)
        if not user:
                template_values = {'msgLog':'Login Required','hits':pagehits}
                directory = os.path.dirname(__file__)
                path = os.path.join(directory, os.path.join('templates','homepage.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG)) 
        else:
                userdata=UserProfile.all().filter('email =',user)
                template_values = {'msg':'','userdata':userdata,'session':self.session,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','profile.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        userdata=UserProfile.all().filter('email',user)
        for a in userdata:
            if self.request.get('fname'):
                    a.firstName = self.request.get('fname')
            else:
                a.firstName=a.firstName
            if self.request.get('lname'):
                    a.lastName = self.request.get('lname')
            else:
                a.lastName=a.lastName
            a.email=user
            if self.request.get('phone'):
                    a.phone = self.request.get('phone')
            else:
                a.phone=a.phone
            if self.request.get('gender'):
                    a.gender = self.request.get('gender')
            else:
                a.gender=a.gender
            if self.request.get('Marital'):
                    a.maritalStatus = self.request.get('Marital')
            else:
                a.maritalStatus=a.maritalStatus
            if self.request.get('pcode'):
                    a.pincode = self.request.get('pcode')
            else:
                a.pincode=a.pincode
            if self.request.get('bloodgroup'):
                    a.bloodGroup = self.request.get('bloodgroup')
            else:
                a.bloodGroup=a.bloodGroup
            if self.request.get('birth_day'):
                    a.birthDay = self.request.get('birth_day')
            else:
                a.birthDay=a.birthDay
            if self.request.get('birth_month'):
                    a.birthMonth = self.request.get('birth_month')
            else:
                a.birthMonth=a.birthMonth
            if self.request.get('birth_year'):
                    a.birthYear = self.request.get('birth_year')
            else:
                a.birthYear=a.birthYear
            if self.request.get('location'):
                    a.address = self.request.get('location')
            else:
                a.address=a.address
            if self.request.get('pword') and self.request.get('cpword') and self.request.get('pword')==self.request.get('cpword'):
                    a.password = self.request.get('pword')
            else:
                a.password=a.password
            a.put()
            directory = os.path.dirname(__file__)
            userdataN=UserProfile.all().filter('email',user)
            template_values = {'userdata':userdataN,'session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','profile.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG)) 

class SignUp(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)   
        directory = os.path.dirname(__file__)
        template_values = {'msg':'','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','signup.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)   
        fn=self.request.get('fname')
        ln=self.request.get('lname')
        email=self.request.get('email')
        pw=self.request.get('pword')
        cpw=self.request.get('cpword')
        birth_day=self.request.get('birth_day')
        birth_month=self.request.get('birth_month')
        birth_year=self.request.get('birth_year')
        gender=self.request.get('gender')
        location=self.request.get('location')
        phone=self.request.get('phone')
        pincode=self.request.get('pcode')
        if pw == '' or email == '' or cpw == '' or fn == '' or ln == '':
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Please fill in all mandatory fields','fn':fn,'ln':ln,'email':email,'gender':gender,'birth_day':birth_day,'birth_month':birth_month,'birth_year':birth_year,'location':location,'phone':phone,'pincode':pincode,'location':location,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','signup.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:

            if len(email) > 7 and re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                if pw != cpw:

                    directory = os.path.dirname(__file__)

                    template_values = {'msg':'Email already in use','fn':fn,'ln':ln,'email':email,'birth_day':birth_day,'birth_month':birth_month,'birth_year':birth_year,'gender':gender,'location':location,'phone':phone,'hits':pagehits}

                    template_values = {'msg':'Password not Matched','fn':fn,'ln':ln,'email':email,'gender':gender,'birth_day':birth_day,'birth_month':birth_month,'birth_year':birth_year,'location':location,'phone':phone}

                    path = os.path.join(directory, os.path.join('templates','signup.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    que = db.Query(UserProfile).filter('email =',email)
                    results = que.fetch(limit=10)
                    if len(results) > 0 :
                        directory = os.path.dirname(__file__)
                        template_values = {'msg':'Email already in use','fn':fn,'ln':ln,'email':email,'birth_day':birth_day,'birth_month':birth_month,'birth_year':birth_year,'gender':gender,'location':location,'phone':phone}
                        path = os.path.join(directory, os.path.join('templates','signup.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                    else:
                        user=UserProfile(firstName =fn,lastName=ln,email=email,password= base64.b64encode(pw),gender=gender,birthDay=birth_day,birthMonth=birth_month,birthYear=birth_year,city=location,phone=phone,userType='user')
                        user.put()
                        logging.info('Adding account='+email)
                        insquery = db.Query(UserProfile).filter('email =',email)
                        insresults = insquery.fetch(limit=1)
                        if len(insresults) > 0 :
                            directory = os.path.dirname(__file__)
                            template_values = {'msgaccount':'Account Created'}
                            path = os.path.join(directory, os.path.join('templates','homepage.html'))
                            self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Invalid Email','fn':fn,'ln':ln,'email':email,'gender':gender,'birth_day':birth_day,'birth_month':birth_month,'birth_year':birth_year,'location':location,'phone':phone}
                path = os.path.join(directory, os.path.join('templates','signup.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
                        
class DoctorSignup(webapp.RequestHandler):
    def get(self):    
        directory = os.path.dirname(__file__)
        template_values = {'msg':''}
        path = os.path.join(directory, os.path.join('templates','signup.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        fn=self.request.get('firstname')
        ln=self.request.get('lastname')
        if self.request.get('specialization1')=="others":
            specialization=self.request.get('specialization2')
        else:
            specialization=self.request.get('specialization1')
        hospital=self.request.get('hospital')
        location=self.request.get('location')
        phone=self.request.get('phone')
        email=self.request.get('doctoremail')
        pw=self.request.get('password')
        cpw=self.request.get('repwd')
        if fn == '' or ln == '' or pw == '' or email == '' or cpw == '' or phone == '' or specialization=='':
            directory = os.path.dirname(__file__)
            template_values = {'msg1':'Please fill in all mandatory fields','fn':fn,'ln':ln,'email':email,'error':'doctor','phone':phone,'location':location,'hospital':hospital}
            path = os.path.join(directory, os.path.join('templates','signup.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            if len(email) > 7 and re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                if pw != cpw:
                    directory = os.path.dirname(__file__)
                    template_values = {'msg1':'Password not Matched','fn':fn,'ln':ln,'email':email,'phone':phone,'location':location,'hospital':hospital}
                    path = os.path.join(directory, os.path.join('templates','signup.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    que = db.Query(DoctorProfile).filter('email =',email)
                    results = que.fetch(limit=10)
                    if len(results) > 0 :
                        directory = os.path.dirname(__file__)
                        template_values = {'msg1':'Email already in use','fn':fn,'ln':ln,'email':email,'phone':phone,'location':location,'hospital':hospital}
                        path = os.path.join(directory, os.path.join('templates','signup.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                    else:
                        user=DoctorProfile(firstName =fn,lastName=ln,email=email,password= base64.b64encode(pw),userType='doctor',specialization=specialization,hospital=hospital,city=location,phone=phone)
                        user.put()
                        logging.info('Adding account='+email)
                        insquery = db.Query(DoctorProfile).filter('email =',email)
                        insresults = insquery.fetch(limit=1)
                        if len(insresults) > 0 :
                            directory = os.path.dirname(__file__)
                            template_values = {'msgaccount':'Account Created'}
                            path = os.path.join(directory, os.path.join('templates','homepage.html'))
                            self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                template_values = {'msg1':'Invalid Email','fn':fn,'ln':ln,'phone':phone,'location':location,'hospital':hospital}
                path = os.path.join(directory, os.path.join('templates','signup.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class HospitalSignup(webapp.RequestHandler):
    def get(self):    
        directory = os.path.dirname(__file__)
        template_values = {'msg':''}
        path = os.path.join(directory, os.path.join('templates','signup.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        hospname=self.request.get('hospname')
        fax=self.request.get('fax')
        website=self.request.get('website')
        specialization1=self.request.get('specialization1')
        if specialization1=='choose':
            specialization=self.request.get('specialization2')
        else:
            specialization=self.request.get('specialization1')
        hospital=self.request.get('hospital')
        location=self.request.get('location')
        phone=self.request.get('phone')
        email=self.request.get('doctoremail')
        pw=self.request.get('password')
        cpw=self.request.get('repwd')
        if hospname == '' or pw == '' or email == '' or cpw == '' or location =='' :
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Please fill all fields','hospname':hospname,'email':email}
            path = os.path.join(directory, os.path.join('templates','signup.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            if pw != cpw:
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Password not Matched','hospname':hospname,'email':email}
                path = os.path.join(directory, os.path.join('templates','signup.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                que = db.Query(UserProfile).filter('email =',email)
                results = que.fetch(limit=10)
                if len(results) > 0 :
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'Email already in use','email':email}
                    path = os.path.join(directory, os.path.join('templates','signup.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    user=Hospital(hospitalName=hospname,fax=fax,email=email,password= base64.b64encode(pw),userType='doctor',specialization=specialization,hospital=hospital,address=location,phone=phone,website=website)
                    user.put()
                    logging.info('Adding account='+email)
                    insquery = db.Query(Hospital).filter('email =',email)
                    insresults = insquery.fetch(limit=1)
                    if len(insresults) > 0 :
                        directory = os.path.dirname(__file__)
                        template_values = {'msg':'Account Created'}
                        path = os.path.join(directory, os.path.join('templates','signup.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                        
class SignIn(webapp.RequestHandler):
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        lm=self.request.get('email')
        pwd=self.request.get('pwd')
        logging.info("Checking account="+lm+" pw="+pwd)
        self.session.delete_item('username')
        if lm == '' or pwd == '':
            directory = os.path.dirname(__file__)
            template_values = {'msgLoginall':'Please fill in all fields'}
            path = os.path.join(directory, os.path.join('templates','homepage.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            adminque = db.Query(UserProfile).filter('email =',lm).filter("password = ",base64.b64encode(pwd))
            results = adminque.fetch(limit=1)
            if len(results) > 0 :
                self.session['username'] = lm
                self.session['name'] = results[0].firstName 
                global user
                wellness=Wellness.all().filter('user',self.session['username'])
                directory = os.path.dirname(__file__)
                template_values = {'msgLogin':'','session':self.session,'wellness':wellness,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','homepage.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                template_values = {'msgLogindetails':'Invalid details','hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','homepage.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class SignOut(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)   
        self.session.delete_item('username')
        self.session.delete_item('name')
        self.session.delete_item('type')
        directory = os.path.dirname(__file__)
        template_values = {'msgLogin':'Invalid details','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','homepage.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class PhysicalActivity(webapp.RequestHandler):
    def get(self):        
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)      
        uservalue=self.session['username']     
        exercise=Exercise.all().filter('user', uservalue)
        walking=Walking.all().filter('user', uservalue)
        swim=Swim.all().filter('user', uservalue)
        cycle=Cycling.all().filter('user', uservalue)
        template_values = {'msg':'','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, os.path.join('templates','physicalactivity.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        

                    
class WeightBmi(webapp.RequestHandler):
    def get(self): 
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)      
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness,'session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','weightbmi.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        pagehits=hit.fetch(1)
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','weightbmi.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            bmiDate=self.request.get('bmidate')
            bmiWeight=self.request.get('wt')
            bmiHeight=self.request.get('ht')
            bmi=self.request.get('bmi')
            if bmiDate and bmiWeight and bmi and bmiHeight:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', bmiDate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.weight=self.request.get('wt')
                        a.height=self.request.get('ht')
                        a.bmi=self.request.get('bmi')
                        a.bmiGoal=self.request.get('bmigoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'bmimsg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','weightbmi.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    bmiWeight=self.request.get('wt')
                    bmiHeight=self.request.get('ht')
                    bmi=self.request.get('bmi')
                    bmiGoal=self.request.get('bmigoal')
                    bmiupdate=Wellness(weight=bmiWeight,height=bmiHeight,bmi=bmi,bmiGoal=bmiGoal,bmiNote='',collectionDate=bmiDate,user=self.session['username'])
                    bmiupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'bmimsg':'Added with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','weightbmi.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                wellness=Wellness.all().filter('user', uservalue)
                template_values = {'bmimsg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','weightbmi.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))        

class Nutrition(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','homepage.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Skin(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','skin.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class MakeUp(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','makeup.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   
        
class Hair(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','hair.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   
        
class EyeCare(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','eyecare.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))    
        
class ManiCure(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','manicure.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))    
        
class PediCure(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','pedicure.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))      
        
class LipCare(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','lipcare.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Fitness(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','fitness.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))     
        
class HomePage(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','homepage.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))                                           
        

class VitalSigns(webapp.RequestHandler):
    def get(self):        
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)         
        uservalue=self.session['username']
        heart=Heart.all().filter('user', uservalue)
        tempe=Temperature.all().filter('user', uservalue)
        blood=BloodPressure.all().filter('user', uservalue)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'tempe':tempe,'heart':heart,'blood':blood,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','vitalsigns.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class KeyBloodTest(webapp.RequestHandler):
    def get(self):        
        self.session = Session() 
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)         
        user=self.session['username']
        wellness=Wellness.all().filter('user', user)
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'wellness':wellness,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','keybloodtest.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))       
             
class UploadRecord(webapp.RequestHandler):
    def get(self):
        self.session = Session() 
        hit=Counter.all()
        pagehits=hit.fetch(1)        
        upload_url = blobstore.create_upload_url('/upload')
        #self.response.out.write('<html><body>')
        #self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
        #self.response.out.write("""Upload Record: <input type="file" name="file"><br> <input type="submit" name="submit" value="Submit"> </form></body></html>""")
        directory = os.path.dirname(__file__)
        blob_data=blobstore.BlobInfo.all()
        template_values = {'blob':blob_data,'upload_url':upload_url,'session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','uploadrecord.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        #self.response.out.write('Your Files:')
        #for b in blobstore.BlobInfo.all():
        #    self.response.out.write('<li><a href="/serve/%s' % str(b.key()) + '">' + str(b.filename) + '</a>'+'('+str(b.creation)+')')    
class DeleteRecord(webapp.RequestHandler):
    def get(self):
        self.session = Session()        
        upload_url = blobstore.create_upload_url('/upload')
        key=self.request.get('key')
        if not blobstore.get(key):
            self.error(404)
        else:
            blobstore.delete(key)
        directory = os.path.dirname(__file__)
        blob_data=blobstore.BlobInfo.all()
        template_values = {'blob':blob_data,'upload_url':upload_url,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','uploadrecord.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG)) 
       
class MedicalContacts(webapp.RequestHandler):
    def get(self):
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session}
        path = os.path.join(directory, os.path.join('templates','medicalcontacts.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class FixAppointement(webapp.RequestHandler):
    def get(self):
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session}
        path = os.path.join(directory, os.path.join('templates','fixappointment.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Womendiet(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','womendiet.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Housekeeping(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','housekeeping.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Menopause(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','menopause.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Menstrualcycle(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','menstrualcycle.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Exerciseminutes(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)          
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        exercise=Exercise.all().filter('user', uservalue)
        #walking=Walking.all().filter('user', uservalue)
        #swim=Swim.all().filter('user', uservalue)
        #cycle=Cycling.all().filter('user', uservalue)
        template_values = {'msg':'','exercise':exercise,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','exercise.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','exercise.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            wrktme=self.request.get('wrktme')
            exrcsegoal=self.request.get('exrcsegoal')
            exdate=self.request.get('exdate')
            exerciseNote=self.request.get('exnote')
            if wrktme and exdate:
                exercise1=Exercise.all().filter('user', uservalue).filter('collectionDate', exdate).fetch(1)
                exercise=Exercise.all().filter('user', uservalue)
                if exercise1:
                    for a in exercise1:
                        a.exerciseTime=self.request.get('wrktme')
                        a.exerciseGoal=self.request.get('exrcsegoal')
                        a.collectionDate=a.collectionDate
                        a.exerciseNote=self.request.get('exnote')
                        a.user=uservalue
                        a.put()
                    directory = os.path.dirname(__file__)
                    exercise=Exercise.all().filter('user', uservalue)
                    #walking=Walking.all().filter('user', uservalue)
                    #swim=Swim.all().filter('user', uservalue)
                    #cycle=Cycling.all().filter('user', uservalue)
                    template_values = {'emsg':'updated with the same date','exercise':exercise,'hits':pagehits,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','exercise.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    exercise=Exercise.all().filter('user', uservalue)
                    exupdate=Exercise(exerciseTime=wrktme,exerciseGoal=exrcsegoal,exerciseNote=exerciseNote,collectionDate=exdate,user=self.session['username'])
                    exupdate.put()
                    directory = os.path.dirname(__file__)
                    exercise=Exercise.all().filter('user', uservalue)
                    template_values = {'emsg':'added with the new date','exercise':exercise,'hits':pagehits,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','exercise.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                exercise=Exercise.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'emsg':'Please enter the date','session':self.session,'exercise':exercise,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','exercise.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

#    def get(self):
#        self.session = Session()        
#        directory = os.path.dirname(__file__)
#        template_values = {'msg':' ','session':self.session}
#        path = os.path.join(directory, os.path.join('templates','exercise.html'))
#       self.response.out.write(template.render(path,template_values, _DEBUG))        

class Premenstrualsyndrome(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','premenstrualsyndrome.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Thyroidproblems(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','thyroidproblems.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Breastcancer(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','breastcancer.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Walkingexercise(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','walking.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Swimmingexercise(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)          
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        exercise=Exercise.all().filter('user', uservalue)
        walking=Walking.all().filter('user', uservalue)
        swim=Swim.all().filter('user', uservalue)
        cycle=Cycling.all().filter('user', uservalue)
        template_values = {'msg':'','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','swimming.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
            self.session = Session()
            hit=Counter.all()
            for hi in hit:
                    hi.counter+=1
                    hi.put()        
            pagehits=hit.fetch(1)  
            uservalue=self.session['username']
            if not self.session['username']:
                directory = os.path.dirname(__file__)
                template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','swimming.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                swimDist=self.request.get('swimdst')
                swimDistGoal=self.request.get('swimgoal')
                swimTime=self.request.get('swimtme')
                swimTimeGoal=self.request.get('swimtmegoal')
                swmdate=self.request.get('swmdate')
                if swimDist and swimTime:
                    swim1=Swim.all().filter('user', uservalue).filter('collectionDate', swmdate).fetch(1)
                    swim=Swim.all().filter('user', uservalue)
                    if swim1:
                        for a in swim1:
                            a.swimDist=self.request.get('swimdst')
                            a.swimDistGoal=self.request.get('swimgoal')
                            a.swimTime=self.request.get('swimtme')
                            a.swimTimeGoal=self.request.get('swimtmegoal')
                            a.put()
                        directory = os.path.dirname(__file__)
                        exercise=Exercise.all().filter('user', uservalue)
                        walking=Walking.all().filter('user', uservalue)
                        swim=Swim.all().filter('user', uservalue)
                        cycle=Cycling.all().filter('user', uservalue)
                        template_values = {'smsg':'updated with the same date','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
                        path = os.path.join(directory, os.path.join('templates','swimming.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                    else:
                        swim=Swim.all().filter('user', uservalue)
                        swmupdate=Swim(swimDist=swimDist,swimDistGoal=swimDistGoal,swimTime=swimTime,swimTimeGoal=swimTimeGoal,collectionDate=swmdate,user=self.session['username'])
                        swmupdate.put()
                        directory = os.path.dirname(__file__)
                        exercise=Exercise.all().filter('user', uservalue)
                        walking=Walking.all().filter('user', uservalue)
                        swim=Swim.all().filter('user', uservalue)
                        cycle=Cycling.all().filter('user', uservalue)
                        template_values = {'cmsg':'added with new date','session':self.session,'cycle':cycle,'exercise':exercise,'walking':walking,'swim':swim,'hits':pagehits}
                        path = os.path.join(directory, os.path.join('templates','swimming.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    directory = os.path.dirname(__file__)
                    swim=Swim.all().filter('user', uservalue)
                    template_values = {'smsg':'Please enter the date','session':self.session,'swim':swim,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','swimming.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
        
 
 
class Cyclingexercise(webapp.RequestHandler):
    def get(self): 
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)        
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        exercise=Exercise.all().filter('user', uservalue)
        walking=Walking.all().filter('user', uservalue)
        swim=Swim.all().filter('user', uservalue)
        cycle=Cycling.all().filter('user', uservalue)
        template_values = {'msg':'','cycle':cycle,'exercise':exercise,'swim':swim,'walking':walking,'hits':pagehits,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','cycling.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msgLog':'Login Required','session':self.session,'hits':pagehits}
            path = os.path.join(directory, os.path.join('templates','cycling.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            cyclingDist=self.request.get('cdstnce')
            cyclingtGoal=self.request.get('cdgoal')
            cyclingTime=self.request.get('ct')
            cyclingTimeGoal=self.request.get('ctgoal')
            cycdate=self.request.get('cycdate')
            if cyclingDist and cyclingTime:
                cycle1=Cycling.all().filter('user', uservalue).filter('collectionDate', cycdate).fetch(1)
                cycle=Cycling.all().filter('user', uservalue)
                if cycle1:
                    for a in cycle1:
                        a.cyclingDist=self.request.get('cdstnce')
                        a.cyclingtGoal=self.request.get('cdgoal')
                        a.cyclingTime=self.request.get('ct')
                        a.cyclingTimeGoal=self.request.get('ctgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    exercise=Exercise.all().filter('user', uservalue)
                    walking=Walking.all().filter('user', uservalue)
                    swim=Swim.all().filter('user', uservalue)
                    cycle=Cycling.all().filter('user', uservalue)
                    template_values = {'cmsg':'updated with the same date','session':self.session,'cycle':cycle,'exercise':exercise,'walking':walking,'swim':swim,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','cycling.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    cycle=Cycling.all().filter('user', uservalue)
                    cycpupdate=Cycling(cyclingDist=cyclingDist,cyclingtGoal=cyclingtGoal,cyclingTime=cyclingTime,cyclingTimeGoal=cyclingTimeGoal,collectionDate=cycdate,user=self.session['username'])
                    cycpupdate.put()
                    directory = os.path.dirname(__file__)
                    exercise=Exercise.all().filter('user', uservalue)
                    walking=Walking.all().filter('user', uservalue)
                    swim=Swim.all().filter('user', uservalue)
                    cycle=Cycling.all().filter('user', uservalue)
                    template_values = {'cmsg':'added with new date','session':self.session,'cycle':cycle,'exercise':exercise,'walking':walking,'swim':swim,'hits':pagehits}
                    path = os.path.join(directory, os.path.join('templates','cycling.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                cycle=Cycling.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'cmsg':'Please enter the date','session':self.session,'cycle':cycle,'hits':pagehits}
                path = os.path.join(directory, os.path.join('templates','cycling.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class Healthyfood(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','healthyfood.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Fruits(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','fruits.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Water(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','water.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Infants(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','infants.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class Toddlers(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','toddlers.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class ToddlersTwo(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','toddlers2.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class MenNutrition(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','mennutrition.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class HeartDisease(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','heartdisease.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))       
        
class HeatStroke(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','heatstroke.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))         
        
class Dengue(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','dengue.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))           

class BellyFat(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','bellyfat.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))           
        
class Malaria(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','malaria.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))           

class QuitSmoking(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','quit.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   

class PreSchoolers(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','preschoolers.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   

class MidChild(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','midchildhood.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   

class MidChildOne(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','midchildone.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   

class ChildTwo(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','midchildtwo.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))   
        
class MiddleAdolescence(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','middleadolescence.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG)) 

class ChildhoodVaccination(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','childhoodvaccination.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG)) 

class Pregnancy(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        hit=Counter.all()
        for hi in hit:
                hi.counter+=1
                hi.put()        
        pagehits=hit.fetch(1)  
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':' ','session':self.session,'hits':pagehits}
        path = os.path.join(directory, os.path.join('templates','pregnant.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG)) 
        
class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        blob_key =self.request.get('key')
        if not blobstore.get(blob_key):
            self.error(404)
        else:
            self.send_blob(blobstore.BlobInfo.get(blob_key), save_as=True)


application = webapp.WSGIApplication([('/nutrition', Nutrition),('/breastcancer',Breastcancer),('/womendiet',Womendiet),('/thyroidproblems',Thyroidproblems),('/premenstrual',Premenstrualsyndrome),('/menstrualcycle',Menstrualcycle),('/housekeeping',Housekeeping),('/menopause',Menopause),('/hospitalsignup',HospitalSignup),('/doctorsignup', DoctorSignup),('/myprofile', Profile),('/vitalsigns', VitalSigns),('/keybloodtest', KeyBloodTest),('/signup', SignUp),('/signin', SignIn),('/signout', SignOut),('/uploadrecord',UploadRecord ),('/delete',DeleteRecord ),('/serve', ServeHandler),('/physicalactivity', PhysicalActivity),('/weightbmi', WeightBmi),('/medicalcontacts', MedicalContacts),('/fixappointment', FixAppointement),('/walking', WalkingTracker),('/sleep', HoursSlept),('/bodytemp', BodyTemperature),('/heartrate', HeartRate),('/skin',Skin),('/makeup',MakeUp),('/hair',Hair),('/eyecare',EyeCare),('/manicure',ManiCure),('/pedicure',PediCure),('/lipcare',LipCare),('/fitness',Fitness),('/',HomePage),('/fitexercise',Exerciseminutes),('/fitwalking',Walkingexercise),('/fitswimming',Swimmingexercise),('/fitcycling',Cyclingexercise),('/healthyfood',Healthyfood),('/fruits',Fruits),('/water',Water),('/bp',BPHandler),('/heartrate',HeartRate),('/bloodsugar',SugarTracker),('/infant',Infants),('/toddlers',Toddlers),('/toddlers2',ToddlersTwo),('/mennutrition',MenNutrition),('/heartdisease',HeartDisease),('/heatstroke',HeatStroke),('/dengue',Dengue),('/malaria',Malaria),('/bellyfat',BellyFat),('/quit',QuitSmoking),('/preschoolers',PreSchoolers),('/midchild',MidChild),('/childone',MidChildOne),('/childtwo',ChildTwo),('/middleadolescence',MiddleAdolescence),('/childhoodvaccination',ChildhoodVaccination),('/pregnancy',Pregnancy)], debug=True)


def main():
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()


