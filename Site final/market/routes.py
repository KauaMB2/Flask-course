from market import app
from market.models import Item,User,db
from flask import render_template,redirect,url_for,flash,request
from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm,AddItemForm,CommentItemForm
from flask_login import login_user,logout_user,login_required,current_user
import os
import json

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market',methods=['GET','POST'])
@login_required
def market_page():
    #Purchase Item Logic
    itemsDict=Item.query.filter_by(owner=None)
    dataItem=Item.query.all()
    dataUser=User.query.all()
    commentsList=[]
    nameList=[]
    for data in dataItem:
        try:
            dadoDict=dict(json.loads(data.comm))
            commentsList.append(dadoDict)
            for name in dadoDict.keys():
                nameList.append(name)
        except:
            pass

    lenCommentsList=len(commentsList)
    purchase_form=PurchaseItemForm()
    selling_form=SellItemForm()
    comment_form=CommentItemForm()
    if request.method=="POST":
        purchased_item=request.form.get('purchased_item')
        p_item_object=Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object.price):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$!",category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')
        #Sell Item Logic
        sold_item=request.form.get('sold_item')
        s_item_object=Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} for {s_item_object.price} back to market",category="success")
            else:
                flash(f"Something went wrong with selling {s_item_object.name}!",category="danger")
        comment_item=request.form.get('commented_item')
        C_item_object=Item.query.filter_by(name=comment_item).first()
        if comment_item != None:
            if comment_form.validate_on_submit():
                for i in range(0,lenCommentsList,1):
                    for x in range(0,len(commentsList[i].keys()),1):
                        nameKey=list(commentsList[i].keys())[0]
                        print(nameKey,x,len(commentsList[i].keys()))
                        if nameKey == C_item_object.name:
                            commentsList[i][nameKey][current_user.username]=comment_form.comment_input.data
                            commentReplaced=""
                            for x in str(commentsList[i]):
                                if(x=="\'"):
                                    commentReplaced=commentReplaced+"\""
                                else:
                                    commentReplaced=commentReplaced+x
                            print(commentReplaced)
                            C_item_object.toComment(commentReplaced)
                            break
                        if (x)==len(commentsList[i].keys()):
                            print("gnfgfgnsfgnsfgnsfgnfgnfgnfg")
            flash(f"Congratulations! You commented about {comment_item}",category="success")
        return redirect(url_for('market_page'))
    if request.method=="GET":
        owned_items=Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=itemsDict, purchase_form=purchase_form, owned_items=owned_items,selling_form=selling_form, comment_form=comment_form,comments=commentsList,nameList=nameList,lenCommentsList=lenCommentsList)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}',category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again',category='danger')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out",category='info')
    return redirect(url_for("home_page"))

@app.route('/addItem',methods=['GET','POST'])
@login_required
def addItem_page():
    imgLogo=os.path.join(app.config['UPLOAD_FOLDER'],"logo.png")
    form=AddItemForm()
    if form.validate_on_submit():
        itemToCreate = Item(name=form.name.data,
                              price=form.price.data,
                              barcode=form.barcode.data,
                              description=form.description.data,
                              comm="{\""+str(form.name.data)+"\":"+"{}}")
        db.session.add(itemToCreate)
        db.session.commit()
        flash(f'New item successfully added',category='success')
    if request.method=="POST":
        return redirect(url_for("addItem_page"))
    if request.method=="GET":
        return render_template('addItems.html',form=form,imgLogo=imgLogo)



