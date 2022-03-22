from flask import *
import  pymysql
from src.myknn import prep

app=Flask(__name__)
app.secret_key='qwer'
con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="heart_didease")
cmd=con.cursor()

@app.route("/")
def main():
    return render_template("log in.html")

@app.route("/addtreatment")
def addtreatment():
    return render_template("addtreatmentdoc.html")

@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")
@app.route("/askquestion")
def askquestion():
    cmd.execute("select*from question where u_id= '"+str(session['lid'])+"'")
    s=cmd.fetchall()
    return render_template("askquestion user.html",val=s)
@app.route("/dochome")
def dochome():
    return render_template("dochome.html")
@app.route("/register")
def register():
    return render_template("register user.html")
@app.route("/qsts",methods=['post'])
def qsts():
    return render_template("add_question.html")
@app.route('/regester',methods=['post'])
def regester():
    name=request.form['textfield']
    age=request.form['textfield2']
    gender=request.form['radiobutton']
    mobile=request.form['textfield4']
    email=request.form['textfield5']
    username=request.form['textfield6']
    password=request.form['textfield7']
    cmd.execute("insert into login values(null,'" + username +"','"+password+"','user')" )
    lid=con.insert_id()
    cmd.execute("insert into user values(null,'"+ str(lid)+"','"+name+"','"+age+"','"+gender+"','"+mobile+"','"+email+"')")
    con.commit()
    return'''<script>alert("inserted");window.location="/userhome"</script>'''

@app.route('/add_question',methods=['post'])
def add_question():
    quest=request.form['textarea']
    cmd.execute("insert into question values(null,'"+ str(session['lid'])+"','"+quest+"','pending',curdate())")
    con.commit()
    return'''<script>alert("inserted");window.location="/userhome"</script>'''

@app.route('/send_feddback',methods=['post'])
def send_feddback():
    feeds=request.form['textarea']
    cmd.execute("insert into view_feedback values(null,'"+ str(session['lid'])+"','"+feeds+"',curdate())")
    con.commit()
    return'''<script>alert("inserted");window.location="/userhome"</script>'''

@app.route("/viewprediction")
def viewprediction():
    return render_template('prediction.html')
@app.route("/feedbacks")
def feedbacks():
    return render_template('addfeedback.html')

@app.route("/viewprediction1",methods=['post'])
def viewprediction1():

    Name=request.form['textfield2']
    Gender=request.form['radiobutton']
    Chestpaintype=request.form['select']
    Rastingbloodsugar=request.form['select2']
    Restceg=request.form['select3']
    Exang=request.form['select4']
    Slope=request.form['select5']
    CA=request.form['ca']
    Thal=request.form['select6']
    Testbloodpressure=request.form['textfield4']
    Serumcholestrol=request.form['textfield5']
    thalach=request.form['textfield3']
    oldpeak=request.form['textfield6']
    Ageinyear=request.form['textfield7']
    val=(int(Ageinyear),int(Gender),int(Chestpaintype),int(Testbloodpressure),int( Serumcholestrol),int( Rastingbloodsugar),int(Restceg),int(thalach),int( Exang),int(oldpeak),int(Slope),int(Thal),int(CA))
    res=prep(val)
    if res==0:
        res="STAGE A"
        res1="As stated in other articles, the signs and symptoms of Heart Failure are not always easy to detect. But with awareness of family history (genetics), personal behavior (diet, exercise regime, drug abuse, alcohol and sodium intake), and health related problems (diabetes, infection, anemia, and thyroid problems), a person may determine whether or not they may be at a high risk for Heart Failure. Obviously those people that have a family history of high blood pressure (hypertension), diabetes, or heart problems should pay close attention to heart health. If you have a history of the aforementioned problems, or if you have a diet high in fat, abuse alcohol or drugs, or smoke, you may be a high risk candidate for Stage A Heart Failure.";
        return render_template('prediction1.html', nm=Name, r=res, r1=res1)
    elif res==1:
        res= "STAGE B";
        res1="Stage B Heart Failure candidates have probably never experienced symptoms of HF, but have been diagnosed with the disease. There is clear evidence of Heart Failure during diagnosis but no clear symptoms. At this point a physician may prescribe medication such as ACE Inhibitors or Beta Blockers (See-Glossary) There will be close monitoring of blood pressure (hypertension OR hypotension-See Glossary). ";
        return render_template('prediction1.html', nm=Name, r=res, r1=res1)
    elif res==2:
        res="STAGE C";
        res1="In Stage C, cardiac dysfunction is present, as are symptoms. Tiredness while performing simple activities like walking or bending over, are common symptoms. Shortness of breath and overall fatigue are present. In Stage C strict attention should be paid to exercise (consult your physician), eating properly (with low sodium intake) and little to no alcohol consumption.";
        return render_template('prediction1.html', nm=Name, r=res, r1=res1)
    else:
        res= "STAGE D";
        res1="Patients in Stage D of Heart Failure show signs and symptoms of HF even though they have undergone treatment and therapy. Monitoring of diet, exercise, and blood pressure is still adhered to during Stage D. Patients will probably be prescribed medications, depending on the person and the extent of Heart Failure. This stage is associated with surgical options. ";

        return render_template('prediction1.html',nm=Name,r=res,r1=res1)


