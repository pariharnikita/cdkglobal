from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/api')
def calculate_discount():
		customer_type  = request.args.get('customer_type', '')
		total_amount = int(request.args.get('total_amount', 0))
		discount = 0

		if customer_type == 'Regular':
			if total_amount > 5000:
				if total_amount >= 10000:
					discount += (10000-5000)*(10/100)
				else:
					discount += (total_amount-5000)*(10/100)
			if total_amount > 10000:
				discount += (total_amount-10000)*(20/100)
		elif customer_type == 'Premium':
			if total_amount < 4000:
				discount += total_amount*(10/100)
			else:
				discount += 4000*(10/100)  
			if total_amount > 4000:
				if total_amount >= 8000:
					discount += (8000-4000)*(15/100)
				else:
					discount += (total_amount-4000)*(15/100)
			if total_amount > 8000:
				if total_amount >= 12000:
					discount += (12000-8000)*(20/100)
				else:
					discount += (total_amount-8000)*(20/100)
			if total_amount > 12000:
				discount += (total_amount-12000)*(30/100)
		return render_template('output.html', total_amount=total_amount, 
								pay_amount=total_amount-discount, discount=discount)

app.run(debug=True)

#http://127.0.0.1:5000/api?customer_type=Regular&total_amount=10000
