import cgi
import cgitb
cgitb.enable
import athletemodel
import yate

form_data = cgi.FieldStorage()#獲取所有表單數據，並放在一個字典中
athlete_name = form_data['which_athlete'].value#.value是從表單數據訪問一個指定的數據

athletes = athletemodel.get_from_store()
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: "+athlete_name+ ",DOB:"+ 
        athletes[athlete_name].dob+"."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))#有@就不需要再top3加()
print(yate.include_footer({"Home":"/index.html", "Select another athlete":
                            "generate_list.py"}))
