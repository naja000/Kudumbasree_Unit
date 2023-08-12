from flask import Flask, render_template, request, redirect,session,jsonify
import datetime
from DBConnection import Db

app = Flask(__name__)
app.secret_key="kkk"
# staticpath=r"C:\Users\DELL\Documents\kudumbasree project\\"
staticpath=r"C:\Users\DELL\Documents\kudumbasree project\static\\"

# @app.route('/')
# def login():
#     return render_template('login.html')

@app.route('/login_post', methods=['post'])
def login_post():
    uname = request.form['name']
    psword = request.form['pwd']
    qry="SELECT `login_id`,`type` FROM `login` WHERE `username`='"+uname+"' AND PASSWORD='"+psword+"'"
    dd=Db()
    res=dd.selectOne(qry)
    session["lid"]=res["login_id"]
    if res["type"]=="admin":
        return '''<script>alert('Login Successfully');window.location='/ad'</script>'''
    elif res["type"]=="kudumbasree":
        q2="SELECT `staus` FROM `kudmbasree` WHERE `login_id`='"+str(res["login_id"])+"'"
        res2=dd.selectOne(q2)
        if res2 is not None:
            if res2["staus"]=="approved":
                return '''<script>alert('Login Successfully');window.location='/khome'</script>'''

            else:

                return '''<script>alert('pending');window.location='/'</script>'''

        else:
            return '''<script>alert('invalid');window.location='/'</script>'''
    elif res["type"]=="user":
        return '''<script>alert('Login Successfully');window.location='/uhome'</script>'''


    else:
        return '''<script>alert('invalid');window.location='/'</script>'''


@app.route('/admintemp')
def admin_admintemp():
    return render_template('admin/admintemp.html')

@app.route('/admin_home')
def admin_home():
    return render_template('admin/home.html')



@app.route('/admin_add_festval')
def admin_add_festval():
    return render_template('admin/add_festival.html')

@app.route('/admin_add_festval_post',methods=['post'])
def admin_add_festval_post():
    name = request.form['textfield']
    image = request.files['file']
    date = request.form['textfield2']
    time = request.form['time']
    desc = request.form['textfield3']
    date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    image.save(r"C:\Users\DELL\Documents\kudumbasree project\static\festval\\"+date+'.jpg')
    path="/static/festval/"+date+'.jpg'
    qry="INSERT INTO festival(DATE,TIME,description,image,name)VALUES('"+date+"','"+time+"','"+desc+"','"+path+"','"+name+"')"
    dd=Db()
    id=dd.insert(qry)
    return '''<script>alert('success');window.location='/admin_add_festval'</script>'''

@app.route('/admin_delete_festival/<id>')
def delete_festival(id):
    dd=Db()
    qry="delete from festival where fest_id='"+id+"'"
    res=dd.delete(qry)
    return'''<script>alert('deleted');window.location='/admin_view_festival'</script>'''


@app.route('/admin_add_notification')
def admin_add_notification():
    return render_template('admin/add_notification.html')

@app.route('/admin_add_notification_post',methods=['post'])
def admin_add_notification_post():
    notification = request.form['textfield']
    qry="INSERT INTO notification(notification,`date`)VALUES('"+notification+"',curdate())"
    dd=Db()
    dd.insert(qry)
    return '''<script>alert('success');window.location='/admin_add_notification'</script>'''


@app.route('/admin_delete_notification/<id>')
def admin_delete_notification(id):
    dd=Db()
    qry="delete from notification where nid='"+id+"'"
    res=dd.delete(qry)
    return '''<script>alert('deleted');window.location='/admin_view_notification'</script>'''


# @app.route('/admin_admin_send_reply')
# def admin_admin_send_reply():
#     return render_template('admin/admin_send_reply.html')
#
# @app.route('/admin_admin_send_reply_post',methods=['post'])
# def admin_admin_send_reply_post():
#     reply = request.form['textfield']
#     qry="insert into admin_send_reply()
#
#     return 'ok'

@app.route('/admin_send_reply/<id>')
def admin_send_reply(id):
    return render_template('admin/admin_send_reply.html',id=id)

@app.route('/admin_send_reply_post',methods=['post'])
def admin_send_reply_post():
    dd = Db()
    reply = request.form['textfield']
    id = request.form['hid']
    qry="update `user_complaint` set `reply`='"+reply+"', `STATUS`='replied' where uc_id='"+id+"'"
    res=dd.update(qry)
    return redirect("/admin_view_complaints_and_send_reply")

@app.route('/admin_view_and_approval_of_kudumbasree')
def admin_view_and_approval_of_kudumbasree():
    dd = Db()
    qry = "SELECT * FROM `kudmbasree` WHERE STAUS='pending'"
    res = dd.select(qry)
    return render_template('admin/view_and_approval_of_kudumbasree.html', data=res)



@app.route('/admin_view_and_approving_of_kudumbasree/<ab>/<b>')
def admin_view_and_approving_of_kudumbasree(ab,b):
    dd = Db()
    qry = "UPDATE `kudmbasree` SET `staus`='approved' WHERE `kudumbasree_id`='"+ab+"'"
    qry2 = "UPDATE `login` SET `type`='kudumbasree' WHERE `login_id`='"+b+"'"
    res = dd.update(qry)
    res2 = dd.update(qry2)
    return admin_view_and_approval_of_kudumbasree()


