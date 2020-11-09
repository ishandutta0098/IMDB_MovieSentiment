class Tokenizer:
  
  def clean(self, text):

      #Remove HTML Tags
      no_html = BeautifulSoup(text).get_text()
      
      #Filter Letters and Space
      clean = re.sub("[^a-z\s]+", " ", no_html, flags=re.IGNORECASE)
      
      #Replace Excessive Spacing with Single Space
      return re.sub("(\s+)", " ", clean)
 
  def tokenize(self, text):
      clean = self.clean(text).lower()

      #Remove Stopwords
      stopwords_en = stopwords.words("english")
      return [w for w in re.split("\W+", clean) if not w in stopwords_en]
