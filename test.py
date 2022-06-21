from http import client
import json
from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# need to get Boggle instance to use in session

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = 'test'

    def test_home_route(self):
        with app.test_client() as client:
                with client.session_transaction() as change_session:
                    change_session['highscore'] = 10
                    change_session['nplays'] = 15

                res = client.get('/')
                html = res.get_data(as_text = True)

                self.assertEqual(res.status_code, 200)
                self.assertIn('<p>High Score:', html)
                self.assertIn('<b>10</b>', html)
                self.assertIn('in 15 plays', html)


    def test_check_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = board
            res = client.get('/check-word', query_string = {'word': 'me'})
            html = res.get_data(as_text = True)


            self.assertEqual(res.status_code, 200)
            self.assertIn('ok', html)


    def test_post_score(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                # breakpoint()
                change_session['score']= 25
            
            res = client.post('/post-score', json={'score': 25})
            html = res.get_data(as_text = True)

            # breakpoint()

            self.assertEqual(res.status_code, 200)
            self.assertIn('"brokeRecord": true', html)
            


    # const resp = await axios.post("/post-score", { score: this.score });

# @app.route("/post-score", methods=["POST"])
# def post_score():
#     """Receive score, update nplays, update high score if appropriate."""

#     score = request.json["score"]
#     highscore = session.get("highscore", 0)
#     nplays = session.get("nplays", 0)

#     session['nplays'] = nplays + 1
#     session['highscore'] = max(score, highscore)

#     return jsonify(brokeRecord=score > highscore)


# what are build and tear down functions

# test redirects (n/a), POST

board = [['J', 'S', 'D', 'P', 'Z'], ['V', 'E', 'M', 'E', 'N'], ['B', 'S', 'Y', 'L', 'H'], ['N', 'B', 'M', 'S', 'H'], ['M', 'F', 'R', 'N', 'Q']]