@app.route('/admin_view_and_approval_of_kudumbasree_post',methods=['post'])
def admin_view_and_approval_of_kudumbasree_post():
    search_name = request.form['textfield']
    dd = Db()
    qry = "SELECT * FROM `kudmbasree` WHERE staus='pending' and name like '%"+search_name+"%'"
    res = dd.select(qry)
    return render_template('admin/view_and_approval_of_kudumbasree.html', data=res)


@app.route('/admin_view_approved_kudumbasree')
def admin_view_approved_kudumbasree():
    dd = Db()
    qry = "SELECT * FROM `kudmbasree` WHERE STAUS='approved'"
    res = dd.select(qry)

    return render_template('admin/view_approved_kudumbasree.html',data=res)
@app.route('/admin_view_approved_kudumbasree_post',methods=['post'])
def admin_view_approved_kudumbasree_post():
    search_name = request.form['textfield']
    dd=Db()
    qry="SELECT * FROM `kudmbasree` WHERE STAUS='approved' and name like '%"+search_name+"%'"
    res = dd.select(qry)
    return render_template('admin/view_approved_kudumbasree.html', data=res)

@ app.route('/admin_view_product_information/<lid>')
def admin_view_product_information(lid):
    qry="SELECT * FROM `product` WHERE `kudumbasree_id`='"+lid+"'"
    dd=Db()
    res=dd.select(qry)
    return render_template('admin/view_product_information.html',data=res)

# @ app.route('/admin_search_product_information_post',methods=['post'])
# def admin_search_product_information_post():
#     search=request.form['textfield']
#     dd=Db()
#     qry="select * from product where product_name like '%"+search+"%'"
#     res=dd.select(qry)
#     return render_template('/admin_search_product_information_post.html', data=res)







@app.route('/admin_view_complaints_and_send_reply')
def admin_view_complaints_and_send_reply():
    dd = Db()
    qry = "select * from user_complaint,user where user_complaint.from_id=user.l_id"
    res = dd.select(qry)
    return render_template('admin/view_complaints_and_send_reply.html', data=res)

@app.route('/admin_view_complaints_and_send_reply_post',methods=['post'])
def admin_view_complaints_and_send_reply_post():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd = Db()
    qry = "SELECT user.name,user.email,user_complaint.* FROM USER INNER JOIN user_complaint ON user.l_id=user_complaint.from_id WHERE user_complaint.DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
    res = dd.select(qry)
    print(qry)
    return render_template('admin/view_complaints_and_send_reply.html', data=res)


# @app.route('/admin_complaints_reply')
# def admin_complaints_reply():
#     return render_template('send_reply.html')



@app.route('/admin_view_complaints_from_users_about_kudumba')
def admin_view_complaints_of_users_about_kudumba():
    dd = Db()
    qry = "SELECT `user`.name as uname,`user`.`email`,`kudmbasree`.`name`,`kudmbasree`.`email_id`,`kudumbasree_complaint`.* FROM `user` INNER JOIN `kudumbasree_complaint` ON `user`.`l_id`=`kudumbasree_complaint`.`from_id` INNER JOIN `kudmbasree` ON `kudmbasree`.`login_id`=`kudumbasree_complaint`.`ksree_lid`"
    res = dd.select(qry)
    # print(qry)
    # print(res)
    return render_template('admin/view_complaints_from_users_about_kudumba.html',data=res)
@app.route('/view_complaints_from_users_about_kudumba_search',methods=["post"])
def view_complaints_from_users_about_kudumba_search():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd = Db()
    qry = "SELECT `user`.name as uname,`user`.`email`,`kudmbasree`.`name`,`kudmbasree`.`email_id`,`kudumbasree_complaint`.* FROM `user` INNER JOIN `kudumbasree_complaint` ON `user`.`l_id`=`kudumbasree_complaint`.`from_id` INNER JOIN `kudmbasree` ON `kudmbasree`.`login_id`=`kudumbasree_complaint`.`ksree_lid` WHERE kudumbasree_complaint.DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
    res = dd.select(qry)
    print(qry)
    return render_template('admin/view_complaints_from_users_about_kudumba.html', data=res)

# @app.route('/kudumbasree_send_reply/<id>')
# def kudumbasree_send_reply(id):
#     return render_template('admin/send_reply.html',id=id)
#
#
#
#
# @app.route('/kudumbasree_send_reply_post',methods=["post"])
# def kudumbasree_send_reply_post():
#     dd = Db()
#     reply = request.form['textfield']
#     id = request.form['hid']
#     qry = "update `kudumbasree_complaint` set `reply`='" + reply + "', `STATUS`='replied' where kc_id='" + id + "'"
#     res = dd.update(qry)
#     return redirect("/admin_view_complaints_from_users_about_kudumba")