@app.route("/registrationdoc")
def registrationdoc():
    return render_template("registration doc.html")
@app.route("/replydoc")
def replydoc():
    id=request.args.get('id')
    session['id']=id
    return render_template("replydoc.html")

@app.route("/reply1",methods=['get','post'])
def reply1():
    reply=request.form['reply']
    cmd.execute("update question set reply='"+reply+"' where q_id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert("replied");window.location="/viewquestion"</script>'''
@app.route("/acceptdoc")
def acceptdoc():
    cmd.execute(
        "SELECT `docter`.* FROM `docter` JOIN `login` ON `docter`.`iog_id`=`login`.`login_id` WHERE `login`.`type`='pending'")
    s = cmd.fetchall()
    return render_template("accept_doctors.html",val=s)
@app.route("/viewapprovedoc")
def viewapprovedoc():
    cmd.execute("SELECT `docter`.* FROM `docter` JOIN `login` ON `docter`.`iog_id`=`login`.`login_id` WHERE `login`.`type`!='pending'")
    s=cmd.fetchall()
    return render_template("view approved doc.html",val=s)
@app.route("/viewdocuser")
def viewdocuser():
    cmd.execute("SELECT * FROM 'doc user' JOIN 'LOGIN' ON 'docter'.'log_id'='login'.'login_d' WHERE 'login'.'type'!='pending'")
    s=cmd.fetchall()
    return render_template("view doc usre.html")
@app.route("/viewfeedback")
def viewfeedback():
    cmd.execute("SELECT `user`.`name`,`view_feedback`.`feedback`,`view_feedback`.`date` FROM `user` JOIN `view_feedback` ON `view_feedback`.`user_id`=`user`.`log_id`")
    s=cmd.fetchall()
    return render_template("view feedback.html",val=s)
@app.route("/viewquestion")
def viewquestion():
    cmd.execute("SELECT `question`.*,`user`.`name` FROM `user` JOIN `question` ON `question`.`u_id`=`user`.`log_id` WHERE `question`.`reply`='pending'")
    s=cmd.fetchall()

    return render_template("view questiondoc.html",val=s)
@app.route("/viewtreatment")
def viewtreatment():
    cmd.execute("select * from treatment")
    s=cmd.fetchall()
    return render_template("view treatment user.html",s=s)
@app.route('/addtreatments',methods=['post'])
def addtreatments():
    treatment_name=request.form['textfield']
    details=request.form['textfield2']
    fee=request.form['textfield3']
    cmd.execute("insert into treatment values(null,'"+str(session['lid'])+"','"+treatment_name+"','"+details+"','"+fee+"')")
    con.commit()
    return'''<script>alert("inserted");window.location="/dochome"</script>'''
@app.route("/viewuser")
def viewuser():
    cmd.execute("SELECT * FROM `user`")
    s=cmd.fetchall()
    return render_template("view users.html",val=s)
@app.route("/viewquestiondoc")
def viewquestiondoc():
    return render_template("viewquestiondoc.html")

@app.route("/login",methods=['get','post'])
def login():
    username = request.form['textfield']
    password = request.form['textfield2']
    cmd.execute("select * from login where user_name='" + username + "' and password='" + password + "'")
    s=cmd.fetchone()

    if s is not None:
            if s[3]=="admin":
                return '''<script>alert("loginsuccessful");window.location="/adminhome"</script>'''
            elif s[3]=="docter":
                session['lid']=s[0]
                return '''<script>alert("loginsuccessful");window.location="/dochome"</script>'''
            elif s[3]=="user":
                session['lid']=s[0]
                return '''<script>alert("loginsuccessful");window.location="/userhome"</script>'''
            else:
                return '''<script>alert("login failed");window.location="/"</script>'''



    else:
        return '''<script>alert("login failed");window.location="/"</script>'''


@app.route("/userhome",methods=['get','post'])
def userhome():
    return render_template("userhome.html")

@app.route("/docreg",methods=['get','post'])
def docreg():
    name=request.form['textfield']
    gen=request.form['radio']
    qualification=request.form['textfield4']
    specified_in=request.form['textfield5']
    mobile=request.form['textfield6']
    email=request.form['textfield7']
    Username=request.form['un']
    Password=request.form['pwd']
    cmd.execute("insert into login values(null,'"+ Username +"','"+Password+"','pending')" )
    id=con.insert_id()
    cmd.execute("insert into docter values(null,'"+str(id)+"','"+name+"','"+qualification+"','"+gen+"','"+specified_in+"','"+email+"','"+mobile+"')")
    con.commit()
    return '''<script>alert('ok');window.location='/'</script>'''
@app.route("/accept",methods=['get'])
def accept():
    id=request.args.get('login_id')
    cmd.execute("update login set type='docter' where login_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("verified");window.location="/acceptdoc"</script>'''
@app.route("/reject",methods=['get'])
def reject():
    id=request.args.get('login_id')
    cmd.execute("delete from login where login_id='"+str(id)+"'")
    cmd.execute("delete from docter where iog_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("denied");window.location="/acceptdoc"</script>'''
if __name__=="__main__":
    app.run(debug=True)
