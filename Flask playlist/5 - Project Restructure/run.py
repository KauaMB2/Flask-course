from market import app#Get the var "app" inside market/__init__.py

#Checks if the run.py file has executed directly and not imporeted
if __name__=='__main__':
    app.run(debug=True)#Liga o servidor



#http://127.0.0.1:5000/

#Commands for sqlite:
#
#Acessing
# from market import app,db
# app.app_context().push()
# db.create_all()
#
#Show
# from market import Item
# Item.query.all()
#
#Add
# from market import Item
# varName=Item(name="Keyboard",price=150,barcode='231985128446',description='description')
# db.session.add(varName)
# db.session.commit()
#
#Search
# for item in Item.query.filter_by(price=500):
#     item.name
