from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def purchaseOrder():
   return render_template('purchase_order_example.html')
if __name__ == '__main__':
   app.run(debug=True )
