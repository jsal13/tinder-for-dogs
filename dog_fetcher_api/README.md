# Dog Fetcher API

## Purpose

Given a dog type (folder name, as in the Stanford Dog db), return a random picture of that dog type from S3.

## Debugging and Testing

To test this and get logs, go into this directory and run

```bash
python api.py
```

You should now be able to go to [http://localhost:5000](http://localhost:5000) to access the _Swagger_ documents.

Go to the proper namespace (probably **Default**) and click it. Then click the appropriate endpoint and follow the directions in Swagger.

**NOTE**: Flask should reload as you make changes to files, but make sure it hasn't broken and stopped if you don't see your changes made after saving and reloading the localhost page.