@app.route('/admin_view_feedback')
def admin_view_feedback():
    dd=Db()
    qry="SELECT `user`.`name`,`user`.`email`,`feedback`.* FROM `user`INNER JOIN `feedback` ON `feedback`.`fromlid`=`user`.`l_id` "
    res=dd.select(qry)
    return render_template('admin/view_feedback.html',data=res)



@app.route('/admin_view_feedback2')
def admin_view_feedback2():
    dd=Db()
    qry="SELECT `user`.`name`,`user`.`email`,`feedback`.* FROM `user`INNER JOIN `feedback` ON `feedback`.`fromlid`=`user`.`l_id` "
    res=dd.select(qry)
    return render_template('kudumbasree/view_feedback.html',data=res)


@app.route('/admin_view_feedback_post2',methods=['post'])
def admin_view_feedback_post2():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd = Db()
    qry = "SELECT `user`.`name`,`user`.`email`,`feedback`.* FROM `user`INNER JOIN `feedback` ON `feedback`.`fromlid`=`user`.`l_id` WHERE feedback.DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
    res = dd.select(qry)
    print(qry)
    return render_template('kudumbasree/view_feedback.html',data=res)

@app.route('/admin_view_feedback_post',methods=['post'])
def admin_view_feedback_post():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd = Db()
    qry = "SELECT `user`.`name`,`user`.`email`,`feedback`.* FROM `user`INNER JOIN `feedback` ON `feedback`.`fromlid`=`user`.`l_id` WHERE feedback.DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
    res = dd.select(qry)
    print(qry)
    return render_template('admin/view_feedback.html', data=res)






@ app.route('/admin_view_festival')
def admin_view_festival():
    dd = Db()
    qry="select * from festival"
    res=dd.select(qry)
    return render_template('admin/view_festival.html',data=res)

@ app.route('/admin_view_festival_post',methods=['post'])
def admin_view_festival_post():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd=Db()
    qry="SELECT * FROM `festival` WHERE DATE BETWEEN '"+date_from+"' AND '"+date_to+"'"
    res = dd.select(qry)
    print(qry)
    return render_template('admin/view_festival.html',data=res)

@ app.route('/edit_festival/<id>')
def edit_festival(id):
    dd=Db()
    qry="select * from festival WHERE fest_id='"+id+"'"
    res=dd.selectOne(qry)
    return render_template('admin/edit_festival.html',data=res)

@ app.route('/edit_festival_post',methods=['post'])
def edit_festival_post():
    fe_id=request.form['fe_id']
    name=request.form['textfield']
    date=request.form['textfield2']
    desc=request.form['textfield3']
    time=request.form['time']
    dd=Db()
    if 'file' in request.files:
        image = request.files['file']
        if image.filename!="":              #has image
            image.save(staticpath + "festval\\" + image.filename)
            path = "/static/festval/" + image.filename
            qry = "update festival set name='" + name + "',image='" + path + "',date='" + date + "',time='" + time + "',description='" + desc + "' where fest_id='" + fe_id + "'"
        else:       #browser issue
            qry = "update festival set name='" + name + "',date='" + date + "',time='" + time + "',description='" + desc + "' where fest_id='" + fe_id + "'"

    else:       # no image
        qry="update festival set name='"+name+"',time='"+time+"'date='"+date+"',description='"+desc+"' where fest_id='"+fe_id+"'"
    res=dd.update(qry)
    return redirect("/admin_view_festival")


@app.route('/admin_view_notification')
def admin_view_notification():
    dd = Db()
    qry = "select * from notification"
    res = dd.select(qry)
    return render_template('admin/view_notification.html',data=res)

@app.route('/admin_view_notification_post',methods=['post'])
def admin_view_notification_post():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd = Db()
    qry ="SELECT * FROM `notification` WHERE DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
    res = dd.select(qry)
    print(qry)
    return render_template('admin/view_notification.html', data=res)





@app.route('/admin_view_rate_and_review/<pid>')
def admin_view_rate_and_review(pid):
   dd=Db()
   qry="SELECT `user`.`name`,`user`.`email`,`rating`.* FROM `user`INNER JOIN `rating` ON `user`.l_id=rating.u_id where rating.pid='"+pid+"'"
   res=dd.select(qry)
   return render_template('admin/view_rate_and_review.html',data=res)

# @app.route('/admin_view_rate_and_review_post',methods=['post'])
# def admin_view_rate_and_review_post():
#     date_from = request.form['textfield']
#     date_to = request.form['textfield2']
#     dd = Db()
#     qry = "SELECT `user`.`name`,`user`.`email`,`rating`.* FROM `user`INNER JOIN `rating` ON `user`.l_id=rating.u_id where rating.pid='"+pid+"' WHERE DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
#     res = dd.select(qry)
#     print(qry)
#     return render_template('admin/view_rate_and_review.html', data=res)

@ app.route('/view_financial_report')
def view_financial_report():
        return render_template('view_financial_report.html')
@ app.route('/admin_view_financial_report/<lid>')
def admin_view_financial_report(lid):
    qry="SELECT * FROM `report` where `kudumbasree_id`='"+lid+"'order by rid desc  "
        # "`kudumbasree_id`='"+lid+"'"
    dd=Db()
    res=dd.select(qry)
    return render_template('admin/view_financial_report.html',data=res)




