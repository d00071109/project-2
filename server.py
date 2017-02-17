from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json

class HelloHandler(BaseHTTPRequestHandler):

	def do_GET(self):

		if self.path == "/recipes":
			self.handleRecipeList()

		else:
			self.handle404()


	def handle404(self):
		self.send_response(404)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes("<strong> 404 NOT FOUND </strong>", 'utf-8'))


	def do_POST(self):
		if self.path == "/recipes":
			self.handleRecipeCreate()

		else:
			self.handle404()


	def handleRecipeList(self):


		# my_data = ['1 lb mozzerella cheese', '1 lb colby jack cheese', '1/2 lb lasagna noodles', '5 cups marinara', '2 lbs spicy italian sausage']
		read_in = self.readFile()
		json_string = json.dumps(read_in)

		# print ('JSON: ', json_string)

		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', "*")
		self.send_header('Content-Type', 'application/json')
		self.end_headers()
		self.wfile.write(bytes(json_string, 'utf-8'))
		return

	def handleRecipeCreate(self):

		length = self.headers['Content-Length']
		length = int(length)

		body = self.rfile.read(length).decode('utf-8')
		data = parse_qs(body)
		# print(body)

		message = data['ingredients'][0]
		fin = open('recipes.txt', 'a')
		fin.write(message + '\n')
		fin.close()
		# saveFile(message)
		print(message)

		self.send_response(201)
		self.send_header('Access-Control-Allow-Origin', "*")
		self.end_headers()
		return


	def readFile(self):
		fin = open('recipes.txt', 'rt')
		recipe_list = fin.readlines()
		fin.close()
		return recipe_list
		# try:

		# 	sendResponse = False
		# 	if self.path.endswith(".html"):
		# 		filetype = 'text/html'
		# 		sendResponse = True

		# 	if sendResponse == True:

		# 		f = open(self.path)
		# 		self.send_response(200)
		# 		self.send_header('Content-type', filetype)
		# 		self.end_headers()
		# 		self.wfile.write(f.read())
		# 		f.close()
		# 	return

		# except IOError:
		# 	self.send_error(404, 'File Not Found: %s' % self.path)

	# def do_POST(self):
	# 	if self.path == "/send.html":
	# 		form = cgi.FieldStorage(fp = self.rfile, headers = self.headers, environ = {'REQUEST_METHOD' : 'POST', 'CONTENT_TYPE': self.headers['Content-Type'],})
	# 		print("Ingredient: %s " % form['Ingredient'].value)
	# 		self.send_response(201)
	# 		self.end_headers()
	# 		self.wfile.write(bytes("Ingredient added to Recipe %s " % form['Ingredient'].value), 'utf-8')
	# 	return

def main():
	listen = ("127.0.0.1", 8080)
	server = HTTPServer(listen, HelloHandler)
	print("Listening...")
	server.serve_forever()

main()
