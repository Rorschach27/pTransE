from gensim.corpora import WikiCorpus
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
inp = os.path.join(dir_path, 'eswiki-20180301-pages-articles1.xml-p5p229076.bz2')
outp = os.path.join(dir_path, 'wiki2')
wiki = WikiCorpus(inp, lemmatize=False)
output = open(outp,mode='w', encoding='utf_32')
for text in wiki.get_texts():
    outText = ' '.join(text) + '\n'
    output.write(outText)
output.close()