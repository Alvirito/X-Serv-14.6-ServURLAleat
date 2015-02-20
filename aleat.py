#!/usr/bin/python
import webapp
import random


class aleat(webapp.webApp):

 def process(self, parsedRequest):
   num_al = random.randrange(99999)
   return("200 OK", "<html><body><h1>Hola Mundo!</h1>" +
          "<a href='" + str(num_al) + "'>Dame otra!</a>" +
          "</body></html>" +
          "\r\n")
if __name__ == "__main__":
  testWeb=aleat("localhost",1234)