FROM jekyll/jekyll:3.5

ADD . /site

CMD cd /site && jekyll serve