#---------------------------------------------- Kudumbasree ----------------------------------------


@app.route('/registration')
def registration():
        return render_template('registration.html')

@app.route('/registration_post', methods=['post'])
def registration_post():
    name = request.form['textfield3']
    place = request.form['textfield4']
    area = request.form['textfield5']
    post = request.form['textfield6']
    pin = request.form['textfield7']
    district= request.form['textfield8']
    member_count = request.form['textfield9']
    leader_name = request.form['textfield11']
    leader_phone= request.form['textfield12']
    leader_photo = request.files['file']
    email = request.form['em1']
    password = request.form['password1']
    con_password = request.form['password2']

    leader_photo.save(r"C:\Users\DELL\Documents\kudumbasree project\static\kudumbasree\\" + leader_photo.filename)
    path = "/static/kudumbasree/"+leader_photo.filename
    db = Db()
    qry1 = "INSERT INTO login(username, PASSWORD, TYPE) VALUES('"+email+"','"+password+"','pending')"
    lid=db.insert(qry1)
    qry="INSERT INTO `kudmbasree`(`login_id`,`name`,`place`,`area`,`post`,`pin`,`district`,`member_count`,`leader_name`,`leader_phoneno`,`leader_photo`,`staus`,email_id) VALUES('"+str(lid)+"','"+name+"','"+place+"','"+area+"','"+post+"','"+pin+"','"+district+"','"+member_count+"','"+leader_name+"','"+leader_phone+"','"+path+"','pending','"+email+"')"
    db.insert(qry)


    return '''<script>alert('registration Successfull');window.location='/registration'</script>'''


@app.route('/khome')
def khome():
        return render_template('kudumbasree/index.html')

@app.route('/kudumbasree_add_product')
def kudumbasree_add_product():
    return render_template('kudumbasree/add_product.html')

@app.route('/kudumbasree_add_product_post',methods=['post'])
def kudumbasree_add_product_post():
    name = request.form['textfield5']
    image = request.files['file']
    quantity = request.form['textfield3']
    description = request.form['textfield2']
    cost = request.form['textfield']
    image.save(r"C:\Users\DELL\Documents\kudumbasree project\static\product\\" + image.filename)
    path = "/static/product/" + image.filename
    qry="INSERT INTO product(amount,quantity,details,image,product_name,kudumbasree_id)VALUES('"+cost+"','"+quantity+"','"+description+"','"+path+"','"+name+"','"+str(session["lid"])+"')"
    dd=Db()
    dd.insert(qry)
    return kudumbasree_add_product()

@app.route('/kudumbasree_view_product')
def kudumbasree_view_product():
    dd = Db()
    qry="select * from product where kudumbasree_id='"+str(session["lid"])+"'"
    res=dd.select(qry)
    return render_template('kudumbasree/view_added_product.html',data=res)
@app.route('/kudumbasree_edit_product/<id>')
def kudumbasree_edit_product(id):
    dd=Db()
    qry="select * from product WHERE product_id='"+id+"' "
    res=dd.selectOne(qry)
    return render_template('kudumbasree/edit_product.html',data=res)



@app.route('/kudumbasree_edit_product_post',methods=['post'])
def kudumbasree_edit_product_post():
    id = request.form['id']
    name = request.form['textfield5']

    quantity = request.form['textfield3']
    description = request.form['textfield2']
    cost = request.form['textfield']

    dd = Db()

    if 'file' in request.files:
        image = request.files['file']
        if image.filename!="":              #has image
            image.save(staticpath + "product\\" + image.filename)
            path = "/static/product/" + image.filename
            qry = "UPDATE `product` SET quantity ='" + quantity + "',details='" + description + "',product_name='" + name + "',amount='" + cost + "',image='" + path + "'where product_id='" + id + "'"
            dd.update(qry)
        else:       #browser issue
            qry = "UPDATE `product` SET quantity ='" + quantity + "',details='" + description + "',product_name='" + name + "',amount='" + cost + "' where product_id='" + id + "'"
            dd.update(qry)




    return redirect("/kudumbasree_view_product")

@app.route('/kudumbasree_delete_product/<id>')
def kudumbasree_delete_product(id):
    dd = Db()
    qry = "delete from product where product_id='" + id + "'"
    res = dd.delete(qry)
    return '''<script>alert('deleted');window.location='/kudumbasree_view_product'</script>'''

    return 'ok'

@app.route('/kudumbasree_search_product_post',methods=['post'])
def kudumbasree_search_product_post():
     search=request.form['textfield']
     dd=Db()
     qry="select * from product where product_name like '%"+search+"%' and kudumbasree_id='"+str(session["lid"])+"'"
     res=dd.select(qry)
     return render_template('kudumbasree/view_added_product.html',data=res)

@app.route('/kudumbasree_view_notification')
def kudumbasree_view_notification():
    dd = Db()
    qry = "select * from notification"
    res = dd.select(qry)
    return render_template('kudumbasree/view_notification.html',data=res)

