import cgi
import datetime
import re
import sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

### Class Tutor 

class Tutor(db.Model):
    name=db.StringProperty()
    surname=db.StringProperty()
    date=db.DateProperty() #Birthday
    department=db.StringProperty()
    title=db.StringProperty()

### Entities of class Tutor 

helen = Tutor(key_name = 'Helen', name = 'Helen', surname = 'Smith', date = datetime.date(year=1953, month=12, day=27), department = 'Computer Science and Engineering', title = 'Science')
helen.put()
walter = Tutor(key_name = 'Walter', name = 'Walter', surname = 'White', date = datetime.date(year=1963, month=10, day=12), department = 'Business Studies', title = 'Economy')
walter.put()
litz = Tutor(key_name = 'Litz', name = 'Litz', surname = 'Brown', date = datetime.date(year=1983, month=10, day=25), department = 'Computer Science', title = 'Computer Science', parent=helen)
litz.put()
teresa = Tutor(key_name = 'Teresa', name = 'Teresa', surname = 'Lisbon', date = datetime.date(year=1965, month=05, day=30), department = 'Marketing', title = 'Publicity')
teresa.put()
john = Tutor(key_name = 'John', name = 'John', surname = 'Red', date = datetime.date(year=1949, month=02, day=15), department = 'Marketing', title = 'Marketing and Business')
john.put()
jessie = Tutor(key_name = 'Jessie', name = 'Jessie', surname = 'Pickman', date = datetime.date(year=1970, month=03, day=04), department = 'Business Studies', title = 'Marketing and Business', parent=walter)
jessie.put()
patrick = Tutor(key_name = 'Patrick', name = 'Patrick', surname = 'Jane', date = datetime.date(year=1960, month=11, day=04), department = 'Marketing', title = 'Publicity', parent=teresa)
patrick.put()
carol = Tutor(key_name = 'Carol', name = 'Carol', surname = 'Taylor', date = datetime.date(1973, month=05, day=06), department = 'Computer Science', title = 'Computer Science')
carol.put()
albert = Tutor(key_name = 'Albert', name = 'Albert', surname = 'Lamb', date = datetime.date(year=1973, month=03, day=04), department = 'Computer Science', title = 'Computer Science', parent=helen)
albert.put()

TutorList = [helen, walter, litz, teresa, john, jessie, patrick, carol, albert]

### Class Student 

class Student(db.Model):
    name = db.StringProperty()
    surname = db.StringProperty()
    date = db.DateProperty() #Birthday
    title = db.StringProperty()
    grade = db.IntegerProperty()
    mingrade = db.IntegerProperty()
    credits = db.IntegerProperty()
    average = db.FloatProperty()
    tutor = db.StringProperty()

### Entities of class Student 

