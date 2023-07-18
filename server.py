from flask import Flask
import random

random_number = random.randint(1, 9)
print(random_number)
app = Flask(__name__)


def h_1(function):
    def wrapper():
        return "<h1 style='text-align: center'>" + function() + "</h1>"
    return wrapper


@app.route('/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    if post_id < random_number:
        return f'<h1><p>{post_id} is too low, try again!</p></h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="30%">'
    elif post_id == random_number:
        return f'<h1><p>{post_id} is right, you found me!</p></h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="30%">'
    else:
        return f'<h1><p>{post_id} is too high, try again!</p></h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="30%">'


@app.route("/")
@h_1
def start():
    return "<p>Guess a number between 0 and 9</p>"\
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='30%'>"


if __name__ == "__main__":
    app.run(debug=True)