@app.route('/kudumbasree_view_complaint')
def kudumbasree_view_complaint():
    dd = Db()
    qry = "SELECT `kudumbasree_complaint` .* , `kudmbasree`.* FROM `kudmbasree` INNER JOIN `kudumbasree_complaint` ON `kudumbasree_complaint`.ksree_lid=`kudmbasree`.`kudumbasree_id`"
    res = dd.select(qry)
    return render_template('kudumbasree/view_complaint.html',data=res)

@app.route('/kudumbasree_view_complaint_post', methods=['post'])
def kudumbasree_view_complaint_post():
    date_from = request.form['textfield']
    to_date = request.form['textfield2']
    dd = Db()
    qry="SELECT `kudumbasree_complaint` .* , `kudmbasree`.* FROM `kudmbasree` INNER JOIN `kudumbasree_complaint` ON `kudumbasree_complaint`.ksree_lid=`kudmbasree`.`kudumbasree_id` WHERE DATE BETWEEN '"+date_from+"' AND '"+to_date+"'"
    res = dd.select(qry)
    print(qry)
    return render_template('kudumbasree/view_complaint.html', data=res)

@app.route('/kudumbasree_send_reply/<id>')
def kudumbasree_send_reply(id):
    dd = Db()
    qry="select * from kudumbasree_complaint WHERE kc_id='"+str(id)+"'"
    res=dd.selectOne(qry)
    return render_template('kudumbasree/send_reply.html',data=res)

@app.route('/kudumbasree_send_reply_post',methods=["post"])
def kudumbasree_send_reply_post():
    dd = Db()
    id = request.form['id']
    reply = request.form['textfield']
    qry = "update `kudumbasree_complaint` set `reply`='" + reply + "', `STATUS`='replied' where kc_id='" + id + "'"
    res = dd.update(qry)
    return redirect("/kudumbasree_view_complaint")

@app.route('/kudumbasree_add_fin_report')
def kudumbasree_add_fin_report():
    return render_template('kudumbasree/add_fin_report.html')

@app.route('/kudumbasree_add_fin_report_post',methods=['post'])
def kudumbasree_add_fin_report_post():
    descriptions= request.form['textfield2']
    date = request.form['textfield3']
    Document=request.files['textfield2']



    Document.save(staticpath+"upload_file\\"+Document.filename)
    path="/static/upload_file/"+Document.filename

    qry="INSERT INTO `report`(`kudumbasree_id`,`date`,`file`,`descriptions`) VALUES('"+str(session['lid'])+"','"+date+"','"+path+"','"+descriptions+"')"
    dd=Db()
    dd.insert(qry)
    return'ok'

@app.route('/kudumbasree_view_fin_report')
def kudumbasree_view_fin_report():
    dd = Db()
    qry = "select * from report where kudumbasree_id='" + str(session["lid"]) + "'"
    res = dd.select(qry)
    print(qry)
    print(res)
    return render_template('kudumbasree/view_fin_report.html', data=res)

@app.route('/kudumbasree_view_festival')
def kudumbasree_view_festival():
    dd = Db()
    qry="select * from festival"
    res=dd.select(qry)
    return render_template('kudumbasree/view_festival.html',data=res)

@app.route('/kudumbasree_view_festival_post',methods=['post'])
def kudumbasree_view_festival_post():
    date_from = request.form['textfield']
    date_to = request.form['textfield2']
    dd=Db()
    qry="SELECT * FROM `festival` WHERE DATE BETWEEN '"+date_from+"' AND '"+date_to+"'"
    res = dd.select(qry)
    print(qry)
    return render_template('kudumbasree/view_festival.html',data=res)

@app.route('/kudumbasree_add_advertisement')
def kudumbasree_add_advertisement():
    return render_template('kudumbasree/add_advertisement.html')

@app.route('/kudumbasree_add_advertisement_post',methods=['post'])
def kudumbasree_add_advertisement_post():
    date=request.form['textfield']
    description = request.form['textfield1']
    image= request.files['textfield2']

    image.save(staticpath + "\\advertisement\\" + image.filename)
    path = "/static/advertisement/" + image.filename
    qry="INSERT INTO advertisement(DATE,description,image,kudumbasree_id)VALUES('"+date+"','"+description+"','"+path+"','"+str(session["lid"])+"')"
    dd=Db()
    dd.insert(qry)
    return 'ok'

@app.route('/kudumbasree_view_booking')
def kudumbasree_view_booking():
    dd = Db()
    qry = "SELECT user.name,user.email,booking_main.* FROM USER INNER JOIN booking_main ON user.l_id=booking_main.user_id where booking_main.kud_lid='"+str(session['lid'])+"'"
    res = dd.select(qry)
    print(qry)
    return render_template('kudumbasree/view_booking.html', data=res)

@app.route('/kudumbasree_view_booking_post', methods=['post'])
def kudumbasree_view_bookingt_post():
    date_from = request.form['textfield']
    to_date = request.form['textfield2']
    dd = Db()
    qry="SELECT user.name,user.email,booking_main.* FROM USER INNER JOIN booking_main ON user.l_id=booking_main.user_id WHERE DATE BETWEEN '"+date_from+"' AND '"+to_date+"'"
    res = dd.select(qry)
    print(qry)
    return render_template('kudumbasree/view_booking.html', data=res)

