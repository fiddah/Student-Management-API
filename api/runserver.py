<<<<<<< HEAD
from api import create_app
from api.config.config import config_dict

app = create_app(config=config_dict['prod'])

if __name__=="__main__":
=======
from api import create_app
from api.config.config import config_dict

app = create_app(config=config_dict['prod'])

if __name__=="__main__":
>>>>>>> 2f7b994f2efb5cd9ccc95976fe27afa5bbd6c73d
    app.run(debug=True)