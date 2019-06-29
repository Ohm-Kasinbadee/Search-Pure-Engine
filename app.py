import os
from flask import Flask, render_template, request, url_for
import Index
import hashing
import wildcards
import TF_IDFCosineSimilarityRanking

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result' ,methods = ['POST', 'GET'])
def results():
   if request.method == 'POST':
      	result = request.form['Name']
      	Inverted = Index.InvertedIndex(result)
      	Position = Index.PositionIndex(result)
      	hash = hashing.hashIndex(result)
      	wildcard = wildcards.WildCardsearch(result)
      	Ranking = TF_IDFCosineSimilarityRanking.readfile(result)

      	return render_template("result.html", result = result, test = '10'
      							,Inverted_time = Inverted[1] ,Inverted_cpu = Inverted[6] , Inverted_memory = Inverted[7], Inverted_disk = Inverted[8] 
      							,Position_time = Position[3],Position_cpu = Position[4], Position_memory = Position[5], Position_disk = Position[6]
      							,hash_time = hash[2],hash_cpu = hash[3], hash_memory = hash[4], hash_disk = hash[5]
      							,Ranking_time = Ranking[2],Ranking_cpu = Ranking[3], Ranking_memory = Ranking[4], Ranking_disk = Ranking[5]
      							,wildcard_time = wildcard[2], wildcard_cpu = wildcard[3], wildcard_memory = wildcard[4], wildcard_disk = wildcard[5])

@app.route('/result/resultReturn/<Input>', methods = ['POST', 'GET'])
def resultReturn(Input):
	result = Input
	Inverted = Index.InvertedIndex(result)
	Position = Index.PositionIndex(result)
	hash = hashing.hashIndex(result)
	wildcard = wildcards.WildCardsearch(result)
	Ranking = TF_IDFCosineSimilarityRanking.readfile(result)

	return render_template("result.html", result = result, test = '10'
      							,Inverted_time = Inverted[1] ,Inverted_cpu = Inverted[6] , Inverted_memory = Inverted[7], Inverted_disk = Inverted[8] 
      							,Position_time = Position[3],Position_cpu = Position[4], Position_memory = Position[5], Position_disk = Position[6]
      							,hash_time = hash[2],hash_cpu = hash[3], hash_memory = hash[4], hash_disk = hash[5]
      							,Ranking_time = Ranking[2],Ranking_cpu = Ranking[3], Ranking_memory = Ranking[4], Ranking_disk = Ranking[5]
      							,wildcard_time = wildcard[2], wildcard_cpu = wildcard[3], wildcard_memory = wildcard[4], wildcard_disk = wildcard[5])

@app.route('/result/invertedIndex/<Input>', methods = ['POST', 'GET'])
def invertedIndex(Input):
	result = Input
	results = Index.InvertedIndex(result)
	return render_template('InvertedIndex.html', result = result, count_result_Url = len(results[4]),result_Url = results[0],timeAll = results[1],Time_Url = results[5], Inverted_cpu = results[6], Inverted_memory = results[7], Inverted_disk = results[8] )

@app.route('/result/positionIndex/<Input>', methods = ['POST', 'GET'])
def positionIndex(Input):
	result = Input
	Position = Index.PositionIndex(result)
	return render_template("PositionIndex.html",result = result, Len_PositionIndex_Result_Input = len(Position[0]),PositionIndex_Result_KeyValue = Position[0], PositionIndex_Result_Input = Position[1], PositionIndex_Result_URL = Position[2], TimeAll = Position[3], Position_cpu = Position[4], Position_memory = Position[5], Position_disk = Position[6])
	# return render_template("PositionIndex.html", result = result)

@app.route('/result/BinarySearch/<Input>', methods = ['POST', 'GET'])
def BinarySearch(Input):
	result = Input
	results = Index.InvertedIndex(result)
	return render_template('BinarySearch.html', result = result ,count_result_Url = len(results[4]) ,result_Url = results[0] ,timeAll = results[1] ,counAllLoop = results[2], countLoop = results[3],Time_Url = results[5], Inverted_cpu = results[6], Inverted_memory = results[7], Inverted_disk = results[8] )

@app.route('/result/Hashing/<Input>', methods = ['POST', 'GET'])
def Hashing(Input):
	result = Input
	results = hashing.hashIndex(result)
	return render_template('Hashing.html', result = result, len_hashing = len(results[1]), result_dict = results[0], result_Url = results[1], timeAll = results[2],hash_cpu = results[3], hash_memory = results[4], hash_disk = results[5])

@app.route('/result/wildcard/<Input>', methods = ['POST', 'GET'])
def wildcard(Input):
	result = Input
	results = wildcards.WildCardsearch(result)
	return render_template('wildcard.html', result = result, lenFound = len(results[1]), Found = results[0], url = results[1], timeAll = results[2], wildcard_cpu = results[3], wildcard_memory = results[4], wildcard_disk = results[5])

@app.route('/result/Ranking/<Input>', methods = ['POST', 'GET'])
def Ranking(Input):
	result = Input
	results = TF_IDFCosineSimilarityRanking.readfile(result)
	return render_template('TF_IDFCosineSimilarityRanking.html', result = result, len_Ranking = len(results[1]), tokens = results[0], Ranking = results[1], timeAll = results[2],Ranking_cpu = results[3], Ranking_memory = results[4], Ranking_disk = results[5], Score = results[6])


if __name__ == '__main__':
   app.run(debug = True)
   # app.debug = True
   # app.run(host='0.0.0.0', port = 80)