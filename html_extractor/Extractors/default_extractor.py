from cmoncrawl.processor.pipeline.extractor import BaseExtractor
from cmoncrawl.common.types import PipeMetadata
from bs4 import BeautifulSoup

HTML_TAGS = {'a',
 'abbr',
 'address',
 'area',
 'article',
 'aside',
 'audio',
 'b',
 'base',
 'bdi',
 'bdo',
 'blockquote',
 'body',
 'br',
 'button',
 'canvas',
 'caption',
 'cite',
 'code',
 'col',
 'colgroup',
 'data',
 'datalist',
 'dd',
 'del',
 'details',
 'dfn',
 'dialog',
 'div',
 'dl',
 'dt',
 'em',
 'embed',
 'fieldset',
 'figcaption',
 'figure',
 'footer',
 'form',
 'h1',
 'h2',
 'h3',
 'h4',
 'h5',
 'h6',
 'head',
 'header',
 'hgroup',
 'hr',
 'html',
 'i',
 'iframe',
 'img',
 'input',
 'ins',
 'kbd',
 'keygen',
 'label',
 'legend',
 'li',
 'link',
 'main',
 'map',
 'mark',
 'menu',
 'menuitem',
 'meta',
 'meter',
 'nav',
 'noscript',
 'object',
 'ol',
 'optgroup',
 'option',
 'output',
 'p',
 'param',
 'picture',
 'pre',
 'progress',
 'q',
 'rb',
 'rp',
 'rt',
 'ruby',
 's',
 'samp',
 'script',
 'section',
 'select',
 'small',
 'source',
 'span',
 'strong',
 'style',
 'sub',
 'summary',
 'sup',
 'svg',
 'table',
 'tbody',
 'td',
 'template',
 'textarea',
 'tfoot',
 'th',
 'thead',
 'time',
 'title',
 'tr',
 'track',
 'u',
 'ul',
 'var',
 'video',
 'wbr'}

class DefaultExtractor(BaseExtractor):
   def __init__(self):
      # you can force a specific encoding if you know it
      super().__init__(encoding=None)

   def preprocess_text(self, text: str) -> str:
      # remove multiple spaces
      text = ' '.join(text.split())
      # remove newlines
      text = text.replace('\n', ' ')
      return text

   def extract_soup(self, soup: BeautifulSoup, metadata: PipeMetadata):
      # here you can extract the data you want from the soup
      # and return a dict with the data you want to save
      d = dict()
      doc_tags = soup.find_all()
      tag_counter = 0
      for tag in doc_tags:
         contents = self.preprocess_text(tag.getText().strip())
         if len(contents) > 5 \
         and tag.name in HTML_TAGS:
            d[f'tag_{tag_counter}'] = {"tag" : tag.name, "contents" : contents}
            tag_counter += 1
      return d

   # You can also override the following methods to drop the files you don't want to extracti
   # Return True to keep the file, False to drop it
   def filter_raw(self, response: str, metadata: PipeMetadata) -> bool:
      return True
   def filter_soup(self, soup: BeautifulSoup, metadata: PipeMetadata) -> bool:
      return True

# Make sure to instantiate your extractor into extractor variable
# The name must match so that the framework can find it
extractor = DefaultExtractor()