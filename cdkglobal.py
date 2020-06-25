from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/api')
def discount_calculator():
		customer_type  = request.args.get('customer_type', '')
		total_amount = int(request.args.get('total_amount', 0))
		discount = 0

		if customer_type == 'Regular':
			if total_amount > 5000:
				if total_amount >= 10000:
					discount += cal_disc(10000,5000,10)
				else:
					discount += cal_disc(total_amount,5000,10)
			if total_amount > 10000:
				discount += cal_disc(total_amount,10000,20)
		elif customer_type == 'Premium':
			if total_amount < 4000:
				discount += cal_disc(total_amount,0,10)
			else:
				discount += cal_disc(4000,0,10) 
			if total_amount > 4000:
				if total_amount >= 8000:
					discount += cal_disc(8000,4000,15)
				else:
					discount += cal_disc(total_amount,4000,15)
			if total_amount > 8000:
				if total_amount >= 12000:
					discount += cal_disc(12000,8000,20)
				else:
					discount += cal_disc(total_amount,8000,20)
			if total_amount > 12000:
				discount += cal_disc(total_amount,12000,30)
		return render_template('output.html', total_amount=total_amount, 
								pay_amount=total_amount-discount, discount=discount)

def cal_disc(total_amount, slab_min, per):
	return (total_amount-slab_min)*(per/100)

app.run(debug=True)

#http://127.0.0.1:5000/api?customer_type=Regular&total_amount=10000
