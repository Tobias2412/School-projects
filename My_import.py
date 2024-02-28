def read_answers():
    magic_responses_opened = open(r'8_ball_responses.txt', 'r+')
    responses = magic_responses_opened.read()
    magic_responses_opened.close()
    return responses.splitlines()