sheldom = Student(key_name = 'Sheldom', name = 'Sheldom', surname = 'Cooper', date = datetime.date(year=1988, month=12, day=04), title = 'Computer Science', grade = 4, tutor = 'Carol', parent=carol)
sheldom.put();
ian = Student(key_name = 'Ian', name = 'Ian', surname = 'Ritchie', date = datetime.date(year=1990, month=06, day=12), title = 'Publicity', grade = 3, tutor = 'Teresa', parent=teresa)
ian.put();
robert = Student(key_name = 'Robert', name = 'Robert', surname = 'Langdon', date = datetime.date(year=1992, month=12, day=05), title = 'Business and Economy', grade = 2, mingrade = 1, credits = 35, average = 6.7, tutor = 'Walter', parent=walter)
robert.put();
debra = Student(key_name = 'Debra', name = 'Debra', surname = 'Fieguth', date = datetime.date(year=1990, month=07, day=07), title = 'Computer Science', grade = 4, tutor = 'Helen', parent=helen)
debra.put();
jaime = Student(key_name = 'Jaime', name = 'Jaime', surname = 'Smith', date = datetime.date(year=1993, month=03, day=01), title = 'Business and Economy', grade = 2)
jaime.put();
alicia = Student(key_name = 'Alicia', name = 'Alicia', surname = 'Mant', date = datetime.date(year=1989, month=04, day=14), title = 'Publicity', grade= 4, tutor = 'Carol', parent=carol)
alicia.put();
aviva = Student(key_name = 'Aviva', name = 'Aviva', surname = 'Webb', date = datetime.date(year=1990, month=02, day=25), title = 'Business and Economy', grade = 4, tutor = 'Carol', parent=carol)
aviva.put();
alex = Student(key_name = 'Alex', name = 'Alex', surname = 'Kay', date = datetime.date(year=1986, month=02, day=28), title = 'Publicity', grade = 4, mingrade = 3, credits = 72, average = 7.3, tutor = 'Walter', parent=walter)
alex.put();
david = Student(key_name = 'David', name = 'David', surname = 'Moon', date = datetime.date(year=1989, month=01, day=31), title = 'Marketing', grade = 3, tutor = 'John', parent=john)
david.put();
amy = Student(key_name = 'Amy', name = 'Amy', surname = 'House', date = datetime.date(year=1991, month=05, day=13), title = 'Marketing', grade = 1)
amy.put();
alanis = Student(key_name = 'Alanis', name = 'Alanis', surname = 'Parket', date = datetime.date(year=1988, month=07, day=22), title = 'Publicity', grade = 4, mingrade = 4, credits = 87, average = 8.3, tutor = 'Walter', parent=walter)
alanis.put();
denis = Student(key_name = 'Denis', name = 'Denis', surname = 'Woodman', date = datetime.date(year=1993, month=05, day=15), title = 'Publicity', grade = 1, mingrade = 1, credits = 25, average = 5.3, tutor = 'Walter', parent=walter)
denis.put();

StudentList = [sheldom, ian, robert, debra, jaime, alicia, aviva, alex, david, amy, alanis, denis]

### Class FinalProject 

class FinalProject(db.Model):
    title = db.StringProperty()
    name = db.StringProperty()    #Author name
    surname = db.StringProperty() #Author surname
    read = db.BooleanProperty(default=False)
    date = db.DateProperty()      #When was read
    mark = db.FloatProperty()
    pages = db.IntegerProperty()

### Entities of class FinalProject 

sTASheldom = FinalProject(key_name = 'STASheldom', title = 'String theory aplication', name = 'Sheldom', surname = 'Cooper', read = True, date = datetime.date(year=2012, month=04, day=23), mark = 10.0, pages = 250, parent=sheldom)
sTASheldom.put()
aMPVPIan = FinalProject(key_name = 'AMPVPIan', title = 'A marketing point of view for a product', name = 'Ian', surname = 'Ritchie', pages = 100, parent=ian)
aMPVPIan.put()
aGCDebra = FinalProject(key_name = 'AGCDebra', title = 'Algorithms for graph coloring', name = 'Debra', surname = 'Fieguth', read = True, date = datetime.date(year=2013, month=10, day=25), pages = 150, parent=debra)
aGCDebra.put()
sPPLAlicia = FinalProject(key_name = 'SPPLAlicia', title = 'Study, packaging and product launch', name = 'Alicia', surname = 'Mant', read = True, date = datetime.date(year=2012, month=11, day=04), mark = 9.0, pages = 100, parent=alicia)
sPPLAlicia.put()
cSNLPBAlex = FinalProject(key_name = 'CSNLPBAlex', title = 'Comercial study for a new line of publicity business', name = 'Alex', surname = 'Kay', pages = 90, parent=alex)
cSNLPBAlex.put()
mSMWAviva = FinalProject(key_name = 'MSMWAviva', title = 'A Micro-economy study on mobile world', name = 'Aviva', surname = 'Webb', read = True, date = datetime.date(year=2012, month=06, day=13), mark = 8.5, pages = 320, parent=aviva)
mSMWAviva.put()

FinalProjectList = [sTASheldom, aMPVPIan, aGCDebra, sPPLAlicia, cSNLPBAlex, mSMWAviva]

