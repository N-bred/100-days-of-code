from api import get_questions


URL = "https://opentdb.com/api.php"

question_data = get_questions(URL, amount=9, type="boolean")
