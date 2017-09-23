print("************* What Do you love (Implementation) *****************")
import urllib
def read_text():
	quotes = open("movie_quotes.txt")
	contents = quotes.read()
	print(contents)
	quotes.close()
	check_profanity(contents)
##
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	#print(output) # false->no curse word, if True -> curse word present
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This Documents has No Curse Words")
	else:
		print("Couldn't scan document")
read_text()
