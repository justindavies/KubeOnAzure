# Use the barebones version of Ruby 2.2.3.
FROM ruby:2.2.3-slim

# Optionally set a maintainer name to let people know who made this image.
MAINTAINER Justin Davies 

# Install dependencies:
# - build-essential: To ensure certain gems can be compiled
# - nodejs: Compile assets
# - libpq-dev: Communicate with postgres through the postgres gem
# - postgresql-client-9.4: In case you want to talk directly to postgres
RUN apt-get update && apt-get install -qq -y build-essential nodejs libsqlite3-dev --fix-missing --no-install-recommends

# Set an environment variable to store where the app is installed to inside
# of the Docker image.
ENV INSTALL_PATH /kubeglobal
RUN mkdir -p $INSTALL_PATH

# This sets the context of where commands will be ran in and is documented
# on Docker's website extensively.
WORKDIR $INSTALL_PATH

# Ensure gems are cached and only get updated when they change. This will
# drastically increase build times when your gems do not change.
COPY Gemfile Gemfile
RUN bundle install

EXPOSE 8080

# Copy in the application code from your work station at the current directory
# over to the working directory.
COPY . .

# Provide dummy data to Rails so it can pre-compile assets.
RUN bundle exec rake RAILS_ENV=production SECRET_TOKEN=pickasecuretoken assets:precompile

# The default command that gets ran will be to start the Unicorn server.
CMD bundle exec unicorn -E production -c config/unicorn.rb