testsuiteclasses = ['Tutor', 'Student', 'FinalProject']
classlists = [TutorList, StudentList, FinalProjectList]

""" Main page html structure 

This page contains the structure of the main page of the program. 

The form is to execute a GQL query. The files witch contains the query has an specific 
structure: the first line is the query, and the following lines are its possibles arguments. 
The action in the form /inputfile is focus in the specific GQL queries developed by TER and 
UCASE research groups. The functions behind the inputfile action have been developed to prove 
the GQL mutation operators defined by us.
"""

MAIN_PAGE_HTML = """\
<html>
<body>
<form action="/inputfile" method="post">
<div><p>Introduce the name of the file to execute:</p></div>
<div><textarea name="content" rows="1" cols="30"></textarea></div>
<div><input type="submit" value="Submit"></div>
</form>
</body>
</html>
"""

### Class MainPage 

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write(MAIN_PAGE_HTML)

""" Function readFileLine

This function read files witch contains one GQL query. The first line is the query, and the 
following ones are the possibles arguments of the query. The function returns the GQL query 
that can be processed by the Google App Engine.
"""
	
def readFileLine(file):
    fileToExecute = open(file, "r");
    query = fileToExecute.readline();
    query = query[0:-1]
    item = 0;
    patron = re.compile('(:[0-9]+)')
    replacelist = patron.findall(query)
    while True:
        line = fileToExecute.readline();
        line = line[0:-1]
        if (line):
            query = query.replace(replacelist[item], line)
            item += 1;
        else:
            break
        fileToExecute.close();
    return query;

""" ResultsPage class

This class contains the structure of the results html page. This part of the program is based on 
the classes, entities and queries developed by TER and UCASE research groups. This class is just 
used in the action "inputfile" of the class MainPage form. This class help us to check if the 
outputs queries are different. The structure of the html page is different depends on the number 
of the file witch contains the GQL language. 
"""

class ResultsPage(webapp.RequestHandler):
    def post(self):
        self.response.out.write('<html><body><h1>The query to execute:</h1><pre>')
        file = cgi.escape(self.request.get('content'))
        query = readFileLine(file)
        self.response.out.write('<p><b>%s</b>' % query)
        qresults = db.GqlQuery(query)
        self.response.out.write('<h1>Results for the query:</h1>')
        for qresult in qresults:
            if (type(qresult) is Tutor):
                self.response.out.write('<p><b>--- TUTOR ---</b>')
            if (type(qresult) is Student):
                self.response.out.write('<p><b>--- STUDENT ---</b>')
            if (type(qresult) is FinalProject):
                self.response.out.write('<p><b>--- FINAL PROJECT ---</b>')
            self.response.out.write('<p><b>Name:</b> %s  ' % qresult.name)
            if hasattr(qresult, "surname"):
                self.response.out.write('<b>Surname:</b> %s </p>' % qresult.surname)
            self.response.out.write('<p><b>Date:</b> %s </p>' % qresult.date)
            if hasattr(qresult, "title"):
                self.response.out.write('<p><b>Title:</b> %s </p>' % qresult.title)
            if hasattr(qresult, "grade"): 
                self.response.out.write('<p><b>grade:</b> %d </p>' % qresult.grade)
            if hasattr(qresult, "mingrade"):
                self.response.out.write('<p><b>mingrade:</b> %d </p>' % qresult.mingrade)
            if hasattr(qresult, "credits"):
                self.response.out.write('<p><b>Credits:</b> %d </p>' % qresult.credits)
            if hasattr(qresult, "department"):
                self.response.out.write('<p><b>Department:</b> %s </p>' % qresult.department)
            if hasattr(qresult, "mark"):
                self.response.out.write('<p><b>Mark:</b> %s  ' % qresult.mark)
	self.response.out.write('</pre></body></html>')


application = webapp.WSGIApplication(
                                     [('/', MainPage),
									 ('/inputfile', ResultsPage),],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()