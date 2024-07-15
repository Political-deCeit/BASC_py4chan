import basc_py4chan as py4chan


url = "https://archived.moe/b/thread/754027582/"
# url = "https://boards.4chan.org/pw/thread/15236618#q15236618/"
parts = py4chan.get_4chan_url_parts(url)

board = py4chan.Board(parts["board"], domain=parts["domain"])
thread = board.get_thread(parts["thread_id"])
posts = thread.posts
print(thread)