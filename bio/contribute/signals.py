from django import dispatch

vote_plus_answer = dispatch.Signal(providing_args=['instance', 'user'])
vote_minus_answer = dispatch.Signal(providing_args=['instance', 'user'])
unvote_plus_answer = dispatch.Signal(providing_args=['instance', 'user'])
unvote_minus_answer = dispatch.Signal(providing_args=['instance', 'user'])
accepted_answer = dispatch.Signal(providing_args=['instance', 'user'])
unaccepted_answer = dispatch.Signal(providing_args=['instance', 'user'])
