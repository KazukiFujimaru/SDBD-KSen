import os
import json
from flask import render_template, request, jsonify
from modules import modules

def configure_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/testpg")
    def testpg():
        return render_template("testpg.html")
    
    @app.route("/elements")
    def elements():
        return render_template("elements.html")
    
    @app.route("/materi/p1")
    def pertemuan1():
        return render_template("materi1.html")
    
    @app.route("/materi/p2")
    def pertemuan2():
        return render_template("materi2.html")
    
    @app.route("/materi/p3")
    def pertemuan3():
        return render_template("materi3.html")
    
    @app.route("/test2")
    def test2():
        return render_template("testpg2.html")
    
    @app.route("/materi")
    def materipage():
        return render_template("materi.html")
    
    @app.route("/materi/p4")
    def pertemuan4():
        return render_template("materi4.html")
    
    @app.route("/materi/p5")
    def pertemuan5():
        return render_template("materi5.html")
    
    @app.route("/materi/p6")
    def pertemuan6():
        return render_template("materi6.html")
    
    @app.route("/materi/p7")
    def pertemuan7():
        return render_template("materi7.html")
    
    @app.route("/materi/p8")
    def pertemuan8():
        return render_template("materi8.html")
    
    @app.route('/pesan')
    def halaman_cek_pesan():
        return render_template('cek_pesan.html')

    @app.route('/api/cek_pesan', methods=['POST'])
    def api_cek_pesan():
        req_data = request.get_json()
        if not req_data or 'npm' not in req_data or 'nilai' not in req_data:
            return jsonify({'error': 'Permintaan tidak valid. Data tidak lengkap.'}), 400

        npm_input = req_data['npm']
        nilai_input = req_data['nilai']

        try:
            student_data_json = os.environ.get('STUDENT_DATA')
            if not student_data_json:
                print("ERROR: Environment Variable 'STUDENT_DATA' tidak ditemukan.")
                return jsonify({'error': 'Kesalahan konfigurasi pada server.'}), 500
            
            student_list = json.loads(student_data_json)

            # LOGIKA DIKEMBALIKAN: Memeriksa 'npm' dan 'nilai'
            for student in student_list:
                # Menggunakan str() untuk memastikan perbandingan tipe data string vs string
                if student.get('npm') == npm_input and str(student.get('nilai')) == nilai_input:
                    return jsonify({'pesan': student.get('pesan')})

            return jsonify({'error': 'NPM atau Nilai salah. Silakan periksa kembali.'}), 401

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return jsonify({'error': 'Terjadi kesalahan internal.'}), 500