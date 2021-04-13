# MongoDB API
## TO RUN THE API IN YOUR SYSTEM BY DOCKER:
 1. Clone the Greendeck_task_1 repository
 2. Move to 'Greendeck Task1' directory.
 3. Build Docker image by running the following command "$ docker build -t my_docker_flask:latest . "
 4. You can run the build you just created with the docker run command. "$ docker run -d -p 5000:5000 my_docker_flask:latest"
 5. Now you can access the API using curl
## USING THE API:
  1. TO READ ALL RECORDS FROM DATABASE  $ curl -X GET http://127.0.0.1:5000/read_all 
  2. TO READ ONE RECORD THAT MATCHES ONE KEY VALUE PAIR  $ curl -X GET http://127.0.0.1:5000/read_one/<argument>/<value> 
     example: $ curl -X GET http://127.0.0.1:5000/read_one/brand_name/jellycat
  3. TO INSERT ONE RECORD IN DATABASE  $ curl -X GET         http://127.0.0.1:5000/create/<name>/<brand_name>/<regular_price_value>/<offer_price_value>/<currency>/<classification_l1>/<classification_l2>/<classification_l3>/<classification_l4>/<image_url>/
     example: curl -X GET http://127.0.0.1:5000/create/name_trial2/brand_name_trial2/regular_price_value_trial2/offer_price_value_trial2/currency_trail2/classification_l1_trail2/classification_l2_trail2/classification_l3_trial2/classification_l4_trail2/image_url2/ 
  4. TO UPDATE ONE key-value PAIR TO ANOTHER element-updateValue pair $ curl -X GET http://127.0.0.1:5000/update/<key>/<value>/<element>/<updateValue>/ 
     example $ curl -X GET http://127.0.0.1:5000/update/name/name_trial2/name/name_updated/
  5. TO DELETE ONE RECORD HAVING ONE key-value PAIR $ curl -X GET http://127.0.0.1:5000/delete_one/<key>/<value>
     example $ curl -X GET http://127.0.0.1:5000/delete_one/brand_name/brand_name_trial2
 6. TO DELETE ALL RECORDS HAVING MATCHING key-value PAIR $ curl -X GET http://127.0.0.1:5000/delete_many_match/<key>/<value> 
     example $ curl -X GET http://127.0.0.1:5000/delete_many_match/brand_name/jellycat
 7. TO DELETE ALL PRESENT RECORDS  $ curl -X GET http://127.0.0.1:5000/delete_all_records

