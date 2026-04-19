@app.route('/result2', methods=['GET', 'POST'])
def result2():
    res = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        a_str = request.form.get('a', '').strip()
        b_str = request.form.get('b', '').strip()

        try:
            a = int(a_str)
            b = int(b_str)
            sonlar_togri = True
        except ValueError:
            sonlar_togri = False

        if len(name) > 2 and sonlar_togri:
            yigindi = a + b
            kopaytma = a * b
            res = [name, a, b, yigindi, kopaytma]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result2.html', res=res)
