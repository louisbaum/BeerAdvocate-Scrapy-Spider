# BeerAdvocate-Scrapy-Spider
Scrapy Spider to aquire individual reviews from BeerAdvocate

To run download scrapy_spider and subfolders

run cmd

cd to  \scrapy_spider
'scrapy crawl beerspyder -o 'filename.json'

will extract up to the first 25 reviews for each beer and save it in scrapy_spider as json.
takes several hours to run.

extracts the following information:
  name <class 'str'>
  abv <class 'str'>
  score <class 'str'>
  avg_rating <class 'str'>
  num_reviews <class 'str'>
  num_ratings <class 'str'>
  wants <class 'str'>
  gots <class 'str'>
  availability <class 'str'>
  style <class 'str'>
  brewery <class 'str'>
  location <class 'str'>
  user_id <class 'str'>
  ba_score <class 'str'>
  look <class 'str'>
  smell <class 'str'>
  taste <class 'str'>
  mouth_feel <class 'str'>
  overall <class 'str'>
  text <class 'str'>
  date <class 'str'>

