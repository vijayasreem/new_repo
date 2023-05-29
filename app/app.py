from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate_policy', methods=['POST'])
def validate_policy():
	data = request.get_json()

	sum_assured = data['sum_assured']
	age = data['age']
	annual_income = data['annual_income']
	otp = data['otp']
	policy_tenure = data['policy_tenure']

	if sum_assured < 50000 or sum_assured > 200000:
		return jsonify({"message": "Sum assured is not in range."}), 400

	if age < 18 or age > 55:
		return jsonify({"message": "Age not in range."}), 400

	if annual_income < 40000:
		return jsonify({"message": "Income not eligible"}), 400

	if policy_tenure not in [12, 15, 18, 24]:
		return jsonify({"message": "Policy tenure not in range"}), 400

	if otp == None:
		return jsonify({"message": "OTP authentication failed"}), 400

	return jsonify({"message": "Validation successful"})

if __name__ == '__main__':
	app.run(debug=True)