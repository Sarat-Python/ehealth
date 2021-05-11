from google.appengine.ext import blobstore, db, webapp, webapp
from google.appengine.ext.webapp import blobstore_handlers, template
from google.appengine.ext.webapp.util import run_wsgi_app
from util.sessions import Session
import base64
import logging
import os
import wsgiref.handlers
#from google.appengine.ext.webapp import util
_DEBUG = True

class UserProfile(db.Model):                        
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
    phone=db.PhoneNumberProperty()
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
    phone=db.PhoneNumberProperty()
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
    
    bloodPressure1=db.StringProperty()  
    bloodPressure2=db.StringProperty()
    bpGoal=db.StringProperty()
    bpNote=db.StringProperty()
    
    exerciseTime=db.StringProperty()
    exerciseGoal=db.StringProperty()
    exerciseNote=db.StringProperty()  
    
    walkingDist=db.StringProperty()
    walkingDistGoal=db.StringProperty()
    walkingTime=db.StringProperty()
    walkingTimeGoal=db.StringProperty()
    walkingNote=db.StringProperty()
    
    swimDist=db.StringProperty()
    swimDistGoal=db.StringProperty()
    swimTime=db.StringProperty()
    swimTimeGoal=db.StringProperty()
    swimNote=db.StringProperty()

    
    sugarLevel=db.StringProperty()
    sugarLevelGoal=db.StringProperty()
    sugarLevelNote=db.StringProperty()
    
    sleepTime=db.StringProperty()
    sleepTimeGoal=db.StringProperty()
    sleepTimeNote=db.StringProperty()
    
    cyclingDist=db.StringProperty()
    cyclingtGoal=db.StringProperty()
    cyclingTime=db.StringProperty()
    cyclingTimeGoal=db.StringProperty()
    cyclingNote=db.StringProperty()
    
    temperature=db.StringProperty()
    temperatureGoal=db.StringProperty()
    temperatureNote=db.StringProperty()
    
    heartRate=db.StringProperty()
    heartRateGoal=db.StringProperty()
    heartRateNote=db.StringProperty()
    
    newField1=db.StringProperty()
    newField2=db.StringProperty()
    newField3=db.StringProperty()
    
class MyFile(db.Model): 
    filedata = db.BlobProperty()

