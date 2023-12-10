import time
import threading


def counter(function):
    def wrapper(*args, **kwargs):
         start_time = time.time()
         result = function(*args, **kwargs)
         end_time = time.time()
         execution_time = end_time - start_time
         print(function.__name__ + " executed in " + str(execution_time) + " seconds")
         return result
    return wrapper
         
                    
                        
def process_lines(text_lines):
     wordfreq = {}
     for line in text_lines:
        for word in line.split():
            if word not in wordfreq:
                wordfreq[word] = 0
            wordfreq[word] += 1
     return wordfreq



@counter
def count_words_not_multithread(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        return process_lines(lines)




@counter
def count_words_with_multithread(name, count_of_thrads):
    wordfreq = {}
    lock = threading.Lock()

    def process_lines_and_add_to_dictionarie(lines):
        dict_from_lines = process_lines(lines)
        with lock:
            for word, count in dict_from_lines.items():
                wordfreq[word] = wordfreq.get(word, 0) + count

    with open(name, 'r') as file:
        file_lines = file.readlines()

    chunk_size = len(file_lines)
    threads = []


    for i in range(count_of_thrads):
        start = i * chunk_size if i == 0 else i * chunk_size + 1
        end = (i+1) * chunk_size
        lines = file_lines[start:end]

        thread = threading.Thread(target=process_lines_and_add_to_dictionarie, args=(lines,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return wordfreq


count_words_not_multithread("text.txt")
count_words_with_multithread("text.txt", 5)