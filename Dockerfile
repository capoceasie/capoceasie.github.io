FROM jekyll/jekyll:3.8

ADD . /site

RUN /bin/bash -c "chmod 777 /site/* && ls -al /site"

#RUN bundle install
#RUN gem install public_suffix --version 3.1.1

CMD cd /site && jekyll serve