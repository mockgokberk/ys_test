# Getting Started

Clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/mockgokberk/ys_test.git  
    $ cd ys_test
    
Then

    docker-compose build
    docker-compose up



#Usage

    At first launch a script that is triggered from docker-compose file will 
    auto import some models to test. 

    the main structure is 

    orders.views.SendOrderViewSet -> redis -> listener -> orders.views.OrderViewSet 


    SendOrderViewSet publishes to redis which then the subscriber(Listener) script 
    that runs in a different container gets the pub and posts to the OrderViewSet
    A celery implementation in between would be a better execution since waiting for 
    OrderViewSet to respond is less reliable than queue celery tasks. 

    
    API DOCS : http://0.0.0.0:8000/api/v1/ 
    
    1- Curl request to trigger the SendOrderViewSet which will initiate the chain
    which can be accessed from http://0.0.0.0:8000/api/v1/create_order/

    curl --location --request POST 'http://127.0.0.1:8000/api/v1/create_order/' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=260Y51cSY9Kcgulr74Uh3cJwSrUlvQcVaRsbD0k771Uk56tvIWX4BG5iVd4flV8z' \
    --data-raw '{
        "user":1,
        "address":"testadress",
        "order":1,
        "quantity":"1",
        "status": "preparing"
    }'


    2- Order statuses can be accessed and filtered via
    order endpoint + status parameter for the sake of simplicity i 
    added 10 seconds of delay to process order. a couple post using 
    postman will give enough delay to check order endpoints and statuses.


    3. Also added management command to sub redis for fun purposes :) 
    Decided to go with separate script. 