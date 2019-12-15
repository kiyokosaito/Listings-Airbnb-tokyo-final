# Listings-Airbnb-tokyo-final
This repo is for project for Programming for Data Analysis, deadline is 16th Dec, 2019

# Fidnding the best category of listing and price range to gain reviews in Tokyo Airbnb listings to promote host's earnings opportunity

########This repo is for project for Programming for Data Analysis, deadline is 16th Dec, 2019.

## Introduction

As I am working for Airbnb, I am curious to see if there are any relationships between data that we have on our system. I chose the database that gathered Airbnb host's listings in Tokyo which contains many variables which Date Compiled was on 28 September, 2019. The aim of this project is to investigate the datasets to discuss what I found with the data set.

Airbnb is a marketplace which heavily depends on user reviews. It is very important to get good reviews for our hosts to promote their booking.

Getting more reviews would promote more earnings for our hosts because;
      -potential guests would know more accurate description of the listing apart from the listing page
      -build more trust on hosting standard
      -it would lead to our Superhost program which would give more benefitial features on our platform
      
Above factors would promote our hosts more earnings on our platform. I'll analyze existing data about hosts in Tokyo to find the best category and price range to gain reviews on their listing. To make my recommendation, I'll try to find out:

What is the best category for our hosts to receive more reviews.
Is there any relationship between price and receiving reviews.
What is the best minimum nights setting for our hosts to get more reveiws.

I adapted the database from http://insideairbnb.com/get-the-data.html Ref:[1]

There are so many variables in this data set. I picked 5 variables below in this project to investigate further.

1.room_type, 2.price, 3.minimum_nights 4.number_of_reviews, 5.calculated_host_listings_count.

1.There are 4 types of room types. +Entire house, +Hotel rooms, +Private room, +Shared room
2.Price per night of the listing
3.Minimum nights stay setting
4.Total of reviews that host earned
5.Total of listings that host published on our platform

## Summary of Results

I took 100 randum samples from the whole Tokyo listings data set (recorded in Sep 2019) and data strongly shows that entire house is the best category to earn most reviews. Less than 3 nights is the best minimum setting for getting most reviews. Under 30000JPY per night is the best price per night to get the most reviews. And less than 10 listings per host get most reveiws. This means that hosts who has more than 1 listings up to 10 lsitings, the type of listing is entire house, less than 30000 JPY per night



## Exploring Existing Data

![Annotation 2019-12-15 221138 price 4 types](https://user-images.githubusercontent.com/47428283/70870187-0c43ba80-1f88-11ea-9d86-ca332bd20bd8.jpg)

This shows that majority of listings set the price per night under 30000 JPY. 

![Annotation 2019-12-15 221608 prices individual types](https://user-images.githubusercontent.com/47428283/70870241-a9065800-1f88-11ea-92f8-1efd5f4f0ac2.jpg)

This shows that majority of entire house set the price per night also udner 30000 JPY. 

![Annotation 2019-12-15 221814 minimum](https://user-images.githubusercontent.com/47428283/70870252-d0f5bb80-1f88-11ea-835c-664d02749045.jpg)

This shows majority of entire house set minimum stay night setting less than 3 nights. 

![Annotation 2019-12-15 221850reviews](https://user-images.githubusercontent.com/47428283/70870257-e79c1280-1f88-11ea-8f84-cfcdc52802a8.jpg)

This shows more than 60 entire house hosts earned more than 50 reviews.

![Annotation 2019-12-15 221935number of listings](https://user-images.githubusercontent.com/47428283/70870267-03071d80-1f89-11ea-8bb8-ea8d1751ddb7.jpg)

This shows that more than 50 hosts of the samples has more than 10 listings.

![Annotation 2019-12-15 222056entire-minimum ](https://user-images.githubusercontent.com/47428283/70870275-32b62580-1f89-11ea-9568-347f27b3b680.jpg)

![Annotation 2019-12-15 222133entire reviews](https://user-images.githubusercontent.com/47428283/70870284-50838a80-1f89-11ea-8f35-714421b5ad51.jpg)

![Annotation 2019-12-15 222223 entire-listings numbers](https://user-images.githubusercontent.com/47428283/70870296-6a24d200-1f89-11ea-82f7-ba64ee952d0f.jpg)

These three plots shows ;

less than 3 nights on minimum stay nights setting and more than 1 but up to 10 listings that hosts published on our platform which set less than 30000JPY per night get most reviews. 


Reference
[1] Murray, C.,2014,Inside Airbnb,[Online],Available from http://insideairbnb.com/index.html,  [viewed 3rd December 2019].
