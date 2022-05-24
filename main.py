import numpy as np

def check_word(word, conditions):
    for i in range(5):
        for cond in conditions[i]:
            if (cond[0] == 0 and cond[1] in word) or (cond[0]==2 and cond[1]!=word[i]) or (cond[0] == 1 and (cond[1] == word[i] or cond[1] not in word)):
                return False
            
    return True

def conditionalWords(words,conditions):
    curr_words = []
    for word in words:
        if(check_word(word, conditions)):
            curr_words.append(word)
    return curr_words

all_configurations = []

def configurations(config = []):
    if(len(config)==5):
        all_configurations.append(config.copy())
        return
    config.append(0)
    configurations(config)
    config.pop()
    config.append(1)
    configurations(config)
    config.pop()
    config.append(2)
    configurations(config)
    config.pop()
    return

def information_gain(words,word,conditions):
    poss_split = []
    for config in all_configurations:
        for i in range(5):
            conditions[i].append((config[i],word[i]))
        l = len(conditionalWords(words,conditions))
        if l>0:
            poss_split.append(l)
        for i in range(5):
            conditions[i].pop() 
    poss_split = np.array(poss_split)
    prob_words_split = poss_split/len(words)
    prob_log = np.log(prob_words_split)
    return -np.sum(prob_words_split*prob_log)


def main():
    all_words = []
    file = open("allowed_words.txt", "r")
    lines = file.readlines()
    for line in lines:
        all_words.append(line.strip())
    configurations()
    conditions = [[] for i in range(5)]
    while True:
        word = input("Enter a word: ")
        config = input("Enter a configuration: ")
        if config=="22222":
            break
        for i in range(5):
            conditions[i].append((int(config[i]),word[i]))
        possible_words = all_words.copy()
        possible_words = conditionalWords(possible_words, conditions)
        answers = []
        count = 0
        print(len(possible_words))
        for word in possible_words:
            answers.append((word,information_gain(possible_words,word,conditions)))
            count += 1
            if count%100 == 0:
                print(count)
        answers = sorted(answers, key=lambda x: x[1], reverse=True)
        print(answers[:10])
if __name__ == "__main__":
    main()
