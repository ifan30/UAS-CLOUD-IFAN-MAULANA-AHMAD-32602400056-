import uuid
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from core.database import CV_DATABASE
from core.services import S3SimulationService

cv_bp = Blueprint('cv', __name__)

@cv_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('auth.index'))
    
    total_cv = len(CV_DATABASE)
    total_s1 = sum(1 for cv in CV_DATABASE if "S1" in cv['pendidikan'])
    
    return render_template('dashboard.html', 
                           username=session['user'], 
                           total_cv=total_cv, 
                           total_s1=total_s1)

@cv_bp.route('/create-cv', methods=['GET', 'POST'])
def create_cv():
    if 'user' not in session:
        return redirect(url_for('auth.index'))
        
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        hp = request.form.get('hp')
        pendidikan = request.form.get('pendidikan')
        tema = request.form.get('tema')
        
        file_name = f"cv_{nama.lower().replace(' ', '_')}.txt"
        path_txt_s3 = f"plaintext-hasil-jadi/{file_name}"
        
        data_cv = {'nama': nama, 'email': email, 'hp': hp, 'pendidikan': pendidikan, 'tema': tema}
        S3SimulationService.save_cv_object(file_name, path_txt_s3, data_cv)
            
        cv_id = str(uuid.uuid4())
        CV_DATABASE.append({
            'id': cv_id,
            'nama': nama,
            'pendidikan': pendidikan,
            'tema': tema,
            'path_pdf_s3': path_txt_s3,
            'local_filename': file_name
        })
        
        flash('Berhasil melakukan kompilasi & upload objek ke AWS S3 bucket!', 'success')
        return redirect(url_for('cv.list_cv'))
        
    return render_template('create_cv.html')

@cv_bp.route('/list-cv')
def list_cv():
    if 'user' not in session:
        return redirect(url_for('auth.index'))
        
    search_query = request.args.get('search', '')
    filtered_cv = CV_DATABASE
    
    if search_query:
        filtered_cv = [
            cv for cv in CV_DATABASE 
            if search_query.lower() in cv['nama'].lower() or search_query.lower() in cv['pendidikan'].lower()
        ]
        
    return render_template('list_cv.html', cv_list=filtered_cv, search_query=search_query)

@cv_bp.route('/download/<cv_id>')
def download_cv(cv_id):
    if 'user' not in session:
        return redirect(url_for('auth.index'))
        
    target_cv = next((cv for cv in CV_DATABASE if cv['id'] == cv_id), None)
    if target_cv:
        content = S3SimulationService.read_cv_object(target_cv['local_filename'])
        if content:
            return content, 200, {'Content-Type': 'text/plain; charset=utf-8'}
            
    flash('File objek S3 tidak ditemukan!', 'danger')
    return redirect(url_for('cv.list_cv'))

@cv_bp.route('/delete/<cv_id>')
def delete_cv(cv_id):
    if 'user' not in session:
        return redirect(url_for('auth.index'))
        
    global CV_DATABASE
    target_cv = next((cv for cv in CV_DATABASE if cv['id'] == cv_id), None)
    
    if target_cv:
        S3SimulationService.delete_cv_object(target_cv['local_filename'])
        # Modifikasi list in-place karena manipulasi global blueprint
        CV_DATABASE[:] = [cv for cv in CV_DATABASE if cv['id'] != cv_id]
        flash('Objek berhasil dihapus secara permanen dari bucket AWS S3!', 'success')
        
    return redirect(url_for('cv.list_cv'))