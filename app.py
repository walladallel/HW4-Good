
# importing Modules
from flask import Flask, request, render_template
import datetime
import pprint
import json
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    message = ''
    if request.method == "POST":
        # getting input with name = fname in HTML form
        fname1 = request.form.get("fname1")
        fname2 = request.form.get("fname2")
        fname3 = request.form.get("fname3")
        # getting input with name = lname in HTML form 
        lname1 = request.form.get("lname1")
        lname2 = request.form.get("lname2") 
        lname3 = request.form.get("lname3") 
        # getting input with name = bday in HTML form 
        bday1 = request.form.get("bday1")
        bday2 = request.form.get("bday2")
        bday3 = request.form.get("bday3")
        # getting input with name = smoking in HTML form 
        Smoking1 = request.form.get("Smoking1")
        Smoking2 = request.form.get("Smoking2")
        Smoking3 = request.form.get("Smoking3")
        # getting input with name = ID in HTML form
        id1 = request.form.get("id1")
        id2 = request.form.get("id2")
        id3 = request.form.get("id3")

        worker_list = {}

        #Converting id(int) to string
        id_num1=str(id1)
        id_num2=str(id2)
        id_num3=str(id3)

        #adding 0 to id number if there is not 9 digist   
        idf1=id_num1.zfill(9)
        idf2=id_num2.zfill(9)
        idf3=id_num3.zfill(9)

        #Validation first name Capital
        fname1=fname1.capitalize()
        fname2=fname2.capitalize()
        fname3=fname3.capitalize()
        
        #Validation last name Capital
        lname1=lname1.capitalize()
        lname2=lname2.capitalize()
        lname3=lname3.capitalize()

        #Checking if Message exist
        if (type(fname1)) == str or (type(fname2)) == str or (type(fname3)) == str:
         message = "Hello" + fname1 + " " + lname1 
        else:
            message = " "

        #Smoking 
        if Smoking1 ==("true"):
            Smoking1=(" Yes (its not healthy!\N{angry face})")  
        else:
            Smoking1=(" No ,You Do not smoke \N{smiling face with sunglasses}")
        if Smoking2 ==("true"):
            Smoking2=(" Yes (its not healthy!\N{loudly crying face})")
        else:
            Smoking2=(" No ,You Do not smoke \N{slightly smiling face}")
        if Smoking3 ==("true"):
            Smoking3=(" Yes (its not healthy!\N{unamused face})" )
        else:
            Smoking3=(" No ,You Do not smoke \N{grinning face with smiling eyes}") 
                
        #Adding worker_list to Users Dictionery 
        worker_list={fname1: {'First Name': fname1 , 'Last Name': lname1, "Id":idf1, 'Is Smoking': Smoking1, "Birthday" :bday1},
        fname2: {'First Name': fname2 , 'Last Name': lname2, "Id":idf2, 'Is Smoking': Smoking2 ,"Birthday" :bday2},
        fname3: {'First Name': fname3 , 'Last Name': lname3, "Id":idf3, 'Is Smoking': Smoking3 ,"Birthday" :bday3}}   
                
        #Sorting workerlist with sorted & printing it nicer with pprint 
        az_workerlist = sorted(worker_list)
        for j in az_workerlist:
                    pp = pprint.PrettyPrinter(indent=4)
                    pp.pprint(worker_list[j])

        #Converting workerlist into a string with json
        final_str = json.dumps(worker_list)

        #Saving the final sorted string into a .txt file
        output_Workerlist = open("file.txt","w")
        output_Workerlist.write(final_str)
        output_Workerlist.close()

        return render_template('index.html' ,message=message,fname1=fname1 , lname1=lname1 , bday1=bday1 ,Smoking1=Smoking1 ,id1=idf1,fname2=fname2 , lname2=lname2 , bday2=bday2 ,Smoking2=Smoking2 ,id2=idf2, fname3=fname3 , lname3=lname3 , bday3=bday3 ,Smoking3=Smoking3 ,id3=idf3)
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()(host="0.0.0.0", port=5000, debug=True)