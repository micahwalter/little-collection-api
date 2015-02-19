# little-collection-api
a python flask based api using RawGit and GitHub as a data source

### wha?

This is a little experiment. There is nearly no code in this thing yet. 

This just uses [RawGit](https://rawgit.com/) to turn the collection data [Cooper Hewitt has published](https://github.com/cooperhewitt/collection) as json files into a little mini-api.

Right now, it just has two endpoints
* /objects/object_id
* /people/person_id

You can try it out on Heroku here

like this for an object

    $ curl https://little-collection-api.herokuapp.com/objects/35456731

or like this for a person

    $ curl https://little-collection-api.herokuapp.com/people/18048255

### why?

In a nutshell, I'm thinking about alternative ways for institutions like [Cooper Hewitt](http://www.cooperhewitt.org) to publish collections meta-data. We already have a [collections website](http://collection.cooperhewitt.org), we have a [public API](http://collection.cooperhewitt.org/api), we have [csv files and a data dump available on GitHub](https://github.com/cooperhewitt/collection), and now this. 

Is it useful? I really can't say, but it jumps over the barrier of having to learn how to use our API and oAuth2 and whatever.

### what it's not?

It's not the API. Currently, there are only two endpoints. I may add more soon, but really, if you want the full featureset of the API, go use it for real. 

This is just an experiment. The URLs above on Heroku are just there to test it out. In other-words, don't go and use this in a production app. Also, you should read all of [RawGit's FAQs](https://rawgit.com/faq) before going too far with this. It's currently using the "dev/testing" endpoint, so keep that in mind and be nice. 
