# Bluemix deployment for graphdb-slate

To deploy to bluemix, just run the deploy script.

```
./deploy
```

Yep, that's all. Okay, maybe not. If you haven't yet, you need to install the  [cloudfoundry command line tool](https://github.com/cloudfoundry/cli/releases), connect to bluemix, and log in before you run the deploy script:

```
cf api https://api.ng.bluemix.net
cf login -u $bluemix_username -o graphdborg -s docs
```

You also need to be in the graphdborg org and have developer access to the docs space.
