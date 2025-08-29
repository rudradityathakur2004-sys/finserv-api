from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "rudraditya_thakur"
DOB = "21082004"
EMAIL = "rudradityathakur2004@gmail.com"
ROLL_NUMBER = "22BCE1396"

def process_data(data):
    even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
    num_sum, alpha_concat = 0, []

    for item in data:
        if item.isdigit():
            num = int(item)
            (even_numbers if num % 2 == 0 else odd_numbers).append(item)
            num_sum += num
        elif item.isalpha():
            alphabets.append(item.upper())
            alpha_concat.append(item)
        else:
            special_chars.append(item)

    concat_string = ""
    toggle = True
    for ch in "".join(alpha_concat)[::-1]:
        concat_string += ch.upper() if toggle else ch.lower()
        toggle = not toggle

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(num_sum),
        "concat_string": concat_string
    }

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        req = request.get_json()
        if not req or "data" not in req:
            return jsonify({"is_success": False, "error": "Invalid input"}), 400
        return jsonify(process_data(req["data"])), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