@app.route('/kudumbasree_view_booking_more/<id>')
def kudumbasree_view_booking_more(id):
    dd = Db()
    qry="SELECT product.*,booking_sub.*from product INNER JOIN booking_sub ON product.product_id=booking_sub.product_id WHERE booking_sub.book_id='"+str(id)+"'"
    res=dd.select(qry)
    print(qry)
    ls=[]
    total=0
    for i in res:
        ppri=i['amount']
        pq=i['qty']
        ptot=int(ppri)*int(pq)
        total=total+ptot
        ls.append({"product_name":i['product_name'],"image":i['image'],"amount":i['amount'],"qty":i['qty'],"ptot":ptot})
    return render_template('kudumbasree/view_booking_more.html',data=ls,ttt=total)

@app.route('/kudumbasree_view_rate_and_review/<pid>')
def kudumbasree_view_rate_and_review(pid):
   dd=Db()
   qry="SELECT `rating`.*, `user`.`name`,`user`.`email` FROM `user` INNER JOIN `rating` ON `user`.`l_id`=`rating`.`u_id` WHERE `rating`.`pid`='"+pid+"'"
   res=dd.select(qry)
   print(res)
   if len(res)>0:
            return render_template('kudumbasree/view_rate_and_review.html',data=res)
   else:
       return '''<script>alert('No ratingss.....Thankyou');window.location='/kudumbasree_view_product'</script>'''


@app.route('/kudumbasree_view_rate_and_review_post',methods=['post'])
def kudumbasree_view_rate_and_review_post():
     date_from = request.form['textfield']
     date_to = request.form['textfield2']
     dd = Db()
     qry = "SELECT `user`.`name`,`user`.`email`,`rating`.* FROM `user`INNER JOIN `rating` ON `user`.l_id=rating.u_id where rating.pid='"+pid+"'-     WHERE DATE BETWEEN '" + date_from + "' AND '" + date_to + "'"
     res = dd.select(qry)
     print(qry)
     return render_template('kudumbasree/view_rate_and_review.html', data=res)

# ===============================USER MODULE================================================


@app.route('/uhome')
def uhome():
        return render_template('user/userindex.html')


@app.route('/userregistration')
def userregistration():
        return render_template('userregistration.html')

@app.route('/userregistration_post', methods=['post'])
def userregistration_post():
    name = request.form['textfield3']
    place = request.form['textfield4']
    # area = request.form['textfield5']
    post = request.form['textfield6']
    pin = request.form['textfield7']
    district= request.form['textfield8']
    # member_count = request.form['textfield9']
    # leader_name = request.form['textfield11']
    leader_phone= request.form['textfield12']
    # leader_photo = request.files['file']
    email = request.form['em1']
    password = request.form['password1']
    con_password = request.form['password2']

    # leader_photo.save("D:\\kalladi2\\kudumbasree project\\static\\kudumbasree\\" + leader_photo.filename)
    # path = "/static/kudumbasree/"+leader_photo.filename
    db = Db()
    qry1 = "INSERT INTO login(username, PASSWORD, TYPE) VALUES('"+email+"','"+password+"','user')"
    lid=db.insert(qry1)
    qry="INSERT INTO `user`(`l_id`,`name`,`place`,`post`,`pin`,`district`,`email`,`phone_no`) VALUES('"+str(lid)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+email+"','"+leader_phone+"')"
    db.insert(qry)


    return '''<script>alert('registration Successfull');window.location='/logg'</script>'''



@app.route('/view_kudumbsreru')
def view_kudumbsreru():
    db=Db()
    qry=db.select("select * from kudmbasree")
    return render_template('user/view_kudumbasree.html',data=qry)


@ app.route('/user_view_product_information/<lid>')
def user_view_product_information(lid):
    qry="SELECT * FROM `product` WHERE `kudumbasree_id`='"+lid+"'"
    dd=Db()
    res=dd.select(qry)
    return render_template('user/view_product_information.html',data=res)



@app.route('/book_q/<pid>',methods=['get','post'])
def book_q(pid):
    if request.method=="POST":
        db=Db()
        q=request.form['textfield']
        # db.selectOne("select * from ")
        qry=db.insert("insert into booking_main VALUES ('','"+str(session["lid"])+"',curdate(),'booked','0','0')")
        db.insert("insert into booking_sub VALUES('','"+str(qry)+"','"+pid+"','"+q+"')")
        return '''<script>alert(' booked');window.location="/view_kudumbsreru"</script>'''



    else:
        return render_template('user/quantity.html')






@ app.route('/add_rating/<pid>',methods=['get','post'])
def add_rating(pid):
    if request.method=="POST":
        r=request.form['textfield']
        db=Db()
        db.insert("insert into rating VALUES ('','"+pid+"','"+str(session["lid"])+"','"+r+"',curdate())")
        return '''<script>alert(' Successfull');window.location='/view_kudumbsreru'</script>'''


    else:
        return render_template('user/send_rating.html')

