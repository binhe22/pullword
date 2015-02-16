#Pullword
A Python package for [pullword.com] (http://pullword.com). 

#Install
``` 
pip install pullword 
or 
easy_install pullword 
```

#Usage
```
from pullword import pullword 
word_list = pullword(u"华中科技大学")
wrod_list = pullword(u"华中科技大学", debug=0)
word_list = pullword(u"华中科技大学", threshold=0.7)
```
##input
source:a paragraph of chinese words， *must be unicode*. for example:
```
pullword(u"华中科技大学")
pullword(source=u"华中科技大学")
```
debug:debug=0, debug model is off; debug=1, debug mode in on(show all probabilities of each word)
threshold: must be [0-1]

##output
function pullword will return a list.

if debug = 0, it will return a list of words;
```
[u'华中,u'华中科技'...]
```
if debug = 1, it will return a list of a list of word and probability.
```
[[u'华中', 0.755862],[u'华中科技', 0.815004]...]
```


