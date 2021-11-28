## IMPORT THE FLASK LIBRARY 
from flask import Flask, render_template, request

### CREATE A FLASK CLASS 
app = Flask(__name__)

# create a route
@app.route('/')
def hello_world():
    return 'Hello world'



# # class Booboo():
# #       def __init__(self):
# #           print("hi from booboo")

# # boo = Booboo()

# @app.route('/')
# def hello_world():
#     return 'Hello world'


# @app.route('/fu')
# def fu_world():
#     return 'fu'

# ### SAMPLE ROUTE 
# @app.route('/smarty_dodo')
# def smarty():
#     return 'dodos'

# @app.route('/sean')
# def seano():
#     return render_template('sean.html')

# @app.route('/echo')
# def grunpy():
#     return render_template('echo.html')


# @app.route('/two_plus_four')
# def sarty():
#     result = 2 + 4
#     return str(result)

# @app.route('/double_me',methods = ['POST', 'GET'])
# def double():
#    if request.method == 'POST':
#       result = int(request.form['nm'])
#       print(result)
#       result = result*2
#       return ("your number doubled is: " + str(result))
#    else:
#        return render_template('number_form.html')


# @app.route('/add_me',methods = ['POST', 'GET'])
# def add():
#    if request.method == 'POST':
#       result1 = int(request.form['nm1'])
#       print(result1)
#       result2 = int(request.form['nm2'])
#       print(result2)
#       result = result1 + result2
#       return ("your numbers add up is: " + str(result))
#    else:
#        return render_template('add_me.html')

# @app.route('/triple_me',methods = ['POST', 'GET'])
# def triple():
#    if request.method == 'POST':
#       result1 = int(request.form['nm1'])
#       print(result1)
#       result2 = int(request.form['nm2'])
#       print(result2)
#       result = (result1 + result2)*3
#       return render_template('triple_me_result.html', my_result = result, my_list = [result1, result2])
#    else:
#        return render_template('triple_me_form.html')


# ### START tHE APP 
# app.run(host='0.0.0.0', port=5000)










