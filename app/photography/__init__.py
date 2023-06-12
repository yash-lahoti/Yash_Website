from flask import Blueprint, render_template

photography_blueprint = Blueprint("photography", __name__,
                                  template_folder='templates/photography',
                                  static_folder='static/',
                                  static_url_path='photography/static')

@photography_blueprint.route('/photography.html/')
def photohome():
    print('hi')
    return render_template('photo_home.html')