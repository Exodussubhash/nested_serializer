# nested_serializer

nested-rest-api.herokuapp.com

Serializers in django rest framework are similar to django forms. By using django rest framework serializers we can serialize and deserialize the data. We can also validate the incoming data using django rest framework serializers to maintain the integrity of the data. We can divide the django rest framework serializers into two categories.

Normal Serializers

It simply validates the data and performs the serialization and de-serialization. For normal serializers we need implement the serializer methods like "save" and "update".
We also need to specify the each and every field of serializer externally and also in the serializer meta class "fields" attribute.

Model serializers

It comes with advanced features like in-built functionality for "save", "update".
Unlike the normal serializers we can simply provide "fields" in the serializer meta class and no need to write external fields.

In this project we can see how a nested serializer can be updated using django-rest framework. 

We have used model serializer.

It gives the nested view of user details having their id and time zone details with start_time and end_time of 
user activity for particular user.

