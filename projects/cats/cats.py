"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    filter_paragraphs = [p for p in paragraphs if select(p)]
    if k < len(filter_paragraphs):
        return filter_paragraphs[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def about_helper(paragraph):
        paragraph = remove_punctuation(paragraph)
        paragraph = lower(paragraph)
        # 如果不加这一行代码就无法通过测试。split将句子分割并转化为列表
        paragraph = split(paragraph)
        for w in topic:
            if w in paragraph:
                return True
        return False
    return about_helper
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed_words) == 0:
        return 0.0
    cnt = 0
    for i in range(len(typed_words)):
        if i >= len(reference_words):
            break
        if typed_words[i] == reference_words[i]:
            cnt += 1
    return cnt/len(typed_words)*100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    if typed == "":
        return 0.0
    else:
        minute = elapsed/60
        num_word = len(typed)/5
        v = num_word/minute
        return v


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        ind, lowerst = 0, 100
        for i in range(len(valid_words)):
            diff = diff_function(user_word, valid_words[i], limit)
            if diff < lowerst:
                lowerst = diff
                ind = i
        if lowerst <= limit:
            return valid_words[ind]
        else:
            return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    """此题借鉴了github上代码,自身代码有一些案例无法通过"""
    # BEGIN PROBLEM 6
    if limit < 0:
        return 0  # 不一定需要是0，只需要返回的结果比limit大就可以了，因为运行到这一步的时候已经意味着需要修改的字符已经超过了limit，所以就直接返回了limit
    if start == '' or goal == '':
        return len(start) + len(goal)
    elif start[0] == goal[0]:  # 直接判断第一个字符是否相等就不需要再定义一个helper函数
        return shifty_shifts(start[1:], goal[1:], limit)
    else:
        return shifty_shifts(start[1:], goal[1:], limit - 1) + 1
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # 当用递归暴力搜索最优的方式时，可以考虑将所有的选择用递归表示出来。
    if limit < 0:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    elif start == '' or goal == '':
        # BEGIN
        return len(start) + len(goal)
        # END
    elif start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # 如果两个字符相等，则处理后面的字符
        return pawssible_patches(start[1:], goal[1:], limit)
        # END
    else:
        # add_diff 用来计算如果增加字符需要的修改次数 --选择add
        add_diff = pawssible_patches(
            start, goal[1:], limit-1) + 1  # Fill in these lines
        # remove_diff 用来计算删除字符需要修改次数 --选择remove
        remove_diff = pawssible_patches(start[1:], goal, limit-1) + 1
        # substitute_diff 用来计算替换字符需要修改次数 --选择substitute
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1) + 1
        # BEGIN
        "*** YOUR CODE HERE ***"
        # 有增，删，改三种变动策略，应该选择何种策略？ --其实就是用递归暴力搜索，取所有可能性的最小值。
        return min(add_diff, remove_diff, substitute_diff, add_diff+remove_diff, add_diff+substitute_diff, remove_diff+substitute_diff, add_diff+remove_diff+substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    cnt = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            cnt += 1
        else:
            break
    finish_ratio = cnt/len(prompt)
    send({'id': user_id, 'progress': finish_ratio})
    return finish_ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    k = 0
    while (k < len(times_per_player)):
        lst = []
        i = 1
        while (i < len(times_per_player[k])):
            lst.append(times_per_player[k][i]-times_per_player[k][i-1])
            i += 1
        k += 1
        times.append(lst)
    return game(words, times)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game))  # 表示有几个player
                           )  # contains an *index* for each player
    # contains an *index* for each word
    word_indices = range(len(all_words(game)))  # 表示有几个word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # initial return list
    res = []
    for k in player_indices:
        res.append([])
    for i in word_indices:
        # 因为每一个word就要重新开始比较，所以min_time和select_player的初始化要房放在里面。
        min_time = 100
        select_player = 0
        for j in player_indices:
            t = time(game, j, i)
            if (t < min_time):
                min_time = t
                select_player = j
        res[select_player].append(word_at(game, i))
    return res
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]
               ), 'words should be a list of strings'
    assert all([type(t) == list for t in times]
               ), 'times should be a list of lists'
    assert all([isinstance(i, (int, float))
               for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]
               ), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
