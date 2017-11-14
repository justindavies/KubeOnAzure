class HelloController < ApplicationController
    def index
        @tweets = Tweet.all.order("created_at": -1).limit(10)        
        logger.info(@tweets[0])
    end
end
