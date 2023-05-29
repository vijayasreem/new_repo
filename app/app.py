from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/validate_user', methods=['POST'])
def validate_user():
    data = request.get_json()
    min_sum_assured = data['min_sum_assured']
    max_sum_assured = data['max_sum_assured']
    min_age_limit = data['min_age_limit']
    max_age_limit = data['max_age_limit']
    annual_income = data['annual_income']
    sum_assured_ranges = data['sum_assured_ranges']
    policy_tenure_ranges = data['policy_tenure_ranges']
    spouse_eligibility = data['spouse_eligibility']
    otp_authentication = data['otp_authentication']
    response = {}
    if min_sum_assured > max_sum_assured:
        response["error"] = "min_sum_assured cannot be greater than max_sum_assured"
    elif min_age_limit > max_age_limit:
        response["error"] = "min_age_limit cannot be greater than max_age_limit"
    elif annual_income < 40000:
        response["error"] = "annual_income cannot be less than 40000"
    elif sum_assured_ranges not in [50000, 100000, 150000, 200000]:
        response["error"] = "sum_assured_ranges must be one of [50000, 100000, 150000, 200000]"
    elif policy_tenure_ranges not in [12, 15, 18, 24]:
        response["error"] = "policy_tenure_ranges must be one of [12, 15, 18, 24]"
    elif not spouse_eligibility:
        response["error"] = "spouse_eligibility cannot be false"
    elif not otp_authentication:
        response["error"] = "otp_authentication cannot be false"
    else:
        response["status"] = "success"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)