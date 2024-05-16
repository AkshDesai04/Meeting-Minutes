import temp

def manual_cleanup(list, word_count = 5):
    print('original', list)
    filler_words = ['Um', 'Uh', 'Er', 'Like', 'Well', 'You know', 'So', 'Anyway', 'I mean', 'Actually', 'Basically', 'Literally', 'Kind of', 'Sort of', 'Right', 'Exactly', 'Right', 'Yeah', 'Mhmm', 'Hmm', 'Thank You', 'Thank You So Much', 'Thank You Very Much']
    list = remove_small_sentences(list, word_count)
    print('removed small sentences', list)
    list = remove_filler(list, filler_words, 0.5)
    print('removed fillers', list)
    return list

def remove_small_sentences(list, word_count):
    list = [item for item in list if len(item['text'].split()) >= word_count]
    return list

def remove_filler(list, fillers, filler_percentage = 0.5):
    list = [item for item in list if not any(filler in item['text'].split() for filler in fillers) and len(item['text'].split()) >= len(item['text'].split()) * (1 - filler_percentage)]
    return list

manual_cleanup(temp.ingest_target('test.txt'))