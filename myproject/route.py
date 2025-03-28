from flask import render_template,redirect,url_for
from myproject import app  # ✅ Correct import
from myproject.models import Item,User  # ✅ Correct import
from myproject.forms import Registerform
from myproject import db                    
                        
@app.route('/')
@app.route('/home')
def home_page():
       return render_template('home.html')

@app.route('/market')
def market_page():
      items=Item.query.all()
      return render_template('market.html', items= items)

@app.route('/register', methods=['GET','POST'])
def register_page():
       form = Registerform()
       if form.validate_on_submit():
              user_to_create=User(username=form.username.data,
                                  email_address=form.email_address.data,
                                  password_hash=form.password.data)
              db.session.add(user_to_create)
              db.session.commit()
              return redirect(url_for('market_page'))
       return render_template('register.html', form=form)