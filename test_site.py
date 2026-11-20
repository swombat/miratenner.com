from html.parser import HTMLParser
from pathlib import Path
import unittest
import build

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.links=[]; self.h1=0; self.scripts=0; self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='script': self.scripts+=1
        if tag in ('a','link'): self.links.append(attrs.get('href',''))

class SiteTests(unittest.TestCase):
    def test_pages(self):
        build.build()
        pages=list(build.OUT.rglob('*.html'))
        self.assertEqual(len(pages),8)
        for p in pages:
            doc=Document(p.read_text())
            self.assertEqual(doc.h1,1,p)
            self.assertEqual(doc.scripts,0,p)
            for link in doc.links:
                if link.startswith('/'):
                    dest=build.OUT/link.lstrip('/')
                    self.assertTrue(dest.is_file() or (dest/'index.html').is_file(),link)
    def test_prose_is_preserved(self):
        for slug,title in build.STORIES:
            source=(build.ROOT/'stories'/f'{slug}.md').read_text().split('\n',1)[1].strip()
            rendered=(build.OUT/slug/'index.html').read_text()
            for paragraph in source.split('\n\n'):
                self.assertIn(f'<p>{build.inline(paragraph)}</p>',rendered)
    def test_escaping(self):
        self.assertEqual(build.inline('<script>&'), '&lt;script&gt;&amp;')

if __name__=='__main__': unittest.main()