@app.route('/view_adv')
def view_adv():
    db = Db()
    qry = db.select("select * from advertisement,kudmbasree WHERE advertisement.kudumbasree_id=kudmbasree.kudumbasree_id")
    return render_template('user/view_ad.html', data=qry)

@app.route('/view_pg')
def view_pg():
    db = Db()
    qry = db.select("select * from festival")
    return render_template('user/view_ad.html', data=qry)


@ app.route('/send_feedbck',methods=['get','post'])
def send_feedbck():
    if request.method=="POST":
        f=request.form['textarea']
        db=Db()
        db.insert("insert into feedback VALUES ('',curdate(),'"+str(session["lid"])+"','"+f+"')")
        return '''<script>alert(' Successfull');window.location='/uhome'</script>'''


    else:
        return render_template('user/send_feedback.html')

@app.route('/send_complaint', methods=['get', 'post'])
def send_review():
    if request.method == "POST":
        c = request.form['textarea']
        db = Db()
        db.insert("insert into user_complaint VALUES ('','" + str(session["lid"]) + "','" + c + "','pending','pending','pending')")
        return '''<script>alert(' Successfull');window.location='/uhome'</script>'''


    else:
        return render_template('user/send_complaint.html')

@app.route('/view_com')
def view_com():
    db = Db()
    qry = db.select("select * from user_complaint WHERE from_id='"+str(session["lid"])+"'")
    return render_template('user/view_complaints.html', data=qry)


#===============================================#

@app.route('/landindex')
def landindex():
    return render_template('landindex.html')

@app.route('/')
def landindex2():
    return render_template('landindex.html')

@app.route('/logg')
def logg():
    return render_template('loginindex.html')


@app.route('/ad')
def ad():
    return render_template('index.html')


@app.route('/reg')
def reg():
    return render_template('registration.html')
#==========================================
@app.route("/and_user_registration",methods=['post'])
def and_user_registration():

    name=request.form["name"]
    # image=request.form["img"]
    place=request.form["place"]
    post=request.form["post"]
    pin=request.form["pin"]
    email=request.form["email"]
    contact=request.form["phone"]
    password=request.form["password"]

    # import base64
    # imgdata = base64.b64decode(image)
    # from datetime import datetime
    #
    # staticpath="D:\\kalladi2\\kudumbasree project\\static\\user\\"
    #
    # filename=datetime.now().strftime("%Y%m%d%I%M%S%p")
    # sa = staticpath + filename +".jpg"
    # with open(sa, 'wb') as f:
    #     f.write(imgdata)
    #
    # sp="/static/user/"+filename+".jpg"

    qry = "insert into login (username,password,type) values ('" + email+"','" + password+"','user')"
    db=Db()
    lid=db.insert(qry)

    qry="insert into user (name,place,post,pin,email,phone_no,l_id) values ('"+name+"','"+place+"','"+post+"','"+pin+"','"+email+"','"+contact+"','"+str(lid)+"')"
    db.insert(qry)

    return jsonify(status="ok")


@app.route("/and_homemaker",methods=['post'])
def and_homemaker():
    qry="select * from homebaker"
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)

@app.route("/and_handicraft",methods=['post'])
def and_handicraft():
    qry="select * from kudmbasree"
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)


@app.route("/and_events",methods=['post'])
def and_events():
    qry="select * from festival"
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)





@app.route("/and_backer_profile",methods=['post'])
def and_backer_profile():
    uid=request.form["uid"]
    qry="select * from homebaker where h_id='"+uid+"'"
    db=Db()
    res=db.selectOne(qry)
    return  jsonify(status="ok",data=res)


@app.route("/and_bakers_product",methods=['post'])
def and_bakers_product():
    uid=request.form["lid"]
    qry = "select * from homebakerproduct where baker_lid='" + uid + "'"
    db = Db()
    res = db.select(qry)
    return jsonify(status="ok", data=res)

#
# @app.route("/and_gallery",methods=['post'])
# def and_gallery():
#     qry="select * from product"
#     print(qry)
#     db=Db()
#     res=db.select(qry)
#     return  jsonify(status="ok",data=res)


@app.route("/and_gallery",methods=['post'])
def and_gallery():
    n=request.form['id']
    qry="select * from product where kudumbasree_id='"+n+"'"
    print(qry)
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)


@app.route("/and_gallery_ser",methods=['post'])
def and_gallery_ser():
    n=request.form['id']
    na=request.form['name']
    qry="select * from product where kudumbasree_id='"+n+"' and product_name like '%"+na+"%'"
    print(qry)
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)

@app.route("/and_prdy",methods=['post'])
def and_prdy():
    qry="select * from product"
    print(qry)
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)

@app.route("/and_handicraftproduct",methods=['post'])
def and_handicraftproduct():

    id= request.form["lid"]
    qry="select * from advertisement where kudumbasree_id='"+id+"'"
    print(qry)
    db=Db()
    res=db.select(qry)

    return  jsonify(status="ok",data=res)



@app.route("/userviewdon",methods=['post'])
def userviewdon():

    id= request.form["lid"]
    qry="select product.*,booking_sub.* from booking_sub,booking_main,product where product.product_id=booking_sub.product_id and booking_sub.book_id=booking_main.book_id and booking_main.user_id='"+id+"'"
    print(qry)
    db=Db()
    res=db.select(qry)
    print(res)
    return  jsonify(status="ok",data=res)


