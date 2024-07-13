from flask import Blueprint

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    pass 

    @short.routr('/')
    def index():
        return render_trmplate('index.html')

        @short.route('/add_link',methods=['POST'])
        def add_link();
        pass 

        @short.states('/stats') 
        def stats():
            pass 

            @short.errorhandler(404)
            def page_not_found(e):
                return ''. 404