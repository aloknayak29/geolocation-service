## Python Flask modified Skeleton for Google App Engine for creating JSON based web services

A modified skeleton for building Python applications on Google App Engine with the
[Flask micro framework](http://flask.pocoo.org).

See other [Google Cloud Platform github
repos](https://github.com/GoogleCloudPlatform) for sample applications and
scaffolding for other python frameworks and use cases.

this web service JSON API prvides following services:
* coordinates of an area or location in India (e.g cities)
* nearby areas of an area or location in India (e.g cities)
* nearby areas(cities) of any particular coordinates

this Repository's API is for Indian Locations, but you modify/edit the numeric_cc.csv file to create services for your locations

Here is few examples of Usage of this web service JSON API:
http://opportune-lore-728.appspot.com/area_coordinates?area=bihar

http://opportune-lore-728.appspot.com/area_coordinates?area=biharsdfg

http://opportune-lore-728.appspot.com/nearby_areas/sorted?lat=29&lon=71

http://opportune-lore-728.appspot.com/nearby_areas/blocks?lat=29&lon=71



## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone https://github.com/aloknayak29/geolocation-service.git
   ```
3. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   cd geolocation-service
   pip install -r requirements.txt -t lib
   ```
4. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```
1. Congratulations!  Your application is now live at your-app-id.appspot.com

## Next Steps
This skeleton includes `TODO` markers to help you find basic areas you will want
to customize.

### Relational Databases and Datastore
To add persistence to your models, use
[NDB](https://developers.google.com/appengine/docs/python/ndb/) for
scale.  Consider
[CloudSQL](https://developers.google.com/appengine/docs/python/cloud-sql)
if you need a relational database.

### Installing Libraries
See the [Third party
libraries](https://developers.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK.  To include SDK
libraries, add them in your app.yaml file. Other than libraries included in
the SDK, only pure python libraries may be added to an App Engine project.

### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Contributing changes
See [CONTRIB.md](CONTRIB.md)

## Licensing
See [LICENSE](LICENSE)

## Author
Alok Nayak