class Ehealth(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
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
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
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
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                wellness=Wellness.all().filter('user', uservalue)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
            
class BloodPressure(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            bp1=self.request.get('bldprs1')
            bp2=self.request.get('bldprs2')
            colDate=self.request.get('cdate')
            bpGoal=self.request.get('bpgoal')
            if bp1 and bp2 and bpGoal and colDate:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', colDate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.bloodPressure1=self.request.get('bldprs1')
                        a.bloodPressure2=self.request.get('bldprs2')
                        a.bpGoal=self.request.get('bpgoal')
                        a.bpNote=''
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    bp1=self.request.get('bldprs1')
                    bp2=self.request.get('bldprs2')
                    colDate=self.request.get('cdate')
                    bpGoal=self.request.get('bpgoal')
                    bpupdate=Wellness(bloodPressure1=bp1,bloodPressure2=bp2,bpGoal=bpGoal,bpNote='',collectionDate=colDate,user=self.session['username'])
                    bpupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                wellness=Wellness.all().filter('user', uservalue)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class Excersice(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            wrktme=self.request.get('wrktme')
            exrcsegoal=self.request.get('exrcsegoal')
            exdate=self.request.get('exdate')
            if wrktme and exdate:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', exdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.exerciseTime=self.request.get('wrktme')
                        a.exerciseGoal=self.request.get('exrcsegoal')
                        a.exerciseNote=''
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    exupdate=Wellness(exerciseTime=wrktme,exerciseGoal=exrcsegoal,exerciseNote='',collectionDate=exdate,user=self.session['username'])
                    exupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
                              
class WalkingTracker(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            walkngDist=self.request.get('wd')
            walkingDistGoal=self.request.get('wdgoal')
            walkngTime=self.request.get('walktme')
            wlkdate=self.request.get('wlkdate')
            wtGoal=self.request.get('wtgoal')
            if walkngDist and wlkdate:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', wlkdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.walkingDist=self.request.get('wd')
                        a.walkingDistGoal=self.request.get('wdgoal')
                        a.walkingTime=self.request.get('walktme')
                        a.walkingTimeGoal=self.request.get('wtgoal')
                        a.walkingNote=''
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    wlkupdate=Wellness(walkingDist=walkngDist,walkingDistGoal=walkingDistGoal,walkingTime=walkngTime,walkingTimeGoal=wtGoal,walkingNote='',collectionDate=wlkdate,user=self.session['username'])
                    wlkupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
  
        
class Swimming(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            swimDist=self.request.get('swimdst')
            swimDistGoal=self.request.get('swimgoal')
            swimTime=self.request.get('swimtme')
            swimTimeGoal=self.request.get('swimtmegoal')
            swmdate=self.request.get('swmdate')
            if swimDist and swimTime:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', swmdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.swimDist=self.request.get('swimdst')
                        a.swimDistGoal=self.request.get('swimgoal')
                        a.swimTime=self.request.get('swimtme')
                        a.swimTimeGoal=self.request.get('swimtmegoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    swmupdate=Wellness(swimDist=swimDist,swimDistGoal=swimDistGoal,swimTime=swimTime,swimTimeGoal=swimTimeGoal,collectionDate=swmdate,user=self.session['username'])
                    swmupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                wellness=Wellness.all().filter('user', uservalue)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
    
       
class SugarLevel(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            sugarLevel=self.request.get('slevel')
            sugarLevelGoal=self.request.get('sgoal')
            sdate=self.request.get('sdate')
            if sugarLevel and sugarLevelGoal:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', sdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.sugarLevel=self.request.get('slevel')
                        a.sugarLevelGoal=self.request.get('sgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    sugarupdate=Wellness(sugarLevel=sugarLevel,sugarLevelGoal=sugarLevelGoal,collectionDate=sdate,user=self.session['username'])
                    sugarupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
         
class HoursSlept(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            sleepTime=self.request.get('slptme')
            sleepTimeGoal=self.request.get('sltmegoal')
            sldate=self.request.get('sldate')
            if sleepTime and sleepTimeGoal:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', sldate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.sleepTime=self.request.get('slptme')
                        a.sleepTimeGoal=self.request.get('sltmegoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    slpupdate=Wellness(sleepTime=sleepTime,sleepTimeGoal=sleepTimeGoal,collectionDate=sldate,user=self.session['username'])
                    slpupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class Cycling(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            cyclingDist=self.request.get('cdstnce')
            cyclingtGoal=self.request.get('cdgoal')
            cyclingTime=self.request.get('ct')
            cyclingTimeGoal=self.request.get('ctgoal')
            cycdate=self.request.get('cycdate')
            if cyclingDist and cyclingTime:
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', cycdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.cyclingDist=self.request.get('cdstnce')
                        a.cyclingtGoal=self.request.get('cdgoal')
                        a.cyclingTime=self.request.get('ct')
                        a.cyclingTimeGoal=self.request.get('ctgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    cycpupdate=Wellness(cyclingDist=cyclingDist,cyclingtGoal=cyclingtGoal,cyclingTime=cyclingTime,cyclingTimeGoal=cyclingTimeGoal,collectionDate=cycdate,user=self.session['username'])
                    cycpupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
                
class BodyTemperature(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            temperature=self.request.get('ptemp')
            temperatureGoal=self.request.get('tempgoal')
            btempdate=self.request.get('btempdate')
            if temperature :
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', btempdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.temperature=self.request.get('ptemp')
                        a.temperatureGoal=self.request.get('tempgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    btupdate=Wellness(temperature=temperature,temperatureGoal=temperatureGoal,collectionDate=btempdate,user=self.session['username'])
                    btupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))                

class HeartRate(webapp.RequestHandler):
    def get(self): 
        self.session = Session()       
        directory = os.path.dirname(__file__)
        uservalue=self.session['username']
        wellness=Wellness.all().filter('user', uservalue)
        template_values = {'msg':'hello','wellness':wellness}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        uservalue=self.session['username']
        if not self.session['username']:
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Login Required','session':self.session}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            heartRate=self.request.get('phr')
            heartRateGoal=self.request.get('hrtgoal')
            hrdate=self.request.get('hrdate')
            if heartRate :
                wellness1=Wellness.all().filter('user', uservalue).filter('collectionDate', hrdate).fetch(1)
                wellness=Wellness.all().filter('user', uservalue)
                if wellness1:
                    for a in wellness1:
                        a.heartRate=self.request.get('phr')
                        a.heartRateGoal=self.request.get('hrtgoal')
                        a.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'updated with the same date','session':self.session,'wellness':wellness}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    wellness=Wellness.all().filter('user', uservalue)
                    hrtupdate=Wellness(heartRate=heartRate,heartRateGoal=heartRateGoal,collectionDate=hrdate,user=self.session['username'])
                    hrtupdate.put()
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'add with new date','wellness':wellness,'session':self.session}
                    path = os.path.join(directory, os.path.join('templates','home.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                wellness=Wellness.all().filter('user', uservalue)
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Please enter the date','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG)) 

class Profile(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        user=self.session['username']
        directory = os.path.dirname(__file__)
        if not user:
                template_values = {'msg':'Login Required'}
                directory = os.path.dirname(__file__)
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG)) 
        else:
                userdata=UserProfile.all().filter('email =',user)
                template_values = {'msg':'','userdata':userdata,'session':self.session}
                path = os.path.join(directory, os.path.join('templates','profile.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        self.session = Session()
        for a in UserProfile:
            a.firstName=self.request.get('fname')
            a.lastname=self.request.get('lname')
            a.email=self.request.get('email')
            a.put()
        directory = os.path.dirname(__file__)
        template_values = {'userprofile':UserProfile,'session':self.session}
        path = os.path.join(directory, os.path.join('templates','profile.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))     

class SignUp(webapp.RequestHandler):
    def get(self):    
        directory = os.path.dirname(__file__)
        template_values = {'msg':''}
        path = os.path.join(directory, os.path.join('templates','signup.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
    def post(self):
        fn=self.request.get('fname')
        ln=self.request.get('lname')
        email=self.request.get('email')
        pw=self.request.get('pword')
        cpw=self.request.get('cpword')
        if fn == '' or ln == '' or pw == '' or email == '' or cpw == '' :
            directory = os.path.dirname(__file__)
            template_values = {'msg':'Please fill all fields','fn':fn,'ln':ln,'email':email}
            path = os.path.join(directory, os.path.join('templates','signup.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
        else:
            if pw != cpw:
                directory = os.path.dirname(__file__)
                template_values = {'msg':'Password not Matched','fn':fn,'ln':ln,'email':email}
                path = os.path.join(directory, os.path.join('templates','signup.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                que = db.Query(UserProfile).filter('email =',email)
                results = que.fetch(limit=10)
                if len(results) > 0 :
                    directory = os.path.dirname(__file__)
                    template_values = {'msg':'Email already in use','fn':fn,'ln':ln,'email':email}
                    path = os.path.join(directory, os.path.join('templates','signup.html'))
                    self.response.out.write(template.render(path,template_values, _DEBUG))
                else:
                    user=UserProfile(firstName =fn,lastName=ln,email=email,password= base64.b64encode(pw),userType='user')
                    user.put()
                    logging.info('Adding account='+email)
                    insquery = db.Query(UserProfile).filter('email =',email)
                    insresults = insquery.fetch(limit=1)
                    if len(insresults) > 0 :
                        directory = os.path.dirname(__file__)
                        template_values = {'msg':'Account Created'}
                        path = os.path.join(directory, os.path.join('templates','signup.html'))
                        self.response.out.write(template.render(path,template_values, _DEBUG))
                         
class SignIn(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        user=self.session['username']
        if not user:
            directory = os.path.dirname(__file__)
            template_values = {'msgLogin':'login required'}
            path = os.path.join(directory, os.path.join('templates','home.html'))
            self.response.out.write(template.render(path,template_values, _DEBUG))
     
    def post(self):
        self.session = Session()
        lm=self.request.get('email')
        pwd=self.request.get('pwd')
        logging.info("Checking account="+lm+" pw="+pwd)
        self.session.delete_item('username')
        if lm == '' or pwd == '':
            directory = os.path.dirname(__file__)
            template_values = {'msgLogin':'Please fill in all fields'}
            path = os.path.join(directory, os.path.join('templates','home.html'))
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
                template_values = {'msgLogin':'','session':self.session,'wellness':wellness}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))
            else:
                directory = os.path.dirname(__file__)
                template_values = {'msgLogin':'Invalid details'}
                path = os.path.join(directory, os.path.join('templates','home.html'))
                self.response.out.write(template.render(path,template_values, _DEBUG))

class SignOut(webapp.RequestHandler):
    def get(self):
        self.session = Session()
        self.session.delete_item('username')
        self.session.delete_item('name')
        self.session.delete_item('type')
        directory = os.path.dirname(__file__)
        template_values = {'msgLogin':'Invalid details','session':self.session}
        path = os.path.join(directory, os.path.join('templates','home.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))
        
class Medicalrecords(webapp.RequestHandler):
    def get(self):        
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':'hello','session':self.session}
        path = os.path.join(directory, os.path.join('templates','medicalrecords.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class UploadRecord(webapp.RequestHandler):
    def get(self):
        self.session = Session()        
        upload_url = blobstore.create_upload_url('/upload')
        #self.response.out.write('<html><body>')
        #self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
        #self.response.out.write("""Upload Record: <input type="file" name="file"><br> <input type="submit" name="submit" value="Submit"> </form></body></html>""")
        directory = os.path.dirname(__file__)
        blob_data=blobstore.BlobInfo.all()
        template_values = {'blob':blob_data,'upload_url':upload_url,'session':self.session}
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
        template_values = {'msg':'hello','session':self.session}
        path = os.path.join(directory, os.path.join('templates','medicalcontacts.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class FixAppointement(webapp.RequestHandler):
    def get(self):
        self.session = Session()        
        directory = os.path.dirname(__file__)
        template_values = {'msg':'hello','session':self.session}
        path = os.path.join(directory, os.path.join('templates','fixappointment.html'))
        self.response.out.write(template.render(path,template_values, _DEBUG))

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        blob_key =self.request.get('key')
        if not blobstore.get(blob_key):
            self.error(404)
        else:
            self.send_blob(blobstore.BlobInfo.get(blob_key), save_as=True)

application = webapp.WSGIApplication([
  ('/', Ehealth),('/myprofile', Profile),('/signup', SignUp),('/signin', SignIn),('/signout', SignOut),('/uploadrecord',UploadRecord ),('/delete',DeleteRecord ),('/serve', ServeHandler),('/medicalrecords', Medicalrecords),('/medicalcontacts', MedicalContacts),('/fixappointment', FixAppointement),('/home', BloodPressure),('/exercise', Excersice),('/walking', WalkingTracker),('/swimming', Swimming),('/sugar', SugarLevel),('/sleep', HoursSlept),('/cycling', Cycling),('/bodytemp', BodyTemperature),('/heartrate', HeartRate)], debug=True)



def main():
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()