@app.route("/jj",methods=['post'])
def jj():

    id= request.form["dd"]
    qry="delete from booking_sub where bsid='"+id+"'"
    print(qry)
    db=Db()
    res=db.delete(qry)
    print(res)
    return  jsonify(status="ok")



@app.route("/and_view_complaints",methods=['post'])
def and_view_complaints():

    id= request.form["lid"]
    qry="select * from kudumbasree_complaint where from_id='"+id+"'"
    print(qry)
    db=Db()
    res=db.select(qry)
    return  jsonify(status="ok",data=res)




@app.route("/and_user_sentcomp",methods=['POST'])
def and_user_sentcomp():
    comp=request.form["comp"]
    lid=request.form["lid"]
    klid=request.form['klid']
    qry="insert into kudumbasree_complaint(from_id,complaint,reply,date,status,ksree_lid)values('"+lid+"','"+comp+"','pending',curdate(),'pending','"+klid+"')"
    db=Db()
    db.insert(qry)
    return jsonify(status="ok")



@app.route("/inserintoorder",methods=['POST'])
def inserintoorder():
    db=Db()
    pdid=request.form["pdid"]
    lid=request.form["lid"]
    qty=request.form['qty']
    p=request.form['price']
    ff="select * from product where product_id='"+str(pdid)+"'"
    print(ff)
    ee=db.selectOne(ff)
    m=ee['kudumbasree_id']
    print("------------")
    qry="insert into booking_main(user_id,date,status,amount,kud_lid)values('"+str(lid)+"',curdate(),'pending','0','"+str(m)+"')"
    print(qry)
    vvvv=db.insert(qry)
    qry22 = "insert into booking_sub(book_id,product_id,qty)values('"+str(vvvv)+"','"+pdid+"','"+qry+"')"
    db.insert(qry22)
    return jsonify(status="ok")


@app.route("/and_cust_feedback",methods=['POST'])
def and_cust_feedback():
    comp=request.form["feedback"]
    lid=request.form["lid"]
    qry="insert into feedback(date,fromlid,feedback)values(curdate(),'"+lid+"','"+comp+"')"
    db=Db()
    db.insert(qry)
    return jsonify(status="ok")


@app.route("/raa",methods=['POST'])
def raa():
    comp=request.form["rat"]
    lid=request.form["lid"]
    pid=request.form['pid']
    qry="insert into rating(pid,u_id,rating,date)values('"+pid+"','"+lid+"','"+comp+"',curdate())"
    db=Db()
    db.insert(qry)
    return jsonify(status="ok")


@app.route("/inserintoorder",methods=['POST'])
def insorder():
    pid=request.form["pid"]
    lid=request.form["lid"]
    qty=int(request.form["qty"])
    price=float(request.form["price"])
    qry="insert into order_main(order_date,total_amount,user_id,`order _type`,status) values (now(),'"+str(qty*price)+"','"+lid+"','','pending')"
    db=Db()
    print(qry)
    oid=str(db.insert(qry))
    qry="insert into ordersub (ordermain_id,product_id,quantity) values ('"+oid+"','"+pid+"','"+str(qty)+"')"
    db.insert(qry)
    return jsonify(status="ok")


@app.route("/viewmyorders",methods=['POST'])
def viewmyorders():
    lid=request.form["lid"]

    qry="(select ordersub.product_id,ordersub.quantity,handicraftproduct.product_name,handicraftproduct.product_price,handicrafts.name,handicrafts.contact from handicraftproduct inner join handicrafts on handicrafts.login_id=handicraftproduct.crafts_lid inner join ordersub on ordersub.product_id=handicraftproduct.product_id inner join order_main on order_main.order_main_id=ordersub.ordermain_id where  order_main.user_id='"+lid+"') union (select ordersub.product_id,ordersub.quantity,homebakerproduct.product_name,homebakerproduct.product_price,homebaker.name,homebaker.contact from homebakerproduct inner join homebaker on homebaker.login_id=homebakerproduct.baker_lid inner join ordersub on ordersub.product_id=homebakerproduct.product_id inner join order_main on order_main.order_main_id=ordersub.ordermain_id where  order_main.user_id='"+lid+"')"

    print(qry)
    db=Db()
    res=db.select(qry)

    return jsonify(status="ok",data=res)


@app.route("/myprofile",methods=['post'])
def myprofile():
    lid=request.form["lid"]
    db=Db()
    qry="select name,image,place,post,pin,district,email,contact from users where login_id='"+lid+"'"
    res=db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",data=res)
    else:
        return jsonify(status="no")



@app.route('/and_home_login',methods = ['post'])
def and_home_login():
    email = request.form['name']
    passwrd = request.form['pass']
    print(email,passwrd)
    db = Db()
    res = db.selectOne("select * from login where username='"+email+"' and password = '"+passwrd+"'")
    print(res)
    if res is not None:
            return jsonify(status = "ok",id = res['login_id'],type =res['type'])
    else:
        return jsonify(status="none")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
